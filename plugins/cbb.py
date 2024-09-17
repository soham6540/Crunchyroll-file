from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging

logging.basicConfig(level=logging.INFO)

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    try:
        if data == "about":
            await query.message.edit_text(
                text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @crunchyroll_hindi_animes_india_a\n○ Support Group : @team_jjk</b>",
                disable_web_page_preview = True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔒 Close", callback_data = "close")
                        ]
                    ]
                )
            )
        elif data == "close":
            await query.message.delete()
            try:
                await query.message.reply_to_message.delete()
            except Exception as e:
                logging.error(f"Failed to delete reply-to message: {e}")
    except Exception as e:
        logging.error(f"Error handling callback query: {e}")
