"""예제 07 Excel 업무 자동화 — 고객군별 가입률 집계 → AI 해석 → 서식이 적용된 Excel 보고서."""
from pathlib import Path

import pandas as pd

from exercises.common import (check_message, check_numbers, load_customers, output_path,
                              overview, rate_table, summary_json, to_records, write_excel)

DIMENSIONS = ["연령대", "직업군", "잔액구간", "대출상태"]     # Excel 시트로 만들 고객군 기준


# 1. 금융업무 기능 (정답이 있는 계산은 Pandas가)
def run_function(data_file, question):
    df = load_customers(data_file)
    return {
        "업무 요청": question,
        "데이터 파일": Path(data_file).name,
        **overview(df),
        "고객군별 가입률": {dim: to_records(rate_table(df, dim)) for dim in DIMENSIONS},
    }


# 2. LLM 업무 프롬프트 (해석과 문장은 AI가)
def make_prompt(question, data_summary):
    data = {k: v for k, v in data_summary.items() if k not in ("업무 요청", "데이터 파일")}
    return f"""당신은 저축은행의 데이터 분석 담당자입니다.
업무 요청: {question}

아래는 Pandas로 계산한 분석 결과입니다.
{summary_json(data)}

다음 내용을 한국어로 작성하세요.
1. 주요 분석 결과 (고객군 기준마다 1줄, 가입률 숫자 포함)
2. 특이사항 (전체 가입률 {data_summary['전체 가입률(%)']}%와 크게 다른 고객군, 고객수가 적은 고객군)
3. 실무 적용 아이디어 (2개)

입력 데이터에 없는 숫자를 만들지 마세요. 500자 안팎으로 작성하세요."""


# 3. 결과보기 (파일 만들기는 Python이)
def show_result(data_summary, ai_text):
    tables = {dim: pd.DataFrame(rows) for dim, rows in data_summary["고객군별 가입률"].items()}
    basics = {k: data_summary[k] for k in ("전체 고객수", "전체 가입자수", "전체 가입률(%)")}
    stem = Path(data_summary["데이터 파일"]).stem
    name = "고객별_예금가입_분석.xlsx" if stem == "bank_customers" else f"고객별_예금가입_분석_{stem}.xlsx"
    check = check_numbers(ai_text, data_summary)
    path = write_excel(output_path(name), basics, tables, f"{ai_text}\n\n{check_message(check)}")
    return {"files": [path], "message": f"{ai_text}\n\n{check_message(check)}"}
