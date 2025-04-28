import logging
from aiogram import Bot, Dispatcher, executor, types
from calendar_api import create_event
from nlp_parser import extract_task_info
from config import TELEGRAM_BOT_TOKEN
import datetime

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("👋 Привет! Отправь мне текст задачи, и я создам её в твоём календаре.\nПример: 'Позвонить Васе завтра в 14:00' 📅")

@dp.message_handler()
async def handle_task(message: types.Message):
    text = message.text
    task_text, task_datetime = extract_task_info(text)

    if not task_datetime:
        await message.reply("❌ Я не смог найти дату/время в сообщении. Попробуй уточнить.")
        return

    event_link = create_event(task_text, task_datetime)
    await message.reply(f"✅ Задача **{task_text}** создана на {task_datetime.strftime('%d.%m.%Y %H:%M')}!\n\n[Открыть в календаре]({event_link})", parse_mode="Markdown")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)