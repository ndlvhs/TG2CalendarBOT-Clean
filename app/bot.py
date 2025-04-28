import logging
from aiogram import Bot, Dispatcher, types, executor
import os
from openai_api import send_to_openai  # Импортируем функцию из openai_api.py

# Инициализация бота
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Логирование для отладки
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я помогу тебе добавить задачу в календарь. Просто напиши её в свободной форме!")

@dp.message_handler()
async def echo_message(message: types.Message):
    user_text = message.text
    print(f"Received message: {user_text}")  # Логируем полученное сообщение

    # Парсим с GPT, используя функцию из openai_api.py
    parsed = send_to_openai(user_text)
    print(f"Parsed response: {parsed}")  # Логируем ответ GPT

    # Далее обработка данных
    if "error" in parsed:
        await message.answer("❌ Не смог распознать дату и время. Попробуй уточнить.")
    else:
        date = parsed["date"]
        time = parsed["time"]
        event = parsed["event"]
        await message.answer(f"✅ Задача добавлена: {event} на {date} в {time}")
    
    # Эхо-ответ: просто повторим текст
    await message.answer(f"Вы написали: {user_text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)