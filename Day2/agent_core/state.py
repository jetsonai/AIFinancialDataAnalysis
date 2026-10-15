from typing import TypedDict, Any


class FinanceState(TypedDict, total=False):
    # 입력 데이터
    data_file: str
    question: str
    provider: str

    # 기능 실행 노드
    data_summary: dict[str, Any]

    # LLM 실행 노드
    prompt: str
    ai_text: str

    # 결과보기 노드
    artifacts: list[str]
    view_text: str

    # 실행 상태
    status: str
    error: str
