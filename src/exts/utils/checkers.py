import discord

__all__ = ("random_num_check")


def random_num_check(author: discord.User):
    def inner_check(message):
        if message.author != author:
            return False
        try:
            int(message.content)
            return True
        except ValueError:
            return False

    return inner_check
