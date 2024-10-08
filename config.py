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
DB_NAME = os.environ.get("DATABASE_NAME", "sharexbotjjkverse")

# Number of workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Force subscribe channel
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "-1002109545727")  # Add your channel ID here

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}...")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}...")

try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split() if x.isdigit()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Other settings
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

