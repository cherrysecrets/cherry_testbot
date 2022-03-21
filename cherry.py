#!/usr/bin/env python3

from logging import basicConfig, getLogger, INFO
from flask import Flask, request, jsonify
from html import escape
from requests import get, post
from os import environ
import config

from telegram.ext import CommandHandler, Updater

server = Flask(__name__)

basicConfig(level=INFO)
log = getLogger()

ENV = bool(environ.get('ENV', False))

if ENV:
    BOT_TOKEN = environ.get('BOT_TOKEN', None)
    PROJECT_NAME = environ.get('PROJECT_NAME', None)
    ip_addr = environ.get('APP_URL', None)
    # You kanged our project without forking it, we'll get you DMCA'd.
    GIT_REPO_URL = environ.get('GIT_REPO_URL', "https://github.com/pokurt/GitGram")
else:
    BOT_TOKEN = config.BOT_TOKEN
    PROJECT_NAME = config.PROJECT_NAME
    ip_addr = get('https://api.ipify.org').text
    GIT_REPO_URL = config.GIT_REPO_URL

updater = Updater(token=BOT_TOKEN, workers=1)
dispatcher = updater.dispatcher

print("If you need more help, join @GitGramChat in Telegram.")


def start(_bot, update):
    """/start message for bot"""
    message = update.effective_message
    message.reply_text(
        f"This is the Updates watcher for {PROJECT_NAME}. I am just notify users about what's happen on their Git repositories thru webhooks.\n\nYou need to [self-host](https://waa.ai/GitGram) or see /help to use this bot on your groups.",
        parse_mode="markdown")


def help(_bot, update):
    """/help message for the bot"""
    message = update.effective_message
    message.reply_text(
        f"*Available Commands*\n\n`/connect` - Setup how to connect this chat to receive Git activity notifications.\n`/support` - Get links to get support if you're stuck.\n`/source` - Get the Git repository URL.",
        parse_mode="markdown"
    )


def support(_bot, update):
    """Links to Support"""
    message = update.effective_message
    message.reply_text(
        f"*Getting Support*\n\nTo get support in using the bot, join [the GitGram support](https://t.me/GitGramChat).",
        parse_mode="markdown"
    )


def source(_bot, update):
    """Link to Source"""
    message = update.effective_message
    message.reply_text(
        f"*Source*:\n[GitGram Repo](https://waa.ai/GitGram).",
        parse_mode="markdown"
    )


def getSourceCodeLink(_bot, update):
    """Pulls link to the source code."""
    message = update.effective_message
    message.reply_text(
        f"{GIT_REPO_URL}"
    )




    
    
        

           
    
