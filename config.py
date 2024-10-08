


# (©)CodeXBotz

import os
import logging
from logging.handlers import RotatingFileHandler

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7291162561:AAFFB1Sn2dHW-JO27MEigL8rbRCrtsymcxc")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20733274"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a74c1ddba4508413caf9bf608ac8d9e1")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002302038082"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6574393060"))

# Port
PORT = os.environ.get("PORT", "8080")

# Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://vikas:vikas@vikas.yfezexk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "exbot")

# Number of workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# User reply text
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"

# Other settings...
