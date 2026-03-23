"""
Error tracking data model.

This module provides the data model for storing and retrieving
error logs from the database.
"""

from discord.ext import commands
import discord
from utils.mongo import Document


class Errors(Document):
    """
    Data model for error logs.
    
    Stores error information including error messages, timestamps,
    and unique error IDs for tracking and debugging purposes.
    """
    pass
