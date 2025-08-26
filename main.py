from flask import Flask
import threading
import time
from telegram.ext import Updater, CommandHandler

TOKEN = "7473686932:AAEmpKvL4rJyC2aEzyJ3be65eCF2FFdwc6A"

# ----------------------
# 1) بوت تيليغرام
# ----------------------
def start(update, context):
    update.message.reply_text("✅ البوت شغال 24/7 على Render!")

def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

# ----------------------
# 2) سيرفر ويب صغير
# ----------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running on Render!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

# ----------------------
# 3) تشغيل الاثنين
# ----------------------
threading.Thread(target=run_web).start()
run_bot()
