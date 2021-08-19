class Config(object):
    URL = "https://www.espncricinfo.com"
    LIVEURL = ""


class Translation(object):
    STARTTEXT = '''
Hello {},\n
I am simple bot to get live cricket scores.'''
    HELPTEXT = '''
**Name: ESPNbot**
This is a web scraping bot, to fetch cricket scores ```from www.espncricinfo.com```
\n
**Available Commands:**
/start - check if bot is alive
/matches - everything the bot is about
/help - Help message'''
    ABOUTTEXT = '''
try /matches instead'''
    NUMS = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
    MATCHES = '''
Matches on the board are:\n
{}'''