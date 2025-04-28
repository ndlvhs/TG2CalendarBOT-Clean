import openai
import os

# Устанавливаем ключ API 
openai.api_key = os.getenv("OPENAI_API_KEY")

def send_to_openai(text):
    try:
        # Новый метод API для создания Completion
        response = openai.completions.create(
            model="gpt-4",  # Убедись, что используешь нужную модель
            prompt=text,     # Здесь передаём текст запроса
            max_tokens=150,  # Количество токенов для ответа
            temperature=0.7  # Степень случайности в ответе (чем выше, тем менее предсказуемо)
        )
        
        # Возвращаем ответ от OpenAI
        return response
    except Exception as e:
        print(f"Ошибка при запросе к OpenAI: {e}")
        return {"error": "Ошибка запроса"}

# Пример использования
if __name__ == "__main__":
    prompt = "Какой сегодня день?"
    response = send_to_openai(prompt)
    print(f"Ответ от OpenAI: {response}")