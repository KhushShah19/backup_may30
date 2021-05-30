import requests
import smtplib
from bs4 import BeautifulSoup as bs
import re
"""
a = requests.get("https://en.wikipedia.org/wiki/Web_scraping")
b = BeautifulSoup(a.content, "html.parser")
# print(b)

c = BeautifulSoup(a.content)
print(c)

import glob
import xmltodict
import json
import xml.etree.ElementTree as ET
"""

# a = requests.get("https://readwebnovels.net/novel/i-alone-lvl-up/")
# b = BeautifulSoup(a.content, "html.parser")
#print(b)

c = requests.get("https://readwebnovels.net/novel/i-alone-lvl-up/chapter-1_1/")
d = bs(c.content, "html.parser")
novel = ("https://readwebnovels.net/novel/i-alone-lvl-up/chapter-1_1/")
req = requests.get(novel)
soup = bs(req.text, "html.parser")
# soup = bs(novel, "html.parser")
# main

#for page in range(1, 2):
# str("(page)_01")
# req = requests.get(novel, str("(page)_01"))

# print(req)

# container = soup.find_all(class_="entry-content")

contain = soup.find_all(class_="text-left")
# p_tag = soup.p
#print(p_tag)
print(type(contain))
print(contain)
#mnb = contain.__getattr__(filter(classmethod, "p"))
#print(mnb)
# kon = (soup.get_text(" "))  ############ tags removed
# print(type(kon))
print("jkjkjkjkjkj")
# print(kon)
# print(re.findall("Prologue[.*]", kon))
# kons = kon.str.replace("\n", " ")
#bnm = kon.str.strip(" ")
#print(bnm)
# help(str)

# print(soup.prettify())  ########## easy to get all ch.
#p_tag.p.unwrap()
#print(p_tag)

"""contain = soup.find_all(class_="text-left")
car = soup.find_all("p")
print(car)
for cars in car:
    print(repr(cars))
print("rrrrrrrrr")
# print(contain)"""
# try_01
"""
aim = soup.find("p")
print(type(aim))
print(aim)
aims = aim.find_previous_siblings("p")
print(type(aims))
print(aims)
"""   # try_02
# fun = soup.find("p")
# funny = soup.find("h4")
# cup = soup.find_all("p")
"""for tag in contain:
    tag.find_all('<p>').replace_with(' ')

ChampInfo = [ci.get_text() for ci in contain.select(".ChampionInfo .ChampionName")]

for tag in ChampInfo:
    tag.find_all('<p>').replace_with('\n')
"""
# print(cup)
# print(funny)
# print(fun)
# print(container)
# print(fun)

# print(re.findall("([.*]<p/>)", str(container)))

#names = container.find_all("h4")
#print(names)
"""
import smtplib


import config
import time



def send_email(subject, msg):

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(config.ADD, config.PASS)
    message = "Subject: {}\n\n{}".format(subject, msg)
    server.sendmail(config.ADD, config.ADD, message)
    server.quit()
    print("done")


config.ADD = "my.personal4123@gmail.com"
config.PASS = "red4123one"

subject = "ghost"
msg = "now i can send email though "

while True:
    send_email(subject, msg)
   # time.sleep(5)


"""
"""
novel = ("https://readwebnovels.net/novel/i-alone-lvl-up/chapter-1_1/")
req = requests.get(novel)
soup = bs(req.text, "html.parser")
contain = soup.find_all(class_="text-left")

# everything is fine till here, after this all gone

ChampInfo = [ci.get_text() for ci in contain.select(".ChampionInfo .ChampionName")]

for tag in ChampInfo:
    tag.find_all('<p>').replace_with('\n')
"""
#





#



print("NEW BOOK SCRAP..........")

bun = "https://novelfull.com/reincarnation-of-the-strongest-sword-god/chapter-1-starting-over.html"
r = requests.get(bun)
cup = bs(r.text, "html.parser")
base = cup.find_all(id_="chapter-content")
case = cup.find_all(class_="chapter-c")

# div = cup.find_all("div")
print(base)
print(case)
tan = case.remove( )
jo = " ".join(case)
print(jo)
f = open("sd01", "w")
f.write(case)
print(f)

print("done")
# class_="chapter-c"




















































































































































































































































