import openai
import os
import json
from datetime import datetime

# Загружаем ключ OpenAI из переменных окружения
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_with_gpt(text):
    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
Ты помощник по организации задач. Сегодняшняя дата: {today}.

Я отправлю тебе текст сообщения на русском языке.

Твоя задача:
- Извлечь дату (в формате ГГГГ-ММ-ДД)
- Извлечь время (в формате ЧЧ:ММ)
- Извлечь краткое название события

Если во входном тексте написано "завтра", "послезавтра", "через два дня", "в пятницу" и подобные фразы, 
ты обязан рассчитать реальную дату, начиная от сегодняшней даты: {today}.

Отвечай только в формате JSON:

{{
  "date": "2025-04-29",
  "time": "18:00",
  "event": "тренировка джиу джитсу"
}}

Если дата или время непонятны — ответь так:
{{
  "error": "Не могу определить дату/время"
}}

Текст пользователя:
"{text}"
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты помощник по парсингу событий."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=300,
        )
        message = response['choices'][0]['message']['content']
        return json.loads(message)

    except Exception as e:
        print(f"Ошибка при запросе к OpenAI: {e}")
        return {"error": "Ошибка запроса"}