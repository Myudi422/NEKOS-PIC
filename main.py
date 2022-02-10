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

import yaml
from telegram import BotCommand
from telegram.ext import Updater 
import logging
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler
)
from bot.start import pic
from bot.help import help1, chelp1
from bot.nekos import *
from bot.nekos_fun import asfile

# load config
try:
    CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
except FileNotFoundError:
    print("Read README.md file again. you missed something.")
    quit(1)
except Exception as eee:
    print(
        f"Ah, look like there's error(s) while trying to load your config. It is\n!!!! ERROR BELOW !!!!\n {eee} \n !!! ERROR END !!!"
    )
    quit(1)
 

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

        
updater = Updater(CONFIG['bot_token'], use_context=True)

updater.dispatcher.add_handler(CommandHandler('pic', pic))
updater.dispatcher.add_handler(CommandHandler('help1', chelp1))
updater.dispatcher.add_handler(CallbackQueryHandler(help1, pattern='zero_.*'))
updater.dispatcher.add_handler(CallbackQueryHandler(asfile, pattern='neko_.*'))

updater.dispatcher.add_handler(CommandHandler("lewdkemo", lewdkemo))
updater.dispatcher.add_handler(CommandHandler("neko", neko))
updater.dispatcher.add_handler(CommandHandler("feet", feet))
updater.dispatcher.add_handler(CommandHandler("yuri", yuri))
updater.dispatcher.add_handler(CommandHandler("trap", trap))
updater.dispatcher.add_handler(CommandHandler("futanari", futanari))
updater.dispatcher.add_handler(CommandHandler("hololewd", hololewd))
updater.dispatcher.add_handler(CommandHandler("sologif", sologif))
updater.dispatcher.add_handler(CommandHandler("cumgif", cumgif))
updater.dispatcher.add_handler(CommandHandler("erokemo", erokemo))
updater.dispatcher.add_handler(CommandHandler("lesbian", lesbian))
updater.dispatcher.add_handler(CommandHandler("wallpaper", wallpaper))
updater.dispatcher.add_handler(CommandHandler("lewdk", lewdk))
updater.dispatcher.add_handler(CommandHandler("ngif", ngif))
updater.dispatcher.add_handler(CommandHandler("tickle", tickle))
updater.dispatcher.add_handler(CommandHandler("lewd", lewd))
updater.dispatcher.add_handler(CommandHandler("feed", feed))
updater.dispatcher.add_handler(CommandHandler("eroyuri", eroyuri))
updater.dispatcher.add_handler(CommandHandler("eron", eron))
updater.dispatcher.add_handler(CommandHandler("cum", cum))
updater.dispatcher.add_handler(CommandHandler("bjgif", bjgif))
updater.dispatcher.add_handler(CommandHandler("bj", bj))
updater.dispatcher.add_handler(CommandHandler("nekonsfw", nekonsfw))
updater.dispatcher.add_handler(CommandHandler("solo", solo))
updater.dispatcher.add_handler(CommandHandler("kemonomimi", kemonomimi))
updater.dispatcher.add_handler(CommandHandler("avatarlewd", avatarlewd))
updater.dispatcher.add_handler(CommandHandler("gasm", gasm))
updater.dispatcher.add_handler(CommandHandler("poke", poke))
updater.dispatcher.add_handler(CommandHandler("anal", anal))
updater.dispatcher.add_handler(CommandHandler("hentai", hentai))
updater.dispatcher.add_handler(CommandHandler("avatar", avatar))
updater.dispatcher.add_handler(CommandHandler("erofeet", erofeet))
updater.dispatcher.add_handler(CommandHandler("holo", holo))
updater.dispatcher.add_handler(CommandHandler("tits", tits))
updater.dispatcher.add_handler(CommandHandler("pussygif", pussygif))
updater.dispatcher.add_handler(CommandHandler("holoero", holoero))
updater.dispatcher.add_handler(CommandHandler("pussy", pussy))
updater.dispatcher.add_handler(CommandHandler("hentaigif", hentaigif))
updater.dispatcher.add_handler(CommandHandler("classic", classic))
updater.dispatcher.add_handler(CommandHandler("kuni", kuni))
updater.dispatcher.add_handler(CommandHandler("waifu", waifu))
updater.dispatcher.add_handler(CommandHandler("lewd", lewd))
updater.dispatcher.add_handler(CommandHandler("kiss", kiss))
updater.dispatcher.add_handler(CommandHandler("femdom",femdom))
updater.dispatcher.add_handler(CommandHandler("cuddle", cuddle))
updater.dispatcher.add_handler(CommandHandler("erok", erok))
updater.dispatcher.add_handler(CommandHandler("foxgirl", foxgirl))
updater.dispatcher.add_handler(CommandHandler('titsgif', titsgif))
updater.dispatcher.add_handler(CommandHandler('ero', ero))
updater.dispatcher.add_handler(CommandHandler('smug', smug))
updater.dispatcher.add_handler(CommandHandler('baka', baka))
updater.dispatcher.add_handler(CommandHandler('dva', dva))


updater.start_polling()
updater.idle()
