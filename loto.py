# -*- coding: utf-8 -*-

# НАЗВАНИЕ БОТА: Конструктор ботов 
# ОПИСАНИЕ БОТА: Бот могает клиенту определиться с заказом
# АВТОР БОТА   : Купинов Вадим
# ТЕЛЕГРАММ АВТОРА : @Pi_3dot141 (https://t.me/Pi_3dot141) 

import telebot
import sqlite3
import random
import time  
import random

from telebot import types


print ('Версия 3.0')

def load_staus (user_id):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,status from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,status = row
        print ('[+]',user_id,status)
    return status

def save_status (user_id,username,status):
    label = 'no'
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id = row
        print ('[+]',user_id)
        label = 'yes'
    if label == 'no':
        print ('[+] Новый User'+str(user_id))
        cursor = conn.cursor()
        a = [str(user_id),str(username),'','','','','','','','','100',status]    
        cursor.execute("INSERT INTO user (user_id,username,name,first_name,last_name,setting01,setting02,setting03,setting04,setting05,setting06,status)VALUES (?,?,?,?,?,?,?,?,?,?,?,?);",a)    
        conn.commit()
    else:
        sql = "UPDATE user SET status = '"+str(status)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
        print ('[+] User изменен: '+str(user_id))
   
def save_param (user_id,nom,znak):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    if nom == 1:
        sql = "UPDATE user SET setting01 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 2:    
        sql = "UPDATE user SET setting02 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 3:    
        sql = "UPDATE user SET setting03 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 4:    
        sql = "UPDATE user SET setting04 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 5:    
        sql = "UPDATE user SET setting05 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()
    if nom == 6:    
        sql = "UPDATE user SET setting06 = '"+str(znak)+"' WHERE user_id = '"+str(user_id)+"' "
        cursor.execute(sql)
        conn.commit()

def load_param (user_id,nom):
    conn = sqlite3.connect("user.sqlite") 
    cursor = conn.cursor()
    sql = "select id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 from user where user_id = '"+str(user_id)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 = row
        if nom == 1:
            print ('[+1]',user_id,setting01)
            return setting01
        if nom == 2:
            print ('[+2]',user_id,setting02)
            return setting02
        if nom == 3:
            print ('[+3]',user_id,setting03)
            return setting03
        if nom == 4:
            print ('[+4]',user_id,setting04)
            return setting04
        if nom == 5:
            print ('[+5]',user_id,setting05)
            return setting05
        if nom == 6:
            print ('[+6]',user_id,setting06)
            return setting06


def game_priz ():
    conn = sqlite3.connect("prize.sqlite") 
    cursor = conn.cursor()
    sql = "select id,name,summ,status from priz where status = 'start' Limit 1"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        id_v,name,summ,status = row
        
        sql = "UPDATE priz SET status = 'game' WHERE id = '"+str(id_v)+"'"
        cursor.execute(sql)
        conn.commit()
        
        
        conn = sqlite3.connect("user.sqlite") 
        cursor = conn.cursor()
        sql = "select id,user_id,setting01,setting02,setting03,setting04,setting05,setting06 from user where 1=1"
        cursor.execute(sql)
        data = cursor.fetchall()
        for raw in data:
            id_send,user_id_send,setting01,setting02,setting03,setting04,setting05,setting06 = raw        
            message_out = name 
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(types.InlineKeyboardButton(text='Нажми первым  и выграй 100$', callback_data='answer'))
            print ('[+ id_send:]',user_id_send)
            bot.send_message(user_id_send, message_out, reply_markup=keyboard)   
                   
   
def print_massage (message,status):
    ### настройка цвета для вывода на экран
    c0  =  "\033[0;37m"  ## Белый
    c1  =  "\033[1;30m"  ## Черный
    c2  =  "\033[0;31m"  ## Красный
    c3  =  "\033[0;32m"  ## Зеленый
    c4  =  "\033[1;35m"  ## Magenta like Mimosa\033[1;m
    c5  =  "\033[1;33m"  ## Yellow like Yolk\033[1;m'
    c7  =  "\033[1;37m"  ## White
    c8  =  "\033[1;33m"  ## Yellow
    c9  =  "\033[1;32m"  ## Green
    c10 =  "\033[1;34m"  ## Blue
    c11 =  "\033[1;36m"  ## Cyan
    c12 =  "\033[1;31m"  ## Red
    c13 =  "\033[1;35m"  ## Magenta
    c14 =  "\033[1;30m"  ## Black
    c15 =  "\033[0;37m"  ## Darkwhite
    c16 =  "\033[0;33m"  ## Darkyellow
    c17 =  "\033[0;32m"  ## Darkgreen
    c18 =  "\033[0;34m"  ## Darkblue
    c19 =  "\033[0;36m"  ## Darkcyan
    c20 =  "\033[0;31m"  ## Darkred
    c21 =  "\033[0;35m"  ## Darkmagenta
    c22 =  "\033[0;30m"  ## Darkblack
    c23 =  "\033[0;0m"   ## Off
    
    name_program = 'courier'
    if status == '[s]':
        print ( c0+'Старт программы: '+c8+message+c0)
    if status == '[+]':
        print ( c9+'[+] '+c0+message+c0)
    if status == '[!]':
        print (c12+'[!] '+c0+message+c0)

