import requests
from bs4 import BeautifulSoup
import random
import wikipedia
import webbrowser as wb
import pyjokes

def after():
    inps = input(">>> ")

    if inps == 'hi':
        print("Bot: Hello!")
    elif inps == 'weather':
        print("Bot: Please enter the name of the place whose weather you would like to know.")
        weather = input("Place: ")
        url = f'https://www.google.com/search?q=weather+{weather}&oq=weather+&aqs=chrome.0.69i59l4j69i60l4.2664j0j7&sourceid=chrome&ie=UTF-8'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find('div', class_='BNeawe').text
        print(f"Bot: Temprature for {weather} is {temp}")
    elif inps == 'wikipedia':
        aedvga = input("Search Wikipedia: ")
        results = wikipedia.summary(aedvga, sentences=10)
        print(results)
        repeat()
    elif inps == 'love you':
        print("Bot: But I don't 😎")
    elif inps == 'scrap':
        website = input("Website (Please define the full url) : ")
        url = website
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find().text
        print(temp)
    elif inps == 'youtube':
        print("Bot: Here you go")
        wb.open("https://youtube.com/")
    elif inps == 'what is your name':
        print("Bot: My name is Yae")
    elif inps == 'joke':
        joke = str(pyjokes.get_joke())
        print(f"Bot: {joke}")
    elif inps == 'goodbye':
        print("Goodbye")
        quit()
    else:
        lists = [
            'Kya bol raha hai bhai?', 
            'Pagal! pehele bolna toh seekhle gadhe', 
            'Muh se supari nikal kar baat kar re baba'
            ]
        notUnderstood = random.choice(lists)
        print(notUnderstood)
        repeat()



def repeat():
    while True:
        after()

repeat()