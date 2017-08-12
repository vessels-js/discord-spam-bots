import sys
import subprocess
from time import sleep
from config import *

w1 = "EDIT YOUR CONFIG.PY BEFORE USING!\n"

def worker(file,token):
    print(token + " " + file)
    subprocess.call(file, shell=True)

for char in w1:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
sleep(0.5)
print("Type one of the following numbers to launch that spammmer")
print("1 : Image Spammer - Spam random images in a selected folder")
print("2 : Insult Spammer - Picks insults offline and spams them")
print("3 : Text Spammer - Write your own text to spam")

in_pick = float(input("Select a bot: "))

if in_pick == 1:
    for token in userToken:
        p = subprocess.Popen('python discord_image_spam.py ' + token)
            
if in_pick == 2:
    for token in userToken:
        p = subprocess.Popen('python discord_insult_spam.py ' + token)
        
if in_pick == 3:
    spam_text = input("Write spam text : ")
    print('python discord_text_spam.py ' + "'"+spam_text+"'")
    for token in userToken:
        p = subprocess.Popen('python discord_text_spam.py ' + token + " "+'"'+spam_text+'"')

p.wait()
