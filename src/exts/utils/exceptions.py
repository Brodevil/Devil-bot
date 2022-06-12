# Exceptions :

__all__ = ("ActionCancelled", "UnableToReach")


class ActionCancelled(Exception):
    """Raise when the Action is Canceled"""
    pass

class UnableToReach(Exception):
    """Raise when bot unable to reach any api"""
    pass

class VoiceError(Exception):
    pass

class YTDLError(Exception):
    pass
