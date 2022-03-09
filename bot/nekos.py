# MIT License

# Copyright (c) 2020 Anil Chauhan // This file is part of ZeroTsu

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import requests
import logging
import nekos
import os, threading, math
import re
from telegram.ext.dispatcher import run_async
from telegram import Update
from typing import Callable, List
import random

from telegram.ext import (CallbackContext,
                          run_async, Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler)

from telegram import (ParseMode, Update, InlineKeyboardMarkup, 
                      InlineKeyboardButton, ReplyKeyboardMarkup, 
                      KeyboardButton)

from bot.String import String

delete_button = 'Hapus'

@nekos.on_callback_query(filters.regex(r"^neko anime"))
def neko(update: Update, context: CallbackContext, callback: CallbackQuery) -> None:
    msg = update.effective_message
    chat_id = update.message.from_user.id
    target = "neko"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"),InlineKeyboardButton(text="Change", callback_data=f"neko anime"),]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))
   

def feet(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "feet"
    link = nekos.img(target)    
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def yuri(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "yuri"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def trap(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "trap"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def futanari(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "futanari"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def hololewd(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "hololewd"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def lewdkemo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "lewdkemo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def sologif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "solog"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def feetgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "feetg"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def cumgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "cum"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def erokemo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "erokemo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def lesbian(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "les"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def wallpaper(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "wallpaper"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Kirim Berkas", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def lewdk(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "lewdk"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def ngif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "ngif"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def tickle(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "tickle"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def lewd(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "lewd"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def feed(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "feed"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def eroyuri(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "eroyuri"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def eron(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "eron"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def cum(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "cum_jpg"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def bjgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "bj"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def bj(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "blowjob"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def nekonsfw(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "nsfw_neko_gif"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def solo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "solo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def kemonomimi(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "kemonomimi"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def avatarlewd(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "nsfw_avatar"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def gasm(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "gasm"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def poke(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "poke"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def anal(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "anal"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def hentai(update: Update, context: CallbackContext) -> None:
    tag = random.choice([
        "feet", "yuri", "trap", "futanari", "hololewd", "lewdkemo", "solog", "feetg", "cum", "erokemo", "les",
        "lewdk", "ngif", "lewd", "eroyuri", "eron", "cum_jpg", "bj", "nsfw_neko_gif", "solo",
        "nsfw_avatar", "gasm", "anal", "slap", "hentai", "avatar", "erofeet", "keta", "blowjob",
        "pussy", "tits", "holoero", "pussy_jpg", "pwankg", "classic", "kuni", "waifu", "8ball",
        "femdom", "spank", "erok", "boobs", "random_hentai_gif", "smallboobs", "ero", "lesbian", "pussyWankGif"
    ])
    msg = update.effective_message
    target = "hentai"
    link = nekos.img(tag)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Kirim Berkas", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def avatar(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "avatar"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def erofeet(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "erofeet"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def holo(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "holo"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


# def keta(update: Update, context: CallbackContext) -> None:
#     msg = update.effective_message
#     target = 'keta'
#     if not target:
#         msg.reply_text("No URL was received from the API!")
#         return
#     msg.reply_photo(nekos.img(target))



def pussygif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "pussy"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def tits(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "tits"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def holoero(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "holoero"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def pussy(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "pussy_jpg"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def hentaigif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "random_hentai_gif"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def classic(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "classic"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def kuni(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "kuni"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))





def kiss(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "kiss"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def femdom(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "femdom"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def cuddle(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "cuddle"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def erok(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "erok"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def foxgirl(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "fox_girl"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))


def titsgif(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "boobs"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))


def ero(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "ero"
    link = nekos.img(target)
    link = link[23:],
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, neko"),InlineKeyboardButton(text=f"Direct link",url=f"https://cdn.nekos.life/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}")]]
    msg.reply_photo(f"https://cdn.nekos.life/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))



def smug(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "smug"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))



def baka(update: Update, context: CallbackContext) -> None:
    msg = update.effective_message
    target = "baka"
    link = nekos.img(target)
    keyboard = [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {msg.from_user.id}"), InlineKeyboardButton(text=f"Direct link",url=link)]]
    msg.reply_video(link,reply_markup=InlineKeyboardMarkup(keyboard))
    

def dva(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    link = nsfw.get("url") 
    link = link[31:],
    if not link:
        message.reply_text("No URL was received from the API!")
        return
    keyboard = [[InlineKeyboardButton(text="Send as file", callback_data=f"neko_callback, {link}, hexa"),InlineKeyboardButton(text=f"Direct link",url=f"https://dva.computerfreaker.cf/{link[0]}")]]
    keyboard += [[InlineKeyboardButton(text=delete_button, callback_data=f"neko_delete, {message.from_user.id}")]]
    message.reply_photo(f"https://dva.computerfreaker.cf/{link[0]}",reply_markup=InlineKeyboardMarkup(keyboard))

# buat random waifu

def get_url():
    contents = requests.get('https://arugaz.herokuapp.com/api/nekonime').json()
    url = contents['result']
    return url
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def waifu(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

# Buat random image di folder source

def send_photo(src: str, message=None):
    """Generates a function for sending a photo with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(f"./media/{src}", "rb"),
        )
    return send


def send_video(src: str, message=None):
    """Generates a function for sending a video with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=open(f"./media/{src}", "rb"),
            supports_streaming=True
        )
    return send


def choose_photo(folder: str, message=None, caption=None):
    """Generates a function for sending a photo with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        filename = random.choice(os.listdir(f"./media/{folder}"))
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(f"./media/{folder}/{filename}", "rb"),
            caption=caption
        )
    return send


def choose_video(folder: str, message=None, caption=None):
    """Generates a function for sending a video with an optional message"""
    def send(update: Update, context: CallbackContext):
        if message != None:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                message=message
            )
        filename = random.choice(os.listdir(f"./media/{folder}"))
        context.bot.send_video(
            chat_id=update.effective_chat.id,
            video=open(f"./media/{folder}/{filename}", "rb"),
            supports_streaming=True,
            caption=caption
        )
    return send

def pp(update, context):
    file = random.choice(os.listdir("media/pic"))

    if "png" in file:
        context.bot.send_photo(
            chat_id=update.effective_chat.id, photo=open("./media/pic/"+file, "rb"))
    else:
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(
            "./media/pic/"+file, "rb"), supports_streaming=True)

# image donwload            
# Configuration Start
OID = 1005051233281285
COOKIES = "SUB=_2AkMhFc9hf8NhqwJRmPoRym_jaI9_ygvEiebDAHzsJxJjHlE47Gaj8oPkdVHDdzd9ToAkUSPIsxRx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWM2vn1KHS_k1aSj6DvSDWv; SINAGLOBAL=7552724259118.417.1447641174437; ULV=1447691774405:2:2:2:6434341784127.688.1447691774390:1447641174455; YF-Page-G0=7f5e11c19f51c6954c5e18e40c0b1444; _s_tentry=-; Apache=6434341784127.688.1447691774390; USRANIME=usrmdinst_29"; # Your cookies.
CRAWL_PHOTOS_NUMBER = 186
# Configuration END

COOKIES = dict((l.split('=') for l in COOKIES.split('; ')))
#先创建保存图片的目录
SAVE_PATH="image"+str(OID) + "./media/pic/"
if not os.path.exists(SAVE_PATH):
	os.makedirs(SAVE_PATH)
TEMP_LastMid = ""

def save_image(image_name):
	#if not os.path.isfile(SAVE_PATH + image_name):
	sina_image_url = 'http://ww1.sinaimg.cn/large/' + image_name
	response = requests.get(sina_image_url, stream=True)
	image = response.content
	try:
		print(image_name)
		with open(SAVE_PATH+image_name,"wb") as image_object:
			image_object.write(image)
			return
	except IOError:
		print("IO Error\n")
		return
	finally:
		image_object.close



def get_album_photos_url(page):
	global TEMP_LastMid
	data={
		'ajwvr':6,
		'filter':'wbphoto|||v6',
		'page': page,
		'count':20,
		'module_id':'profile_photo',
		'oid':OID,
		'uid':'',
		'lastMid':TEMP_LastMid,
		'lang':'zh-cn',
		'_t':1,
		'callback':'STK_' + str(random.randint(10000000000000, 900000000000000))
	}
	#print(data)
	#print(COOKIES)
	album_request_result = requests.get('http://photo.weibo.com/page/waterfall',  params = data, cookies = COOKIES).text
	#print(album_request.headers)
	TEMP_LastMid = re.compile(r'"lastMid":"(\d+)"').findall(album_request_result)
	print(TEMP_LastMid)
	return (re.compile(r'(\w+.png|\w+.gif|\w+.jpg)').findall(album_request_result))

if __name__ == '__main__':
	for i in range(1, int(math.ceil(CRAWL_PHOTOS_NUMBER / 20.0))):
		threads = []
		for image_name in get_album_photos_url(i):
			#save_image(image_name);
			threads.append(threading.Thread(target=save_image, args=(image_name,)))
		for t in threads:
			#t.setDaemon(True)
			t.start()