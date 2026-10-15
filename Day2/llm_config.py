"""AI 연결 설정 (강사가 수업 전에 확인하는 파일)

교육생은 이 파일을 고치지 않습니다.
모델을 바꾸려면 아래 값만 수정하거나, 노트북에서 os.environ[...] 로 덮어씁니다.
"""

# 기본 AI 공급자: "ollama"(각 PC의 로컬 Qwen) / "gemini" / "openai"
PROVIDER = "ollama"

# ── 로컬 Ollama ──────────────────────────────────────────────
# qwen3:4b-instruct = 생각 과정(<think>)을 출력하지 않는 지시형 모델 (약 2.5GB)
# 주의: "qwen3:4b" 는 생각(thinking) 모델이라 느리고 생각 과정이 함께 출력됩니다.
OLLAMA_MODEL = "qwen3:4b-instruct"
OLLAMA_URL = "http://127.0.0.1:11434/v1"
OLLAMA_TIMEOUT = 300        # 초. GPU 없이 CPU로 돌면 답변이 1분 이상 걸릴 수 있습니다.

# ── 선택 실습: 개인 API 키가 있는 교육생만 ─────────────────
# 모델 ID는 자주 바뀝니다. 수업 당일 각 회사 문서에서 확인한 이름을 노트북에서 넣습니다.
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
