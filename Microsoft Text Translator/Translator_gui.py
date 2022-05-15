# from curses import COLOR_BLUE, COLOR_WHITE
import tkinter as tk
from turtle import color, width
import requests

url = "https://microsoft-translator-text.p.rapidapi.com/translate"

languages = {"Spanish": "es", "German": "de", "French": "fr", "English": "en"}

# text = input("\nEnter the text to be translated : ")

# lan2 = input("Enter the conversion language : ").capitalize()

querystring = {"to[0]": "es", "api-version": "3.0", "profanityAction": "NoAction", "textType": "plain"}

payload = [{"Text": "text"}]

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com",
    "X-RapidAPI-Key": "e228ed9bcdmsha1fc0c3f1222c75p1d3eafjsn15f97a40c083"
}

response = requests.request("POST", url, json=payload, headers=headers, params=querystring)

master = tk.Tk()
master.title("Translator")
master.minsize(500,500)
# master.resizable(True)
# tk.
tk.Label(master, text='Enter the Text : ',font=('Times_new_Roman', 14)).grid(row=0)

text = tk.Entry(master)
text.grid(row=0, column=1, ipadx=120, padx=20, pady=10)


v = tk.IntVar()
tk.Radiobutton(master, text='English', variable=v, value=1).grid(row=3, pady=10, columnspan=10)
tk.Radiobutton(master, text='French', variable=v, value=2).grid(row=4, pady=10, columnspan=10)
tk.Radiobutton(master, text='German', variable=v, value=3).grid(row=5, pady=10, columnspan=10)
tk.Radiobutton(master, text='Spanish', variable=v, value=4).grid(row=6, pady=10, columnspan=10)

dwnd = tk.PhotoImage(file='Translate.png')
tk.Button(master, image=dwnd, width=0, background='#163dd9', foreground='#fafafc').pack()
tk.mainloop()