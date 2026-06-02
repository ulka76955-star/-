import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Бот работает ✅")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.VIDEO, handle_video))

app.run_polling()
