import logging
import sys

import traceback

from src.bot import bot
from src.constants import Client


log = logging.getLogger(__name__)


# extensions loading
extensions = [
    "src.exts.backend.logging",
    "src.commands",
    "src.exts.moderation.bot_control",
    "src.exts.info.information"

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
