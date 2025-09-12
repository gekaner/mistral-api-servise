#!/usr/bin/env python3

print("Начинаем тестирование импортов...")

try:
    print("1. Импортируем FastAPI...")
    from fastapi import FastAPI
    print("✓ FastAPI импортирован успешно")
except Exception as e:
    print(f"✗ Ошибка импорта FastAPI: {e}")

try:
    print("2. Импортируем конфигурацию...")
    from config import HOST, PORT, DEBUG
    print(f"✓ Конфигурация импортирована: HOST={HOST}, PORT={PORT}, DEBUG={DEBUG}")
except Exception as e:
    print(f"✗ Ошибка импорта конфигурации: {e}")

try:
    print("3. Импортируем роутеры...")
    from app.routers import router
    print("✓ Роутеры импортированы успешно")
except Exception as e:
    print(f"✗ Ошибка импорта роутеров: {e}")

try:
    print("4. Импортируем модели...")
    from app.models import PromptRequest, LLMResponse
    print("✓ Модели импортированы успешно")
except Exception as e:
    print(f"✗ Ошибка импорта моделей: {e}")

try:
    print("5. Импортируем утилиты...")
    from app.utils import mistral
    print("✓ Утилиты импортированы успешно")
except Exception as e:
    print(f"✗ Ошибка импорта утилит: {e}")

print("Тестирование завершено!")

