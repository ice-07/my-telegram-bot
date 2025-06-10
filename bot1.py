from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توكن البوت الخاص بك
TOKEN = "7761959151:AAFES_hfdO2cSY_j3LIGeIrEDEvBGIFBMrA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا")

def main():
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()
    
    # إضافة handler للأمر /start
    application.add_handler(CommandHandler("start", start))
    
    # تشغيل البوت
    print("البوت يعمل...")
    application.run_polling()

if __name__ == "__main__":
    main()
