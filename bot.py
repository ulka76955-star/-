import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video

    if not video:
        return

    file = await context.bot.get_file(video.file_id)

    input_file = "input.mp4"
    output_file = "output.mp4"

    await file.download_to_drive(input_file)

    subprocess.run([
        "ffmpeg",
        "-i",
        input_file,
        "-vf",
        "crop=min(iw\\,ih):min(iw\\,ih),scale=1080:1080",
        "-y",
        output_file
    ])

    await update.message.reply_video(video=open(output_file, "rb"))

    os.remove(input_file)
    os.remove(output_file)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.VIDEO, handle_video))

app.run_polling()
