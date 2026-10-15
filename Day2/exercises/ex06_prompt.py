"""예제 06 금융업무 프롬프트 작성 — 같은 데이터, 다른 지시문 → 다른 결과.

노트북에서 TEMPLATE_NAME 만 바꿔 가며 결과를 비교합니다.
    from exercises import ex06_prompt
    ex06_prompt.TEMPLATE_NAME = "보고서문장"
"""
from datetime import datetime

from exercises.common import (check_message, check_numbers, load_customers, output_path,
                              overview, pick_dimensions, rate_table, summary_json, to_records)

TEMPLATE_NAME = "분석요약"     # "단순" / "분석요약" / "보고서문장" / "검토의견"

TEMPLATES = {
    # 비교용: 역할·목적·기준·형식 없이 질문과 숫자만 던지는 프롬프트
    "단순": """{question}

{data}""",

    # 템플릿 ① 분석 요약형
    "분석요약": """[역할] 당신은 저축은행 수신기획팀의 데이터 분석 담당자입니다.
[업무 목적] 정기예금 유치 전략 회의에서 쓸 고객 분석 요약을 작성합니다.
[업무 요청] {question}

[분석 데이터] 아래는 Pandas로 계산한 결과입니다. 이 숫자만 사용하세요.
{data}

[분석 기준]
- 전체 가입률과 비교해 높은 고객군과 낮은 고객군을 나누세요.
- 고객수가 적은 고객군은 "고객수가 적어 해석 주의"라고 표시하세요.
- 데이터에 없는 숫자나 원인을 지어내지 마세요.

[출력 형식]
1. 핵심 요약 (2문장)
2. 가입률이 높은 고객군 (글머리 3개 이내, 가입률 숫자 포함)
3. 가입률이 낮은 고객군 (글머리 3개 이내, 가입률 숫자 포함)
4. 유의사항 (1문장)
한국어로 400자 안팎으로 작성하세요.""",

    # 템플릿 ② 보고서 문장형
    "보고서문장": """[역할] 당신은 저축은행 경영기획부의 업무보고서 작성 담당자입니다.
[업무 목적] 내부 업무보고서의 '주요 현황' 부분에 들어갈 문장을 작성합니다.
[업무 요청] {question}

[분석 데이터] 아래는 Pandas로 계산한 결과입니다. 이 숫자만 사용하세요.
{data}

[작성 기준]
- 보고서 문체로 씁니다. (예: "~로 나타남", "~할 필요가 있음")
- 수치는 데이터에 있는 그대로 쓰고, 새로 계산하지 마세요.
- "반드시", "확실히" 같은 단정 표현은 쓰지 마세요.

[출력 형식]
제목 1줄, 그 아래 본문 3문단 이내 (문단마다 2~3문장)""",

    # 템플릿 ③ 검토 의견형
    "검토의견": """[역할] 당신은 저축은행 리스크관리·준법감시 관점의 검토자입니다.
[업무 목적] 아래 분석 결과를 영업 전략에 쓰기 전에 주의할 점을 검토합니다.
[업무 요청] {question}

[분석 데이터] 아래는 Pandas로 계산한 결과입니다.
{data}

[검토 기준]
1. 해석의 한계 (함께 나타난 것과 원인은 다름, 고객수가 적은 집단)
2. 고객 보호 (연령·직업만으로 특정 고객을 고르거나 배제하는 위험)
3. 결론 전에 추가로 확인할 데이터

[출력 형식]
검토 기준 1~3마다 제목을 달고 글머리 2개씩, 한국어로 작성하세요.""",
}


def run_function(data_file, question):
    df = load_customers(data_file)
    summary = {"업무 요청": question, **overview(df)}
    for dim in pick_dimensions(question):
        summary[f"{dim}별 가입률"] = to_records(rate_table(df, dim))
    return summary


def make_prompt(question, data_summary):
    data = {k: v for k, v in data_summary.items() if k != "업무 요청"}
    return TEMPLATES[TEMPLATE_NAME].format(question=question, data=summary_json(data))


def show_result(data_summary, ai_text):
    check = check_numbers(ai_text, data_summary)
    log = output_path("ex06_프롬프트_비교기록.md")
    with open(log, "a", encoding="utf-8") as f:
        f.write(f"\n\n## [{TEMPLATE_NAME}] {datetime.now():%H:%M:%S}\n\n")
        f.write(f"**질문**: {data_summary['업무 요청']}\n\n{ai_text}\n\n{check_message(check)}\n")
    return {"files": [str(log)], "message": f"{ai_text}\n\n{check_message(check)}"}
