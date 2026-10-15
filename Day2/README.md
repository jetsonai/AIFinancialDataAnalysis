# AI 금융데이터 분석 실무 · 2일 차 실습 폴더

(base) PS C:\FDA> 

irm https://ollama.com/install.ps1 | iex

conda install git  

git clone https://github.com/jetsonai/AIFinancialDataAnalysis


 python -c "import pandas, plotly, matplotlib, openpyxl, docx, langgraph, langchain_openai; print('설치 확인 완료')"   
 

(1일 차 예제 01~05는 Google Colab, 2일 차 예제 06~10은 이 폴더로 강의실 PC의 Jupyter에서 진행합니다.)

생성형 AI 금융업무 에이전트 · Jupyter · Ollama · Qwen · FinanceAgent

이 폴더를 강의실 PC마다 그대로 복사해 쓰면 됩니다 (예: `C:\AI금융실무\Day2`).
**노트북은 반드시 이 폴더에서 열어야** `finance_agent`, `exercises` 등을 불러올 수 있습니다.

## 1. 폴더 구성

| 파일·폴더 | 내용 | 교육생 수정 |
|---|---|---|
| `06-0_환경점검.ipynb` | 2일 차 시작 전 패키지 · Ollama · 모델 · 첫 대화 확인 | - |
| `06` ~ `10` `*.ipynb` | 예제 노트북 5개 (08은 선택) | 노트북 안의 `# ← 바꿔 보세요` 줄만 |
| `finance_agent.py` | 교육생이 쓰는 FinanceAgent 클래스 (`ask`, `run`, `run_workflow`) | 고정 |
| `llm_config.py` | AI 연결 설정 (모델 이름, 주소, 대기 시간) | 강사만 |
| `agent_core/` | LangGraph 공통 프레임워크 (State · getllm · 4개 노드 그래프) | 고정 |
| `exercises/` | 예제별 모듈 `ex06`~`ex10` (run_function · make_prompt · show_result) + 공통 도구 `common.py` | 고정 |
| `data/` | `bank_customers.csv`(주 실습), `savings_bank.csv`(보조) | - |
| `templates/report_template.docx` | Word 보고서 양식 (맑은 고딕, 머리글) | 회사 양식으로 교체 가능 |
| `outputs/` | Excel · 차트 · Word 결과가 저장되는 곳 | - |
| `requirements.txt` | Anaconda에 없는 패키지 3개 | - |

## 2. 강의실 PC 준비 (수업 전날, PC마다 1회)

1. **Ollama 설치**: https://ollama.com/download 에서 Windows용 설치. 설치 후 작업 표시줄에 라마 아이콘이 보이면 실행 중입니다.
   - RTX 50 시리즈(5060 등)는 **최신 Ollama + 최신 NVIDIA 드라이버**를 권장합니다. 오래된 버전은 GPU를 못 잡고 CPU로 느리게 돌 수 있습니다.
2. **모델 받기** (명령 프롬프트, PC당 약 2.5GB):
   ```
   ollama pull qwen3:4b-instruct
   ```
   - `qwen3:4b`(생각 모델)가 아니라 **`qwen3:4b-instruct`** 입니다. 생각 모델은 느리고 생각 과정이 함께 출력됩니다.
   - 20대가 동시에 받으면 오래 걸리므로 전날 받아 둡니다. 한 PC에서 받은 뒤 `C:\Users\<사용자>\.ollama\models` 폴더를 다른 PC의 같은 위치로 복사해도 됩니다.
3. **패키지 설치** (Anaconda Prompt에서 이 폴더로 이동한 뒤):
   ```
   pip install -r requirements.txt
   ```
   (pandas · plotly · matplotlib · openpyxl · jupyter는 Anaconda에 이미 들어 있습니다.)
4. **확인**: 이 폴더에서 `jupyter notebook` 실행 → `06-0_환경점검.ipynb`를 위에서부터 실행해 모두 ✅인지 확인합니다.
   - `ollama ps`의 PROCESSOR가 `100% GPU`면 정상입니다. 답변 한 번에 보통 수 초~20초 정도 걸립니다.

## 3. 예제 한눈에와 시간표 (50분 수업 × 8교시)

