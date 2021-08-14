import ast
import os
from pyrogram import Client as YO
from pyrogram.methods.chats.iter_chat_members import QUERIES
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import Config,Translation
from pyrogram.emoji import *

@YO.on_callback_query()
async def cb_handler(client,query):
    if query.data == "start_data":
        await query.answer()
        s = Translation.STARTTEXT.format(query.from_user.mention)
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('OWNER 👨‍💻', url='https://t.me/{}'.format(Config.OWNER_USERNAME)),
                    InlineKeyboardButton('HELP', callback_data="help_data" )
                ],
                [
                    InlineKeyboardButton('ABOUT', callback_data="about_data" ),
                    InlineKeyboardButton(f'CLOSE {CROSS_MARK}',callback_data="close_data" )
                ]
            ]
        )
        await query.message.edit_text(
            text=s,
            reply_markup = keyboard,
            disable_web_page_preview=True
        )
        return
    elif query.data == "help_data":
        await query.answer()
        str=Translation.HELPTEXT
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f'{BACK_ARROW} BACK', callback_data="start_data")
                ]
            ]
        )
        await query.message.edit_text(
            str,
            reply_markup = keyboard,
            disable_web_page_preview = True
        )
        return
    elif query.data == "close_data":
        await query.message.delete()
    elif query.data == "about_data":
        await query.answer()
        str = Translation.ABOUTTEXT
        await query.message.edit_text(
            text=str,
            disable_web_page_preview=True
        )
