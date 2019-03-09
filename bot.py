#!/usr/bin/env python3.5.3
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
from common import constants
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(constants.TOKEN)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()