

def msg_bool(msg):
    if msg in ('yes', 'y', 'true', 't', '1', 'enable', 'on'):
        return True
    elif msg in ('no', 'n', 'false', 'f', '0', 'disable', 'off'):
        return False
