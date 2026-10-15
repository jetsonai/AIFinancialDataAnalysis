
# AI 금융데이터 분석 실무 · 1일 차

한국폴리텍대학 광주캠퍼스 저축은행 재직자 과정의 1일 차 실습 노트입니다.
주제는 **금융데이터 분석과 예측 AI**이고, Google Colab · Pandas · Plotly · LSTM을 씁니다.

## 사용 방법

1. 아래 표에서 **Open in Colab** 배지를 누르면 Colab에서 바로 열립니다. 설치할 것은 없어요. (Google 계정으로 로그인)
2. 열리면 먼저 메뉴에서 **[파일] → [Drive에 사본 저장]** 을 누르세요. 그래야 바꾼 내용이 내 드라이브에 저장됩니다.
3. 맨 위 **"0. 실습 준비"** 셀을 실행하면 실습 데이터를 자동으로 내려받습니다. `데이터 준비 완료: True`가 나오면 성공입니다.
4. 셀은 위에서부터 순서대로 `Shift + Enter`로 실행하세요. 연결이 끊겼다면 처음부터 다시 실행하면 됩니다.
5. 코드는 **`# ←` 표시가 있는 줄만** 바꿉니다. 복습 미션의 정답은 각 노트 맨 아래에 있어요.

## 예제별 실습 노트

| 예제 | 주제 | 배우는 기술 | 시간 | 실습 노트 |
|:---:|---|---|:---:|:---:|
| 00 | 파이썬 · pandas 기초 문법 (교재 18~25쪽) | 변수 · 리스트 · 딕셔너리 · 조건 · groupby | 2교시 앞 20분 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/00_%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EA%B8%B0%EC%B4%88%EB%AC%B8%EB%B2%95_%EC%8B%A4%EC%8A%B5.ipynb) |
| 01 | 저축은행 경영지표 분석 | pandas 기초 · Plotly 막대그래프 | 50분 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/01_%EC%A0%80%EC%B6%95%EC%9D%80%ED%96%89_%EA%B2%BD%EC%98%81%EC%A7%80%ED%91%9C_%EB%B6%84%EC%84%9D.ipynb) |
| 02 | 고객 데이터와 정기예금 가입 패턴 | 딕셔너리 · 함수 · groupby · 구간 나누기 | 80분 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/02_%EA%B3%A0%EA%B0%9D%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%98%88%EA%B8%88%EA%B0%80%EC%9E%85_%ED%8C%A8%ED%84%B4.ipynb) |
| 03 | 고객 세분화 대시보드 | 대시보드 · 히트맵 · 선택 상자 | 70분 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/03_%EA%B3%A0%EA%B0%9D%EC%84%B8%EB%B6%84%ED%99%94_%EC%98%88%EA%B8%88%EC%9C%A0%EC%B9%98_%EB%8C%80%EC%8B%9C%EB%B3%B4%EB%93%9C.ipynb) |
| 03+ | [보충] 한 화면 고객 대시보드 | 카드 · 히트맵 · 막대 4개 한 화면 · 직업 선택 | 선택 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/03_extra_one_screen_dashboard.ipynb) |
| 04 | 금리 시계열 분석 | 시계열 · 전월 대비 변화 · 이동평균 | 50분 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/04_%EA%B8%88%EC%9C%B5%EC%8B%9C%EA%B3%84%EC%97%B4_%EA%B8%88%EB%A6%AC%EC%B6%94%EC%84%B8_%EB%B6%84%EC%84%9D.ipynb) |
| 05 | LSTM 금리 예측 체험 | 예측모델(LSTM) · 기준모델 비교 | 70분 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/05_LSTM_%EA%B8%88%EB%A6%AC%EC%98%88%EC%B8%A1_%EC%B2%B4%ED%97%98.ipynb) |

> 예제 02 · 03은 같은 고객 데이터를 이어 쓰고, 예제 04 · 05는 같은 금리 데이터를 이어 씁니다. 순서대로 진행하세요.

## 실습 데이터

노트의 "0. 실습 준비" 셀이 아래 파일을 자동으로 내려받습니다. 직접 받을 필요는 없어요.

| 파일 | 내용 | 쓰는 예제 |
|---|---|:---:|
| [savings_bank.csv](data/savings_bank.csv) | 저축은행 79개사 경영지표 (2026년 3월 말) | 00 · 01 |
| [bank_customers.csv](data/bank_customers.csv) | 은행 고객 마케팅 기록 45,211건 (익명화) | 00 · 02 |
| [bank_customers_prepared.csv](data/bank_customers_prepared.csv) | 예제 02에서 정리한 고객 데이터 (백업본) | 03 |
| [deposit_rate_monthly.csv](data/deposit_rate_monthly.csv) | 예금은행 수신금리 월별 2016.1 ~ 2026.6 | 04 · 05 |
| [lstm_config.json](data/lstm_config.json) | LSTM 모델 설정 (입력 길이 · 0~1 변환 기준값) | 05 |
| [lstm_deposit_rate.weights.h5](data/lstm_deposit_rate.weights.h5) | 강사가 학습한 LSTM 모델 (가중치) | 05 |

**인터넷이 막혔을 때**: 셀을 실행하면 **[파일 선택]** 버튼이 나옵니다. 강사가 USB로 나눠 드린 `data` 폴더의 파일을 고르면 됩니다.

## 꼭 지켜 주세요

- Colab은 회사 밖 클라우드입니다. **회사 고객정보나 내부자료는 Colab에 올리지 마세요.** 이 저장소의 데이터는 모두 공개 데이터입니다.
- 고객 데이터의 연령 · 직업 분석은 집단 단위 통계 교육용입니다. 개인을 고르거나 배제하는 근거로 쓰지 않습니다.
- Colab에 올리거나 만든 파일은 세션이 끝나면 사라집니다. 필요한 결과 파일은 내려받아 두세요.

## 데이터 출처와 라이선스

| 데이터 | 출처 | 라이선스 · 비고 |
|---|---|---|
| 저축은행 경영지표 | 예금보험공사 「저축은행업권 주요 경영지표 현황_20260331」 · [공공데이터포털](https://www.data.go.kr/data/15120292/fileData.do) | 이용허락범위 제한 없음 · 인코딩과 컬럼명만 정리 |
| 고객 마케팅 기록 | [UCI Machine Learning Repository · Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing) (Moro, Cortez & Rita, 2014) | CC BY 4.0 · 포르투갈 은행 2008~2010년 익명화 데이터 |
| 예금은행 수신금리 | [한국은행 경제통계시스템(ECOS)](https://ecos.bok.or.kr) · 통계표 121Y002 | 공개 통계 |

실습 결과는 공개 데이터를 이용한 교육용 예시이며, 특정 금융회사의 경영 상태나 특정 고객의 가입 가능성을 판단하는 자료가 아닙니다.

## 강사용

| 노트 | 내용 | 열기 |
|---|---|:---:|
| 05_강사용_LSTM_모델학습 | 예제 05에서 쓰는 LSTM 모델을 학습해 `lstm_config.json` · `lstm_deposit_rate.weights.h5`를 만듭니다. 교육생은 실행하지 않습니다. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jetsonai/AIFinancialDataAnalysis/blob/main/Day1/05_%EA%B0%95%EC%82%AC%EC%9A%A9_LSTM_%EB%AA%A8%EB%8D%B8%ED%95%99%EC%8A%B5.ipynb) |

---

Copyright © 2026 JetsonAI, Ltd. All rights reserved. · [jetsonai.co.kr](https://jetsonai.co.kr) · [YouTube @r-ssaem](https://www.youtube.com/@r-ssaem)
