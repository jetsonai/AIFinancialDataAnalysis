import re
from pathlib import Path
from importlib import import_module

from langgraph.graph import StateGraph, START, END

from agent_core.state import FinanceState
from agent_core.getllm import getllm

# 강사가 승인한 실습 모듈만 불러옵니다 (허용 목록)
EXERCISES = {
    "ex06": "exercises.ex06_prompt",
    "ex07": "exercises.ex07_excel",
    "ex08": "exercises.ex08_chart",
    "ex09": "exercises.ex09_report",
    "ex10": "exercises.ex10_workflow",
}


def clean_text(text):
    """생각(thinking) 모델이 붙이는 <think>...</think> 부분을 지우고 앞뒤 공백을 정리합니다."""
    return re.sub(r"<think>.*?</think>", "", str(text), flags=re.DOTALL).strip()


def build_agent(exercise_id):
    lesson = import_module(EXERCISES[exercise_id])

    def check_node(state: FinanceState):
        path = Path(state["data_file"])
        if not path.is_file():
            raise FileNotFoundError(path)
        if path.suffix.lower() != ".csv":
            raise ValueError("CSV 파일만 허용합니다.")
        return {"status": "ready"}

    def function_node(state: FinanceState):
        summary = lesson.run_function(state["data_file"], state["question"])
        return {"data_summary": summary}

    def prompt_node(state: FinanceState):
        prompt = lesson.make_prompt(state["question"], state["data_summary"])
        llm = getllm(state.get("provider", "ollama"))
        answer = llm.invoke(prompt)
        return {"prompt": prompt, "ai_text": clean_text(answer.content)}

    def result_node(state: FinanceState):
        result = lesson.show_result(state["data_summary"], state["ai_text"])
        return {"artifacts": result["files"], "view_text": result["message"], "status": "done"}

    builder = StateGraph(FinanceState)

    builder.add_node("check", check_node)
    builder.add_node("function", function_node)
    builder.add_node("prompt", prompt_node)
    builder.add_node("result", result_node)

    builder.add_edge(START, "check")
    builder.add_edge("check", "function")
    builder.add_edge("function", "prompt")
    builder.add_edge("prompt", "result")
    builder.add_edge("result", END)

    return builder.compile()
