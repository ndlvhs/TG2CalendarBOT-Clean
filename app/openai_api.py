import openai
import os
import json

# Устанавливаем ключ API
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_to_openai(prompt):
    try:
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

        # Получаем и возвращаем ответ в виде JSON
        message = response['choices'][0]['message']['content']
        return json.loads(message)
    
    except Exception as e:
        print(f"Ошибка при запросе к OpenAI: {e}")
        return {"error": "Ошибка запроса"}