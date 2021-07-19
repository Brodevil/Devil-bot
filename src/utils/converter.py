

def msg_bool(msg: str):
    if msg in ('yes', 'y', 'true', 't', '1', 'enable', 'on', "True", True):
        return True
    elif msg in ('no', 'n', 'false', 'f', '0', 'disable', 'off', "False", False):
        return False


def acute_remover(msg: str):
    if msg.startswith("```") and msg.endswith("```"):
        return "\n".join(msg.split("\n")[1:-3])
    
    elif msg.startswith("`") and msg.endswith("`"):
        return msg[1:-1]
    
    return msg
    