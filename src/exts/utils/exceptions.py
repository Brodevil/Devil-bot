import discord 
import asyncio

__all__ = ("ActionCancel", )


class ActionCancle(Exception):
    """Raise when the Action is Canceled"""
    pass
