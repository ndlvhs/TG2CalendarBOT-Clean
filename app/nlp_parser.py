import openai
import dateparser
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def extract_task_info(text):
    # Можем использовать OpenAI, но для базового MVP просто парсим дату
    parsed_date = dateparser.parse(text, languages=['en', 'ru'])

    # Простая логика: если нашли дату — оставляем текст задачи без даты
    if parsed_date:
        clean_text = text.replace(str(parsed_date.date()), '').strip()
        return clean_text, parsed_date
    else:
        return text, None