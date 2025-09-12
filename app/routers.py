from fastapi import APIRouter, HTTPException
from app.models import PromptRequest, LLMResponse, HealthResponse
from app.utils import mistral
from config import API_KEY

router = APIRouter()


@router.post("/prompt", response_model=LLMResponse)
async def process_prompt(request: PromptRequest):
    """
    Обрабатывает промпт и отправляет его в LLM.
    
    Args:
        request: Запрос с полями service и user
    
    Returns:
        LLMResponse: Ответ от LLM или ошибка
    """
    try:
        # Проверяем, что поля не пустые
        if not request.service or not request.user:
            raise HTTPException(
                status_code=400, 
                detail="Поля 'service' и 'user' не могут быть пустыми"
            )
        
        # Формируем сообщение для LLM в правильном формате
        message = [
            {"role": "system", "content": request.service},
            {"role": "user", "content": request.user}
        ]
        
        # Отправляем в LLM
        llm_response = mistral(message)
        
        if llm_response is None:
            return LLMResponse(
                response=None,
                error="Таймаут или ошибка при обращении к LLM",
                success=False
            )
        
        return LLMResponse(
            response=llm_response,
            error=None,
            success=True
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Внутренняя ошибка сервера: {str(e)}"
        )


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Проверяет состояние сервиса.
    
    Returns:
        HealthResponse: Статус сервиса и его компонентов
    """
    api_configured = API_KEY is not None and API_KEY != "your_mistral_api_key_here"
    
    status = "healthy" if api_configured else "unhealthy"
    
    return HealthResponse(
        status=status,
        api_configured=api_configured
    )
