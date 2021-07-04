import logging
import sys

import traceback

from bot.bot import bot
from bot.constants import Client


log = logging.getLogger(__name__)


# extensions loading
extensions = [
    "bot.exts.backend.logging",
    "bot.commands",
    "bot.exts.moderation.bot_control",
    "bot.exts.info.information"

]

for extension in extensions:
    try:
        bot.load_extension(extension)
        print(extension)
    except Exception as e:
        print(f'Error loading {extension}', file=sys.stderr)
        traceback.print_exc()
        log.error(f"Error Loding {extension}")

else:
    log.info("Loaded all the Extensions")

bot.run(Client.TOKEN)
