"""
Global error handler for Discord bot events.

This module handles uncaught errors that occur during bot operation,
logging them to both Sentry and the database for tracking and debugging.
"""

import datetime
import logging

import discord
import pytz
from discord.ext import commands
from sentry_sdk import capture_exception, push_scope

from utils.utils import error_gen


class OnError(commands.Cog):
    """Handles global error events and logs them appropriately."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_error")
    async def on_error(self, error):
        """
        Handle uncaught errors during bot operation.
        
        Filters out common expected errors and logs serious errors
        to both Sentry and the database with a unique error ID.
        
        Args:
            error: The exception that was raised
        """
        bot = self.bot
        error_id = error_gen()

        if isinstance(error, discord.Forbidden):
            if "Cannot send messages to this user" in str(error):
                return

        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, commands.CheckFailure):
            return
        if isinstance(error, commands.MissingRequiredArgument):
            return
        # # print(error)
        # # print(str(error))
        with push_scope() as scope:
            scope.set_tag("error_id", error_id)
            scope.level = "error"
            await bot.errors.insert(
                {
                    "_id": error_id,
                    "error": str(error),
                    "time": datetime.datetime.now(tz=pytz.UTC).strftime(
                        "%m/%d/%Y, %H:%M:%S"
                    ),
                }
            )

            capture_exception(error)


async def setup(bot):
    await bot.add_cog(OnError(bot))
