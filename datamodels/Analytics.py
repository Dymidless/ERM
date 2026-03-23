"""
Analytics data model.

This module provides the data model for storing and retrieving
bot usage analytics and statistics.
"""

from discord.ext import commands
import discord
from utils.mongo import Document


class Analytics(Document):
    """
    Data model for bot analytics.
    
    Stores usage statistics, command execution data, and other
    metrics for monitoring bot performance and usage patterns.
    """
    pass
