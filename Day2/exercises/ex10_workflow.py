"""예제 10 금융업무 통합 자동화 — 데이터 분석 → Excel → 차트 → AI 보고서를 한 번에.

    from finance_agent import FinanceAgent
    agent = FinanceAgent(provider="ollama")
    agent.run_workflow(file="data/bank_customers.csv", task="고객군별 정기예금 가입률 분석 및 보고서 작성")
"""
from pathlib import Path

import pandas as pd

from exercises.common import (check_message, check_numbers, load_customers, make_chart_files,
                              output_path, overview, rate_table, split_sections, summary_json,
                              to_records, write_excel)
from exercises.ex09_report import build_report, highlights

DIMENSIONS = ["연령대", "직업군", "잔액구간", "대출상태", "과거캠페인"]
CHARTS = [("연령대", "가입률(%)", "막대"), ("잔액구간", "가입률(%)", "막대"), ("직업군", "가입률(%)", "가로막대")]
SECTIONS = ["분석 요약", "고객군별 특징", "마케팅 전략 초안", "유의사항"]


def run_function(data_file, question):
    df = load_customers(data_file)
    tables = {dim: rate_table(df, dim) for dim in DIMENSIONS}
    return {
        "업무 요청": question,
        "데이터 파일": Path(data_file).name,
        **overview(df),
        "고객군별 최고·최저": highlights(tables),
        "고객군별 가입률": {dim: to_records(t) for dim, t in tables.items()},
    }


def make_prompt(question, data_summary):
    data = {k: v for k, v in data_summary.items() if k not in ("업무 요청", "데이터 파일", "고객군별 가입률")}
    return f"""당신은 저축은행 수신기획팀의 데이터 분석 담당자입니다.
업무 요청: {question}

Pandas로 계산한 분석 결과입니다. 이 숫자만 사용하세요.
{summary_json(data)}

아래 네 제목을 대괄호까지 그대로 쓰고, 제목마다 내용을 작성하세요.
[분석 요약]
(업무 요청에 맞춰 핵심 결과 3문장)
[고객군별 특징]
(고객군 기준마다 글머리 1개, 최고·최저 가입률 숫자 포함)
[마케팅 전략 초안]
(정기예금 가입률 향상 방안 3개, 각각 "대상 · 방법 · 확인 지표"를 한 줄로)
[유의사항]
(해석상 주의점 2개)

데이터에 없는 숫자는 쓰지 말고, 연령·직업만으로 개인을 고르거나 배제하는 방안은 쓰지 마세요."""


def show_result(data_summary, ai_text):
    check = check_numbers(ai_text, data_summary)
    tables = {dim: pd.DataFrame(rows) for dim, rows in data_summary["고객군별 가입률"].items()}
    basics = {k: data_summary[k] for k in ("전체 고객수", "전체 가입자수", "전체 가입률(%)")}
    overall = data_summary["전체 가입률(%)"]
    stem = Path(data_summary["데이터 파일"]).stem
    tag = "" if stem == "bank_customers" else f"_{stem}"

    excel = write_excel(output_path(f"ex10_고객군별_가입률_분석{tag}.xlsx"), basics, tables,
                        f"{ai_text}\n\n{check_message(check)}")
    chart_files = []
    for dim, metric, kind in CHARTS:
        chart_files += make_chart_files(tables[dim], dim, metric, kind, overall, f"ex10_{dim}_가입률{tag}")
    pngs = [f for f in chart_files if f.endswith(".png")]
    sections = split_sections(ai_text, SECTIONS)
    report = build_report(output_path(f"ex10_정기예금_가입률_향상_보고서{tag}.docx"),
                          "정기예금 가입률 향상을 위한 고객관리 방안", data_summary["업무 요청"],
                          data_summary, sections, pngs, check)
    return {"files": [excel, report] + chart_files, "message": f"{ai_text}\n\n{check_message(check)}"}
