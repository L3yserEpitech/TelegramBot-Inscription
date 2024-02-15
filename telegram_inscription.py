import telebot
from telebot import types
from telebot.util import quick_markup
import sys
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

api_key = "6600000609:AAG9M4oEnkTWSHrfVlqlRFi20TWas7q2sfc"
bot = telebot.TeleBot(api_key)


#gestion d'évenement
@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    chat_id = call.message.chat.id
    username = call.from_user.username
    data = call.data
    user_id = call.from_user.id
    
    if data == 'start':
        handle_start(chat_id)
        
    elif data == 'language=french':
        fr_bienvenue(chat_id, username)
    elif data == 'language=english':
        pass
    
    elif data == 'inscription':
        fr_user_inscription(chat_id)
        
    elif data == 'minor':
        fr_user_minor(chat_id)
    elif data == 'major':
        fr_user_country(chat_id)
        
    elif data == 'fr':
        fr_user_pack(chat_id)
    elif data == 'eu':
        fr_user_pack(chat_id)
    
    
        
        
        
        

#message de /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    
    markup = InlineKeyboardMarkup(row_width=2)
    bt_french = InlineKeyboardButton('  🇫🇷  ', callback_data='language=french')
    bt_english = InlineKeyboardButton('  🇬🇧  ', callback_data='language=english')
    
    markup.add(bt_french, bt_english)
    
    bot.send_message(chat_id, f"🌍 Choisis ta langue / Choose your language :", reply_markup=markup, parse_mode="Markdown")

#message de bienvenue
def fr_bienvenue(chat_id, username):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_inscription = InlineKeyboardButton('Inscription', callback_data='inscription')
    bt_info = InlineKeyboardButton('Site internet', url="https://www.auroratrading.fr")
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")

    markup.add(bt_inscription, bt_info, bt_support)
    
    bot.send_message(chat_id, f"*Bonjour* {username}*, nous te souhaitons la bienvenue dans l'équipe Aurora ! 💎 \
    \n\nComment pouvons-nous t'aider ❓*", reply_markup=markup, parse_mode="Markdown")

#lancement processus d'inscription
def fr_user_inscription(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_major = InlineKeyboardButton('+18ans', callback_data='major')
    bt_minor = InlineKeyboardButton('-18ans', callback_data='minor')
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")

    markup.add(bt_major, bt_minor, bt_support)
    
    bot.send_message(chat_id, f"*Bienvenue dans le processus d'inscription Aurora 💎* \n\n\
Pour votre information, les robots de trading Aurora sont *100% automatisés*. \n\n\
Il n'y a pas de signaux à suivre : les transactions *s'ouvrent et se ferment automatiquement*. 🤖\n\n\n\
*‼️ Voici un questionnaire obligatoire :*\n\n*-> Quel âge as-tu ?*", reply_markup=markup, parse_mode="Markdown")

#avertissement mineur
def fr_user_minor(chat_id):
    markup = InlineKeyboardMarkup(row_width=1)
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")

    markup.add(bt_support)
    
    bot.send_message(chat_id, f"*Le trading, tout comme les jeux d'argent, comporte des risques financiers. \
Malheureusement, en tant que mineur, tu ne peux pas bénéficier de nos services. Merci de ta compréhension.*", reply_markup=markup, parse_mode="Markdown")

#question country
def fr_user_country(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_major = InlineKeyboardButton('France', callback_data='eu')
    bt_minor = InlineKeyboardButton('Europe', callback_data='fr')
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")

    markup.add(bt_major, bt_minor, bt_support)
    
    bot.send_message(chat_id, f"Question 2/3\n\n-> Ton pays de résidence ? 🌏", reply_markup=markup, parse_mode="Markdown")
    
#question combien il va investir
def fr_user_pack(chat_id):
    markup = InlineKeyboardMarkup(row_width=2)
    bt_pack_start = InlineKeyboardButton('500 - 1000€', callback_data='pack_start')
    bt_pack_investissor = InlineKeyboardButton('+1000€', callback_data='pack_investissor')
    bt_support = InlineKeyboardButton('Contacter le support', url="https://t.me/auroraofficiel")
    
    markup.add(bt_pack_start, bt_pack_investissor, bt_support)
    
    bot.send_message(chat_id, f"*Question 3/3\n\n➡️ Combien es-tu prêt/e à investir chez nous ?*", reply_markup=markup, parse_mode="Markdown")

# Lancement du bot
bot.polling()
