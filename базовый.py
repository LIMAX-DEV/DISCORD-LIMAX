from программа.Полезный.Config import *
from программа.Полезный.cfg import *
import os
import time

try:
   import webbrowser
   import re
   import pyzipper
   from tkinter import messagebox
   import subprocess
   import sys
   import threading
except Exception as e:
   ErrorModule(e)

option_01 = "Discord-Token-Nuker"
option_02 = "Discord-Token-Info"
option_03 = "Discord-Token-Joiner"
option_04 = "Discord-Token-Leaver"
option_05 = "Discord-Token-Login"
option_06 = "Discord-Token-To-Id-And-Brute"
option_07 = "Discord-Token-Server-Raid"
option_08 = "Discord-Token-Spammer"
option_09 = "Discord-Token-Delete-Friends"
option_10 = "Discord-Token-Block-Friends"
option_11 = "Discord-Token-Mass-Dm"
option_12 = "Discord-Token-Delete-Dm"
option_13 = "Discord-Token-Status-Changer"
option_14 = "Discord-Token-Language-Changer"
option_15 = "Discord-Token-House-Changer"
option_16 = "Discord-Token-Theme-Changer"
option_17 = "Discord-Webhook-Spammer"
option_18 = "Discord-Bot-Server-Nuker"
option_19 = "Discord-Bot-Invite-To-Id"
option_20 = "Discord-Server-Info"
option_21 = "Discord-Webhook-Info"
option_22 = "Discord-Webhook-Delete"




option_01_txt = f"{purple}[{white}01{purple}]{purple} " + option_01.ljust(30)[:30].replace("-", " ")
option_02_txt = f"{purple}[{white}02{purple}]{purple} " + option_02.ljust(30)[:30].replace("-", " ")
option_03_txt = f"{purple}[{white}03{purple}]{purple} " + option_03.ljust(30)[:30].replace("-", " ")
option_04_txt = f"{purple}[{white}04{purple}]{purple} " + option_04.ljust(30)[:30].replace("-", " ")
option_05_txt = f"{purple}[{white}05{purple}]{purple} " + option_05.ljust(30)[:30].replace("-", " ")
option_06_txt = f"{purple}[{white}06{purple}]{purple} " + option_06.ljust(30)[:30].replace("-", " ")
option_07_txt = f"{purple}[{white}07{purple}]{purple} " + option_07.ljust(30)[:30].replace("-", " ")
option_08_txt = f"{purple}[{white}08{purple}]{purple} " + option_08.ljust(30)[:30].replace("-", " ")
option_09_txt = f"{purple}[{white}09{purple}]{purple} " + option_09.ljust(30)[:30].replace("-", " ")
option_10_txt = f"{purple}[{white}10{purple}]{purple} " + option_10.ljust(30)[:30].replace("-", " ")
option_11_txt = f"{purple}[{white}11{purple}]{purple} " + option_11.ljust(30)[:30].replace("-", " ")
option_12_txt = f"{purple}[{white}12{purple}]{purple} " + option_12.ljust(30)[:30].replace("-", " ")
option_13_txt = f"{purple}[{white}13{purple}]{purple} " + option_13.ljust(30)[:30].replace("-", " ")
option_14_txt = f"{purple}[{white}14{purple}]{purple} " + option_14.ljust(30)[:30].replace("-", " ")
option_15_txt = f"{purple}[{white}15{purple}]{purple} " + option_15.ljust(30)[:30].replace("-", " ")
option_16_txt = f"{purple}[{white}16{purple}]{purple} " + option_16.ljust(30)[:30].replace("-", " ")
option_17_txt = f"{purple}[{white}17{purple}]{purple} " + option_17.ljust(30)[:30].replace("-", " ")
option_18_txt = f"{purple}[{white}18{purple}]{purple} " + option_18.ljust(30)[:30].replace("-", " ")
option_19_txt = f"{purple}[{white}19{purple}]{purple} " + option_19.ljust(30)[:30].replace("-", " ")
option_20_txt = f"{purple}[{white}20{purple}]{purple} " + option_20.ljust(30)[:30].replace("-", " ")
option_21_txt = f"{purple}[{white}21{purple}]{purple} " + option_21.ljust(30)[:30].replace("-", " ")
option_22_txt = f"{purple}[{white}22{purple}]{purple} " + option_22.ljust(30)[:30].replace("-", " ")





menu1 = f""" {' ' * 93} 
                                              

 {option_01_txt}          {option_12_txt}                                      
 {option_02_txt}          {option_13_txt}                                      
 {option_03_txt}          {option_14_txt}                                      
 {option_04_txt}          {option_15_txt}                                      
 {option_05_txt}          {option_16_txt}                                     
 {option_06_txt}          {option_17_txt}                                                                                                
 {option_07_txt}          {option_18_txt}                          
 {option_08_txt}          {option_19_txt}          
 {option_09_txt}          {option_20_txt}          
 {option_10_txt}          {option_21_txt}          
 {option_11_txt}          {option_22_txt}                                
          
"""

def Menu():
   popup_version = ""
   menu = menu1
   menu_number = "1"

   banner = f"""{popup_version}{purple}  


▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ██▓     ██▓ ███▄ ▄███▓ ▄▄▄      ▒██   ██▒
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌   ▓██▒    ▓██▒▓██▒▀█▀ ██▒▒████▄    ▒▒ █ █ ▒░
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▒██░    ▒██▒▓██    ▓██░▒██  ▀█▄  ░░  █   ░
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▒██░    ░██░▒██    ▒██ ░██▄▄▄▄██  ░ █ █ ▒ 
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ░██████▒░██░▒██▒   ░██▒ ▓█   ▓██▒▒██▒ ▒██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░ ▒░▓  ░░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░▒▒ ░ ░▓ ░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░ ░ ▒  ░ ▒ ░░  ░      ░  ▒   ▒▒ ░░░   ░▒ ░
 ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░      ░ ░    ▒ ░░      ░     ░   ▒    ░    ░  
   ░     ░        ░  ░ ░          ░ ░     ░        ░           ░  ░ ░         ░         ░  ░ ░    ░  
 ░                   ░                           ░                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
{menu}"""
   return banner, menu_number

while True:
   try:
      Clear()

      banner, menu_number = Menu()

      Title(f"Menu {menu_number}")
      Slow(MainColor(banner))

      choice = input(MainColor(f"""{purple}DIGA O QUE DESEJA ?{purple}"""))

      options = {
         '01': option_01, '02': option_02, '03': option_03, '04': option_04,
         '05': option_05, '06': option_06, '07': option_07, '08': option_08,
         '09': option_09, '10': option_10, '11': option_11, '12': option_12,
         '13': option_13, '14': option_14, '15': option_15, '16': option_16,
         '17': option_17, '18': option_18, '19': option_19, '20': option_20,
         '21': option_21, '22': option_22, } 

      if choice in options:  
         StartProgram(f"{options[choice]}.py")
      elif len(choice) == 1 and '0' + choice in options:
         StartProgram(f"{options['0' + choice]}.py")
      else:
         ErrorChoiceStart()

   except Exception as e:
      Error(e)