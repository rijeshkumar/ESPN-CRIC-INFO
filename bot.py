import pyrogram
from pyromod import listen
from pyrogram import Client


from config import Config, Translation

app = Client (
    session_name='ESPN',
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TG_BOT_TOKEN,
    plugins=dict(root="plugins")
    )

if __name__ == "__main__":
	app.run()