if __name__ == "__main__":
    token = '594826433:AAGLBVRG4g01nx4QV6sCPrjKtTkEk0KwESM'
    bot    = telebot.TeleBot(token)
    print_massage ('@super_loto_bot','[s]')
    game_priz ()

def menu_skolko ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('3 чел.','5 чел.','10 чел.')
    markup.row('25 чел.','50 чел.','100 чел.')
    return markup

def menu_stavka ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('1$','3$','5$')
    markup.row('10$','25$','50$')
    return markup

def menu_main ():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Меню')
    return markup
        
def game (user_id):    
    if 1==1:     
        print ('[++1+]'+str(user_id))
        print ('[+++]'+load_param (user_id,1))        
        sum = load_param (user_id,1)
        sum = sum.replace('$', '')            
        kollpost = int(sum)        
        for k in range (kollpost-1):        
            sm = random.randint(1, 10)
            print ('Ждем: ',sm,' сек.')
            time.sleep(sm)    
            markup = menu_main ()
            message_out = 'Играет '+str(k+2)+' игрока. Ждем еще '+str(kollpost-k-2)+' человек.'
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)  
        markup = menu_main ()
        
        print ('[+k]',kollpost)
        sm = random.randint(1, kollpost)
        if sm == 1:                     
            setting02 = load_param (user_id,2)
            setting06 = load_param (user_id,6)
            balans = float (setting06)
            oldbalans = balans 
            stavka = float (setting02)
            winsumm = stavka*kollpost 
            balans = balans + winsumm -stavka           
            save_param (user_id,6,str(balans))
            save_param (user_id,2,'')
            message_out = 'УРА !!!\nВы выграли !!!\nВаш баланс:'+str(balans)+'$ '            
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)            
            message_out = '<b>ОТЧЕТ</b>\nВыиграш:'+str(winsumm)+'$\nБыло на счете: '+str(oldbalans)+'$\nВаша ставка: -'+str(stavka)+'$\nКолличество игроков: '+str(kollpost)+'\nБаланс: '+str(balans)+'$'+'\n/balans'            
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
            
                        
        else:    
            setting02 = load_param (user_id,2)
            setting06 = load_param (user_id,6)
            balans = float (setting06)
            oldbalans = balans 
            stavka = float  (setting02)
            balans = balans - stavka             
            save_param (user_id,6,str(balans))
            save_param (user_id,2,'')
            message_out = 'УВЫ\nВы проиграли\nВаш баланс:'+str(balans)+'$'
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)            
            message_out = '<b>ОТЧЕТ</b>\nБыло на счете: '+str(oldbalans)+'$\nВаша ставка: -'+str(stavka)+'$\nКолличество игроков: '+str(kollpost)+'\nБаланс: '+str(balans)+'$'+'\n/balans'             
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
                   
    

