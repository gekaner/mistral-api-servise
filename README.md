# LLM Service

Простой сервис на FastAPI для работы с LLM через POST запросы с промптами.

## Описание

Сервис принимает POST запросы с промптом в формате `{"service": "", "user": ""}`, форматирует их для LLM и отправляет в Mistral для получения ответа.

## Установка и запуск

### Локальный запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Настройте переменные окружения в файле `.env`:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

3. Запустите приложение:
```bash
python main.py
```

### Docker запуск

1. Настройте переменные окружения в файле `.env`
2. Запустите через docker-compose:
```bash
docker-compose up --build
```

## API Endpoints

### POST /api/v1/prompt
Обрабатывает промпт и отправляет в LLM.

**Тело запроса:**
```json
{
  "service": "Ты помощник по программированию",
  "user": "Как создать REST API на Python?"
}
```

**Ответ:**
```json
{
  "response": "Ответ от LLM",
  "error": null,
  "success": true
}
```

### GET /api/v1/health
Проверяет состояние сервиса.

**Ответ:**
```json
{
  "status": "healthy",
  "api_configured": true
}
``
```
