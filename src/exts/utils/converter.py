from discord.ext import commands
from discord.ext.commands import Context


__all__ = ("BoolConverter", "acute_remover")


class BoolConverter(commands.Converter):
    async def convert(self, ctx: Context, argument):
        lookup = {
                  True:  ('yes', 'y', 'true', 't', '1', 'enable', 'on'),
                  False: ('no', 'n', 'false', 'f', '0', 'disable', 'off')
                 }
        lower = argument.lower()
        for mode, storage in lookup.items():
            if lower in storage:
                return mode


def acute_remover(msg: str):
    if msg.startswith("```") and msg.endswith("```"):
        return "\n".join(msg.split("\n")[1:-3])
    
    elif msg.startswith("`") and msg.endswith("`"):
        return msg[1:-1]
    
    return msg

