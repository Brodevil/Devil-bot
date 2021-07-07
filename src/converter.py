import re


def msg_bool(msg: str):
    if msg in ('yes', 'y', 'true', 't', '1', 'enable', 'on'):
        return True
    elif msg in ('no', 'n', 'false', 'f', '0', 'disable', 'off'):
        return False


def acute_remover(msg: str):
    msg = msg.replace("```py\n", "").replace("```", "")
    msg = msg.replace("`", "").replace("`", "")
    