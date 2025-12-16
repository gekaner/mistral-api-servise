from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import router
from config import HOST, PORT, DEBUG

# Создаем экземпляр FastAPI
app = FastAPI(
    title="LLM Service",
    version="1.0.0",
    debug=DEBUG
)

# Добавляем CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты
app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root():
    """Корневой эндпоинт."""
    return {
        "message": "LLM Service API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/api/v1/health"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG
    )