from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

TOKEN = "7991357167:AAGF1v2dtldZsCCG34_XswarPJF-jMmi7xI"

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("درخواست تاکسی 🚖", callback_data='taxi')],
        [InlineKeyboardButton("درخواست حمل بار 📦", callback_data='cargo')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'taxi':
        keyboard = [[KeyboardButton("📍 ارسال لوکیشن", request_location=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        await query.message.reply_text("لطفاً لوکیشن خود را ارسال کنید:", reply_markup=reply_markup)

    elif query.data == 'cargo':
        await query.message.reply_text("لطفاً مشخصات بار خود را ارسال کنید (وزن، نوع بسته‌بندی و...)")

async def location_handler(update: Update, context: CallbackContext) -> None:
    user_location = update.message.location
    await update.message.reply_text(f"✅ لوکیشن دریافت شد!\n🌍 مختصات: {user_location.latitude}, {user_location.longitude}")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.LOCATION, location_handler))

    print("bot is now listening ...")
    app.run_polling()

if __name__ == '__main__':
    main()
