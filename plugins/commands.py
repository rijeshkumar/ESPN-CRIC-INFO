import pyrogram 
from pyrogram import filters,Client as YO
from pyrogram.types import ( InlineKeyboardButton,InlineKeyboardMarkup)
from config import Config,Translation
from pyrogram.emoji import *
from plugins.matches import matches


@YO.on_message(filters.command(['start']))
async def start(c,m):
    s = Translation.STARTTEXT.format(m.from_user.mention)
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
    await c.send_message(
        chat_id=m.chat.id,
        text=s,
        reply_to_message_id=m.message_id,
        reply_markup=keyboard
    )

@YO.on_message(filters.command(['help']))
async def help(c,m):
    str = Translation.HELPTEXT
    keyboard= InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(f'{BACK_ARROW} BACK', callback_data="start_data")
            ]   
        ]
    )
    await c.send_message(
        chat_id=m.chat.id,
        text=str,
        reply_to_message_id=m.message_id,
        reply_markup=keyboard
    )

@YO.on_message(filters.command(['about']))
async def about(c,m):
    str = Translation.ABOUTTEXT
    await c.send_message(
        chat_id=m.chat.id,
        text=str,
        reply_to_message_id=m.message_id
    )


@YO.on_message(filters.command(['matches']))
async def match(c,m):
    mCall = await matches(c,m)