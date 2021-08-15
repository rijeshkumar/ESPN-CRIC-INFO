import bs4
import requests
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.emoji import *
from config import Config
async def live_match(c,m,liveLink):
    con = ''
    Config.LIVEURL=liveLink
    liveDetails = requests.get(liveLink)
    liveDetails = bs4.BeautifulSoup(liveDetails.text,"html5lib")
    match_status = liveDetails.select(".match-info.match-info-MATCH .status")
    match_status = match_status[0].string
    match_status = str(match_status).upper()
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
    liveScore = await c.send_message(
        chat_id=m.chat.id,
        text = con,
        reply_markup = keyboard
    )
    print(con)

