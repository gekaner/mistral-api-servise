from pydantic import BaseModel
from typing import Optional


class PromptRequest(BaseModel):
    """Модель запроса с промптом."""
    service: str
    user: str


class LLMResponse(BaseModel):
    """Модель ответа от LLM."""
    response: Optional[str] = None
    error: Optional[str] = None
    success: bool = True


class HealthResponse(BaseModel):
    """Модель ответа для проверки здоровья сервиса."""
    status: str
    api_configured: bool
