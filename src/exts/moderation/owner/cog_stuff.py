from typing import Optional

from logging import getLogger
from json import load

from discord.ext.commands import Bot, Cog
from discord.ext import commands

from discord import Embed
from src.constants import Colours


log = getLogger(__name__)
__all__ = ("Cogs_work", "setup")


class Cogs_work(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(name="load", aliases=["load_cog", "cogload", "load_extension"])
    async def load_cog(self, ctx: commands.Context, cog: str):
        cog = cog.split(", ")
        for _ in cog:
            try:
                self.bot.load_extension(_)
                msg = f"Loaded {_}"
                log.info(msg)
                await ctx.reply(msg)
            except KeyError:
                await ctx.reply("**No such Extension path found**")

    @commands.is_owner()
    @commands.command(name="reload", aliases=("reload_cog", "recog", ))
    async def reload_cogs(self, ctx: commands.Context, cog: Optional[str] = None):
        """Reloads the cogs """

        await ctx.confirm_action()

        with open("src/resource/_cogs.json") as cogs:
            cogs = load(cogs)
            cogs = list(cogs["cogs"])
            cogs.remove("src.exts.backend.logging")

        if cog is None:
            for _ in cogs:
                self.bot.reload_extension(_)
                log.info("Reloaded {0}".format(_))
            await ctx.reply("**Reloaded All the Cogs!**")

        elif cog in " ".join(cogs):
            for _ in cogs:
                if cog in _:
                    self.bot.reload_extension(_)
                    await ctx.reply(f"**Sucessfully Reloaded `{_}` Cog!**")
                    log.info(f"Sucessfully Reloaded `{cog}` Cog File!")
                    break


    @commands.is_owner()
    @commands.command(name="unload", aliases=("unload_cog", "uncog", "unload_cogs", "unload_all", "unload_all_cogs"))
    async def unload_cogs(self, ctx: commands.Context, cog: Optional[str] = None):
        """Unloads the cogs """
        await ctx.confirm_action()
        with open("src/resource/_cogs.json") as cogs:
            cogs = load(cogs)
            cogs = list(cogs["cogs"])

        if cog is None:
            for _ in cogs:
                self.bot.unload_extension(_)
                log.info(f"Unloaded {_}")

            await ctx.reply("**Unloaded All the Cogs!**")
            log.critical("Unloaded All the Cogs!")
            return

        for _ in cogs:
            if cog in _:
                self.bot.unload_extension(_)
                msg = "Unloaded {0}".format(_)
                log.info(msg)
                await ctx.reply(msg)
                break
        else:
            await ctx.reply("**No Such Cog found!**")


    @commands.is_owner()
    @commands.command(name="cogs", aliases=("total_cogs", "show_cogs", "cog"))
    async def cogs(self, ctx: commands.Context):
        """Show case the Total Cogs"""
        with open("src/resource/_cogs.json") as cogs:
            cogs = load(cogs)
            cogs = list(cogs["cogs"])

        not_loaded = "\n".join([_ for _ in self.bot.total_cogs if _ not in self.bot.cogs])
        description = "**Loaded Cogs :**\n```" + "\n".join(self.bot.cogs) + "```"
        if len(not_loaded) != 0:
            description += "\n**Not Loaded Cogs :**\n```{0}```".format(not_loaded)

        embed = Embed(description=description, color=Colours.soft_red)

        await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Cogs_work(bot))
