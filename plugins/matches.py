import bs4
import requests
from bot import app
from .tools.live import live_match
from config import Config, Translation
from pyrogram.emoji import *
from pyrogram.types import (ForceReply, InlineKeyboardButton,InlineKeyboardMarkup)
espn = requests.get(Config.URL)
espn = bs4.BeautifulSoup(espn.text, "html5lib")
status = espn.select(".match-info.match-info-HSB.card.scorecard .status")
teams = espn.select(".match-info.match-info-HSB.card.scorecard .teams .team .name-detail .name")


async def matches(c, m):
    response = await c.send_message(
    chat_id=m.chat.id,
    text="Fetching Match Detailss: ",
    reply_to_message_id=m.message_id
    )
    statusLive = espn.select(".match-info.match-info-HSB.card.scorecard .status.red")
    print(len(statusLive))
    description = espn.select(".match-info.match-info-HSB.card.scorecard .status-text")
    print(len(teams))
    print(len(description))
    ko = len(description)
    k = 0
    j = 0
    ms=''
    for i in range(ko):
        ms += f"\n\n{Translation.NUMS[i]}  **{status[i].text}**\n{teams[k].text}  Vs. {teams[k+1].text}\n{description[i].text}"
        k += 2

    response = await response.edit_text(Translation.MATCHES.format(ms))
    matchChoice = await c.ask(
        text = "Send match number 🔢 to get details",
        chat_id = m.chat.id,
        reply_markup=ForceReply(True)
    )

    ch = int(matchChoice.text)
    liveLink = status[ch].parent
    liveLink = Config.URL+liveLink.get("href")
    result = await live_match(c,m,liveLink)
