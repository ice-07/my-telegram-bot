from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ياهلا وسهلا فيك 🌟")

# رد على أي رسالة
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"أرسلت: {update.message.text}")

def main():
    # حط التوكن الخاص فيك هنا
    BOT_TOKEN = "7761959151:AAFES_hfd02cSY_j3LIGeIrEDEvBGIFBMrA'"

    # إنشاء التطبيق
    application = Application.builder().token(BOT_TOKEN).build()

    # إضافة الأوامر والمستقبلات
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
