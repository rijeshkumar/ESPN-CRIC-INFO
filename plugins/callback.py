import requests
import bs4
from pyrogram import Client as YO
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import Config,Translation
from pyrogram.emoji import *
from config import Config

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

    elif query.data == 'live_refresh':
        await query.answer()
        con = ''
        liveDetails = requests.get(Config.LIVEURL)
        liveDetails = bs4.BeautifulSoup(liveDetails.text,"html5lib")
        match_status = liveDetails.select(".match-info.match-info-MATCH .status")
        match_status = match_status[0].string
        match_status = (match_status).upper()
        desc = liveDetails.select(".match-info.match-info-MATCH .description")
        teamName = liveDetails.select(".match-info.match-info-MATCH .teams .team .name-detail .name")
        score_detail = liveDetails.select(".match-info.match-info-MATCH .teams .team .score-detail .score")
        score_info = liveDetails.select(".match-info.match-info-MATCH .teams .team .score-detail .score-info")
        status_text = liveDetails.select(".match-info.match-info-MATCH .status-text")
        #print(scoreinfo[1].text)
        con = f'''
**{match_status}**
__{desc[0].text}__
-+-+-+-+-+-+-+-+-+-+-+-+-+
{teamName[0].text} Vs. {teamName[1].text}
{score_detail[0].text} :: {score_detail[1].text}
{score_info[0].text}
{status_text[0].text} '''
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(f'{REPEAT_BUTTON} REFRESH',callback_data='live_refresh' )
                ]
            ]
        )
        liveScore = await query.message.edit_text(
            text = con,
            reply_markup = keyboard,
            disable_web_page_preview = True
        )
        print(con)

