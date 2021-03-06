import config 
from time import time

from typing import NamedTuple


__all__ = (
    "Channels",
    "Client",
    "Colours",
    "Emojis",
)

class Channels(NamedTuple):
    LOG_CHANNEL = config.LOG_CHANNEL
    VOICE_CHAT_CHANNEL = config.VOICE_CHAT_CHANNEL


class Client:
    """Client Info."""
    BOT_NAME = "Mr. Devil"
    TOKEN = config.TOKEN
    OWNER_ID = config.OWNER_ID
    PREFIX = config.PREFIX
    UP_TIME = time()

    # Database info.
    DB_HOST = config.DB_HOST
    DB_PORT = config.DB_PORT
    DB_USER = config.DB_USER
    DB_PASSWORD = config.DB_PASSWORD
    DB_NAME = config.DB_NAME



class Colours:
    """Colours code"""
    blue = 0x0279FD
    bright_green = 0x01D277
    dark_green = 0x1F8B4C
    orange = 0xE67E22
    pink = 0xCF84E0
    purple = 0xB734EB
    soft_green = 0x68C290
    soft_orange = 0xF9CB54
    soft_red = 0xCD6D6D
    yellow = 0xF9F586
    python_blue = 0x4B8BBE
    python_yellow = 0xFFD43B
    grass_green = 0x66FF00
    gold = 0xE6C200


class Emojis:
    """Emojis UniCode"""
    cross_mark = "\u274C"
    star = "\u2B50"
    christmas_tree = "\U0001F384"
    check = "\u2611"
    envelope = "\U0001F4E8"
    ok_hand = ":ok_hand:"
    hand_raised = "\U0001F64B"

    number_emojis = {
        1: "\u0031\ufe0f\u20e3",
        2: "\u0032\ufe0f\u20e3",
        3: "\u0033\ufe0f\u20e3",
        4: "\u0034\ufe0f\u20e3",
        5: "\u0035\ufe0f\u20e3",
        6: "\u0036\ufe0f\u20e3",
        7: "\u0037\ufe0f\u20e3",
        8: "\u0038\ufe0f\u20e3",
        9: "\u0039\ufe0f\u20e3"
    }


    dices = {
        1 : "<:dice_1:863427546314178581>",
        2 : "<:dice_2:863427548695363607>",
        3 : "<:dice_3:863427547038220348>",
        4 : "<:dice_4:863427615029198860>",
        5 : "<:dice_5:863427546631897089>",
        6 : "<:dice_6:863427546675019786>"
    }

    confirmation = "\u2705"
    decline = "\u274c"

    x = "\U0001f1fd"
    o = "\U0001f1f4"
    dev = "<:dev:914161575743602699>"
    status_online = "<:online_status:859727593872031794>"
    status_offline = "<:offline_status:859727545157943316>"
    python = "<:python:914507197864624178>"
    bots = "<:bot_tag:859726932752990238>"
    dpy = "<:dpy:914508848012861450>"
    nitro_boost = "<a:nitro_boost:861146239084658709>"


class DB_Scripts:
    bans = """
        CREATE TABLE IF NOT EXISTS `bans` (
            `id` INT NOT NULL AUTO_INCREMENT,
            `user_id` VARCHAR(20) NOT NULL,
            `guild_id` VARCHAR(20) NOT NULL,
            `unban_on` DATETIME NULL,
            PRIMARY KEY (`id`)
        );
        """
