from aiogram import Bot, Dispatcher

from src.config import settings


dp = Dispatcher()


async def main_loop() -> None:
    bot = Bot(settings.TG_BOT_TOKEN)
    await dp.start_polling(bot)
