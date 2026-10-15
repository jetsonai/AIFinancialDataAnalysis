"""교육생이 쓰는 FinanceAgent 클래스.

    from finance_agent import FinanceAgent
    agent = FinanceAgent(provider="ollama")
    agent.ask("정기예금이 무엇인지 한 문장으로 설명해 주세요.")            # AI에게 바로 질문
    agent.run("ex07", "data/bank_customers.csv", "직업군별 가입률 분석")   # 예제 모듈 실행
    agent.run_workflow(file="data/bank_customers.csv", task="...")        # 예제 10 통합 실행

내부에서는 agent_core.graph.build_agent()가 만든 LangGraph 워크플로
(입력 검증 → 금융업무 기능 → 프롬프트·LLM → 결과보기)를 실행합니다.
"""
import time

import llm_config
from agent_core.getllm import getllm
from agent_core.graph import EXERCISES, build_agent, clean_text


class FinanceAgent:
    def __init__(self, provider=None):
        self.provider = provider or llm_config.PROVIDER
        self.last_result = None

    def ask(self, prompt, show=True):
        """프롬프트를 AI에게 그대로 보내고 답을 돌려줍니다."""
        start = time.time()
        answer = clean_text(getllm(self.provider).invoke(prompt).content)
        if show:
            print(answer)
            print(f"\n⏱ {time.time() - start:.1f}초 · {self.provider}")
        return answer

    def run(self, exercise, file, question, show=True):
        """예제 모듈(ex06~ex10)을 공통 워크플로로 실행합니다."""
        if exercise not in EXERCISES:
            raise ValueError(f"사용할 수 있는 예제: {list(EXERCISES)}")
        start = time.time()
        result = build_agent(exercise).invoke({
            "data_file": str(file),
            "question": question,
            "provider": self.provider,
        })
        result["seconds"] = round(time.time() - start, 1)
        self.last_result = result
        if show:
            self.show(result)
        return result

    def run_workflow(self, file, task, show=True):
        """예제 10: 데이터 분석 → Excel → 차트 → AI 보고서를 한 번에 실행합니다."""
        return self.run("ex10", file, task, show=show)

    @staticmethod
    def show(result):
        print(result["view_text"])
        print("\n📁 만들어진 파일")
        for f in result.get("artifacts", []):
            print("  -", f)
        print(f"\n⏱ {result.get('seconds', '-')}초 · 상태: {result.get('status')}")
