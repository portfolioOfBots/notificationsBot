import config
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.client.bot import DefaultBotProperties

TOKEN = config.BOT_TOKEN
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}")


@dp.message(F.text == 'услугу')
@dp.message(F.text == 'услуга')
async def notif(message: Message):
    await message.answer('Предлагаю вам посмотреть мой Репозиторий:\nhttps://github.com/portfolioOfBots/notificationsBot')

async def main() -> None:
    bot = Bot(token=str(TOKEN), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())