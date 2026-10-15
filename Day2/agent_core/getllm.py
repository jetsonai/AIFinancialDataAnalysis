import os
from langchain_openai import ChatOpenAI

import llm_config as cfg


def getllm(provider="ollama"):
    if provider == "ollama":
        return ChatOpenAI(
            model=os.getenv("OLLAMA_MODEL", cfg.OLLAMA_MODEL),
            base_url=os.getenv("OLLAMA_URL", cfg.OLLAMA_URL),
            api_key="ollama",
            temperature=0,
            timeout=cfg.OLLAMA_TIMEOUT,
        )

    if provider == "gemini":
        return ChatOpenAI(
            model=os.environ["GEMINI_MODEL"],
            base_url=cfg.GEMINI_URL,
            api_key=os.environ["GEMINI_API_KEY"],
            temperature=0,
        )

    if provider == "openai":
        return ChatOpenAI(
            model=os.environ["OPENAI_MODEL"],
            api_key=os.environ["OPENAI_API_KEY"],
            temperature=0,
        )

    raise ValueError("지원하지 않는 AI 모델입니다.")
