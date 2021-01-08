from tkinter import *
import  pandas as pd 
import random
import time

from pandas.core.frame import DataFrame
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
################### Read the csv files ###############################
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/german_words.csv")
    to_learn  = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient="records")
################# Functions ##################
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = random.choice(to_learn)
    current_card["German"]
    canvas.itemconfig(card_title, text = "Deutsch", fill = "black")
    canvas.itemconfig(card_word, text = current_card["German"],fill= "black" )
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index= False)
    next_card()
    
#################### Create the User Interface (UI) with Tkinter###################
window = Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width = 800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image= front_image)
card_title = canvas.create_text(400, 150, text="Deutsch", font = ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font = ("Arial", 60, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command= next_card)
unknown_button.grid(row = 2, column = 1)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command= is_known)
known_button.grid(row = 2, column = 2)
next_card()
window.mainloop()
