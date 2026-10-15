"""예제 08 금융 차트 자동 생성 — 자연어 요청 → (정해진 목록으로 해석) → 차트 + AI 설명.

예) "연령대별 가입률 막대그래프, 잔액 구간별 고객 분포, 직업군별 가입률 가로막대"
"""
import re

from exercises.common import (check_message, check_numbers, load_customers, make_chart_files,
                              overview, pick_dimensions, rate_table, summary_json, to_records)
import pandas as pd

DEFAULT_REQUEST = "연령대별 가입률 막대그래프, 잔액 구간별 고객 분포 막대그래프, 직업군별 가입률 가로막대"


def parse_request(question):
    """요청 문장을 차트 목록으로 바꿉니다. 쉼표·줄바꿈·'그리고'로 나눈 조각마다 하나씩."""
    specs = []
    for part in re.split(r"[,\n]|그리고", question):
        dims = pick_dimensions(part, default=())
        if not dims:
            continue
        metric = "고객수" if re.search(r"고객\s*수|분포|인원|몇 명", part) else "가입률(%)"
        if "가로" in part:
            kind = "가로막대"
        elif re.search(r"원그래프|원 그래프|파이|비중", part):
            kind = "원" if metric == "고객수" else "막대"    # 가입률은 원그래프로 그리지 않음
        else:
            kind = "막대"
        specs.append({"기준": dims[0], "지표": metric, "형태": kind})
    return specs


def run_function(data_file, question):
    df = load_customers(data_file)
    specs = parse_request(question) or parse_request(DEFAULT_REQUEST)
    charts = []
    for spec in specs[:4]:                                 # 한 번에 최대 4개
        charts.append({**spec, "데이터": to_records(rate_table(df, spec["기준"]))})
    return {"요청": question, **overview(df), "차트": charts}


def make_prompt(question, data_summary):
    data = {k: v for k, v in data_summary.items() if k != "요청"}
    names = "\n".join(f"[차트 {i}] {c['기준']}별 {c['지표']} ({c['형태']})"
                      for i, c in enumerate(data_summary["차트"], start=1))
    return f"""당신은 저축은행 고객관리팀의 데이터 분석 담당자입니다.
아래 차트들을 보고서에 넣으려고 합니다. 차트마다 읽는 사람이 바로 이해할 설명을 써 주세요.

차트 목록:
{names}

차트에 쓰인 데이터 (Pandas 계산 결과, 전체 가입률 {data_summary['전체 가입률(%)']}%):
{summary_json(data)}

작성 방법:
- 차트마다 [차트 번호] 제목을 쓰고, 그 아래 "주요 특징" 2줄과 "시사점" 1줄을 씁니다.
- 숫자는 데이터에 있는 값만 씁니다.
- 고객수가 적은 고객군은 해석에 주의하라고 덧붙입니다."""


def show_result(data_summary, ai_text):
    overall = data_summary["전체 가입률(%)"]
    files = []
    for i, chart in enumerate(data_summary["차트"], start=1):
        stem = f"ex08_차트{i}_{chart['기준']}_{'가입률' if chart['지표'] == '가입률(%)' else '고객수'}"
        files += make_chart_files(pd.DataFrame(chart["데이터"]), chart["기준"], chart["지표"],
                                  chart["형태"], overall, stem)
    check = check_numbers(ai_text, data_summary)
    return {"files": files, "message": f"{ai_text}\n\n{check_message(check)}"}