| 구간 | 노트북 | 필수 단계 | 결과물 (outputs/) | 시간 |
|---|---|---|---|---|
| 1교시 앞 | 1일 차 복습 + 로컬 AI 소개 + `06-0_환경점검` | 전부 | - | 40분 |
| 06 | 금융업무 프롬프트 작성 | 06-1 ~ 06-11 | 프롬프트 템플릿 3종 + `ex06_프롬프트_비교기록.md` | 60분 |
| 07 | Excel 업무자동화 에이전트 | 07-1 ~ 07-5, 07-7 | `고객별_예금가입_분석.xlsx` | 60분 |
| 08 **[선택]** | 금융차트 자동생성 에이전트 | 08-2, 08-3 | 차트 PNG · HTML + AI 설명 | 40분 (안 하면 여유) |
| 09 | 업무보고서 · 공문작성 에이전트 | 09-1 ~ 09-5 | `정기예금_가입률_향상_전략보고서.docx` · `내부기안문_초안.docx` | 55분 |
| 10 | 금융업무 통합자동화 에이전트 | 10-1 ~ 10-4 | Excel + 차트 3종 + Word 보고서 일괄 | 40분 |
| 여유 | 따라잡기 · 질문 · 개별 지도 | - | - | 55분 |
| 합계 | | | | 400분 |
| 8교시 | 수행평가(결과물 확인) + 과정 정리 · 자리 정리 | - | - | 50분 |

- 각 노트북의 `[선택]` 단계와 복습 미션은 시간이 남을 때만 합니다. 복습 미션은 정답 셀 실행으로 확인하는 것이 기본입니다.
- 08을 건너뛰어도 09 · 10은 그대로 진행되며, 차트는 09 · 10에서 자동으로 만들어집니다.

## 4. 동작 원리 (설계안과 같음)

```
START → check(입력 검증) → function(Pandas 계산) → prompt(프롬프트 + 로컬 AI) → result(Excel·차트·Word) → END
```

- 숫자 · 표 · 차트 · 파일은 Python이 만들고, AI는 계산 결과를 해석하는 문장만 씁니다.
- 결과마다 **숫자 검증** 줄이 붙습니다. AI 문장 속 숫자 중 계산 결과에 없는 숫자를 자동으로 찾아 "확인 필요"로 보여 줍니다.

## 5. 자주 생기는 문제

| 증상 | 해결 |
|---|---|
| `ModuleNotFoundError: finance_agent` | 노트북을 이 폴더 밖에서 열었음 → 이 폴더에서 `jupyter notebook` 다시 실행 |
| `ModuleNotFoundError: langgraph` 등 | `06-0_환경점검`의 설치 셀 실행 후 Kernel → Restart |
| `Connection refused` / `URLError` | Ollama가 꺼져 있음 → 시작 메뉴에서 Ollama 실행 |
| `model "qwen3:4b-instruct" not found` | `ollama pull qwen3:4b-instruct` |
| 답변이 1분 이상 걸림 | GPU를 못 쓰고 있음(`ollama ps` 확인) → 드라이버·Ollama 업데이트. 급하면 `llm_config.py`의 `OLLAMA_TIMEOUT`을 늘림 |
| 답변에 `<think>`가 보임 | 생각 모델을 쓰는 중 → `llm_config.py`의 모델이 `qwen3:4b-instruct`인지 확인 |
| Excel 저장 오류 `PermissionError` | 같은 Excel 파일이 열려 있음 → Excel을 닫고 다시 실행 |
| 보고서의 AI 문단이 한 곳에 몰림 | 작은 모델이 `[제목]` 형식을 안 지킴 → 다시 실행하거나 요청을 짧게 |

## 6. 데이터 주의

`bank_customers.csv`는 한국 저축은행 고객정보가 아니라 포르투갈 은행의 2008~2010년 익명화 마케팅 데이터(UCI Bank Marketing)입니다.
결과물은 교육용 초안이며, 실제 영업전략 확정이나 특정 고객의 가입 가능성 판단에 쓰지 않습니다.
외부 AI(Gemini · OpenAI)에는 공개 데이터만 입력합니다.