@bot.message_handler(commands=['balans'])
def send_welcome(message):
        username   = message.from_user.username
        first_name = message.from_user.first_name
        last_name  = message.from_user.last_name
        user_id    = message.from_user.id
        date       = message.date
        message    = message.text
        setting06 = load_param (user_id,6) ## баланс
        message_out = 'Ваш текущий баланс: '+str(setting06)+'$'
        bot.send_message(user_id,message_out,parse_mode='HTML')   
        

    

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if 1==1:
        username   = message.from_user.username
        first_name = message.from_user.first_name
        last_name  = message.from_user.last_name
        user_id    = message.from_user.id
        date       = message.date
        message    = message.text
        print_massage (message+str(user_id),'[+]')
        save_status (user_id,username,'start')
        save_param (user_id,1,'')
        save_param (user_id,2,'')
        save_param (user_id,3,'')
        save_param (user_id,4,'')
        save_param (user_id,5,'')        
        message_out = 'Супер лото. Ставки среди реальных людей. Лото!'
        bot.send_message(user_id,message_out,parse_mode='HTML')    
        message_out = 'Ваш баланс '+str(load_param (user_id,6))+'$'
        bot.send_message(user_id,message_out,parse_mode='HTML')    
        markup = menu_skolko ()
        message_out = 'В какой группе людей вы хотите попытать счастье?'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)       
        save_status (user_id,username,'skolko')
        
        
  
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
    user_id    = message.from_user.id 
    message    = message.text
    first_name = ''
    last_name  = ''
    username   = ''
    date       = ''
    print_massage (message+str(user_id),'[+]')
    status = load_staus (user_id)
        
    ##save_param (user_id,1,str(message))  КОЛЛИЧЕСТВО УЧАСТНИКОВ
        
    if status == 'skolko':    
        grupa = 0
        if message == '3 чел.':
            grupa = 3 
            message_out = 'В игре участвуют три человека. Включая Вас.'
            bot.send_message(user_id,message_out,parse_mode='HTML') 
        if message == '5 чел.':
            grupa = 5
            message_out = 'В игре участвуют пять человек. Включая Вас.'
            bot.send_message(user_id,message_out,parse_mode='HTML') 
        if message == '10 чел.':
            grupa = 10
            message_out = 'В игре участвуют десять человек. Включая Вас.'
            bot.send_message(user_id,message_out,parse_mode='HTML') 
 
        if message == '25 чел.':
            grupa = 25
            message_out = 'В игре участвуют 25 человек. Включая Вас.'
            bot.send_message(user_id,message_out,parse_mode='HTML') 
             
        if message == '50 чел.':
            grupa = 50
            message_out = 'В игре участвуют 50 человек. Включая Вас.'
            bot.send_message(user_id,message_out,parse_mode='HTML') 
             
        if message == '100 чел.':
            grupa = 100     
            message_out = 'В игре участвуют 100 человек. Включая Вас.'
            bot.send_message(user_id,message_out,parse_mode='HTML') 
            
            
        markup = menu_stavka ()
        message_out = 'На какую сумму Вы желаете сыграть? Если Вы выиграйте то получите ВСЕ'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)  
        print ('[Колличество людей]',grupa) 
        save_param (user_id,1,str(grupa))   
        save_status (user_id,username,'stavka')

    if status == 'stavka':
    
        summstav = 0
        if message.find ('1$') != -1:
            summstav = 1
                                             
        if message.find ('3$') != -1:
            summstav = 3
                                                          
        if message.find ('5$') != -1:
            summstav = 5
                                   
        if message.find ('10$') != -1:
            summstav = 10
                                  
        if message.find ('25$') != -1:
            summstav = 25
                    
        if message.find ('50$') != -1:
            summstav = 50

        message_out = 'Ставка принята.Играем на '+str(summstav)+'$. Ждем взнос от других'
        bot.send_message(user_id,message_out,parse_mode='HTML')          
        save_param (user_id,2,str(summstav))        
        markup = menu_main ()
        message_out = 'Вы первый игрок. Ждем других'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)  
        save_status (user_id,username,'begin')  
        game (user_id)         
        status = 'begin'                                  
        markup = menu_skolko ()
        message_out = 'Сколько ждать учатников?\n'
        bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)               
        save_status (user_id,username,'skolko')
        
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   if call.message:
        user_id = call.message.chat.id    
        if call.data.find ("answer") != -1:  
        
            label = 'no'
            conn = sqlite3.connect("prize.sqlite") 
            cursor = conn.cursor()
            sql = "select id,name,summ,status from priz where status = 'game' Limit 1"
            cursor.execute(sql)
            data = cursor.fetchall()
            for row in data:
                id,name,summ,status = row        
                sql = "UPDATE priz SET status = 'game' WHERE id = '"+str(id)+"'"
                cursor.execute(sql)
                conn.commit()
                label = 'yes'
                
                setting06 = load_param (user_id,6)
                balans = float (setting06)
                save_param (user_id,6,str(balans+summ))  


            if label == 'yes':
                message_out = 'Вы выиграли: '+str(summ)+'$'  
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out)
            else:    
                message_out = 'Не успел'  
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=message_out)
            
            
bot.polling()
