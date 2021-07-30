import discord 
import asyncio

__all__ = ("ActionCancle")


class ActionCancle(Exception):
    """Raise when the Action is Canceled"""
    pass
