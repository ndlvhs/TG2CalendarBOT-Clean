def parse_with_gpt(text):
    today = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
    Ты помощник по организации задач. Сегодняшняя дата: {today}.
    Я отправлю тебе текст сообщения на русском языке.

    Твоя задача:
    - Извлечь дату (в формате ГГГГ-ММ-ДД)
    - Извлечь время (в формате ЧЧ:ММ)
    - Извлечь краткое название события

    Если в тексте встречаются такие фразы, как "завтра", "послезавтра", "через два дня", "в пятницу", 
    ты должен вычислить соответствующую дату, опираясь на сегодняшнюю дату: {today}.
    Примечание: для слов типа "завтра" вычисли **следующую дату**; для "в пятницу" — вычисли ближайшую пятницу от сегодняшнего дня.

    Отвечай только в формате JSON:
    {{
      "date": "2025-04-29",
      "time": "18:00",
      "event": "тренировка джиу джитсу"
    }}

    Если дата или время непонятны, ответь:
    {{
      "error": "Не могу определить дату/время"
    }}

    Текст: "{text}"
    """

    try:
        print(f"OpenAI API Key: {os.getenv('OPENAI_API_KEY')}")
        print(f"Sending prompt to OpenAI: {prompt}")
        
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты помощник по парсингу событий."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=300,
        )
        
        # Логируем ответ от OpenAI
        print(f"OpenAI Response: {response}")

        message = response['choices'][0]['message']['content']
        return json.loads(message)

    except Exception as e:
        print(f"Ошибка при запросе к OpenAI: {e}")
        return {"error": "Ошибка запроса"}