import telegram
from telegram.ext import Updater, MessageHandler, Filters
import tokenkey

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the chat ID and the user ID of the sender
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    # Send an image to the user who sent the most recent message
    photo = open('send.jpg', 'rb')
    bot = context.bot
    bot.send_photo(chat_id=user_id, photo=photo)


if __name__ == "__main__":
    # Create an Updater object and attach a MessageHandler to it
    updater = Updater(token=tokenkey.BotToken, use_context=True)
    dispatcher = updater.dispatcher
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()
