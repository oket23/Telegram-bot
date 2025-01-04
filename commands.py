from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commads(bot: Bot):
    commands = [
        BotCommand(command="start", description="Початок роботи / start bot"),
        BotCommand(command="stop", description="Закінчити / stop bot"),
        BotCommand(command="ip", description="???")
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
