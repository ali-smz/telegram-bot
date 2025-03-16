from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = "7991357167:AAGF1v2dtldZsCCG34_XswarPJF-jMmi7xI"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your Telegram bot.')

# Help command handler
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Here are the commands you can use: /start, /help')

# Main function to start the bot
def main() -> None:
    # Create an Application instance
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    # Start polling for updates
    application.run_polling()
    print('running')

if __name__ == '__main__':
    main()