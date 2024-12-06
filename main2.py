from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "TOKEN"
BOT_USERNAME: Final = '@ReMakeMakeup_bot'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! What can I help you with today?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am ReMake Bot! Please type something so I could respond!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

# Response handler
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'face shape' in processed:
        return (
        "Sure! Here are the list of face shapes:\n"
        "oval - Proportional and softly curved edges\n"
        "round - Fullness in cheeks and a circular appearance\n"
        "square - Defined and sharp angles, especially at the jaw\n"
        "heart - Prominent forehead and smaller chin\n"
        "diamond - High cheekbones with a pointed chin\n"
        "oblong - Length is the most noticeable feature\n"
        "triangle - Emphasis on the lower half of the face\n"
        "inverted triangle - Wide upper face and slim jaw"
        )
    elif "oval" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "round" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "square" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "heart" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "diamond" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "oblong" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "triangle" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    elif "inverted triangle" in processed:
        return "Would you like to know some techniques that suit that face shape?"
    else:
        return "I do not understand what you wrote..."


# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Handle message differently for group or private chats
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            if new_text:  # Ensure there's something to process
                response: str = handle_response(new_text)
            else:
                response: str = "Please mention something specific after my username."
        else:
            return  # Ignore group messages without mention
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




















if __name__ == '__main__':
    print('Starting bot!')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=5)
