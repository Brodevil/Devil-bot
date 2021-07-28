import discord 


__all__ = ("ActionCancel", )



class ActionCancle(discord.HTTPException):
    """Raise when the Action is Canceled"""
    pass
