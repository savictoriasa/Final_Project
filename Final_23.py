import random
import tkinter


#Create Object 
root = tkinter.Tk() 
 
#pop up size
root.geometry("800x400")

#background set to black
root.configure(bg = "black")
 
#pop up title 
root.title("Rock Paper Scissors Lizard Spock") 


#computer options 
comp_choice = { 
"0":"Rock", 
"1":"Paper", 
"2":"Scissors",
"3":"Lizard",
"4":"Spock"
} 


#restarts game 
def reset_game(): 
    b1["state"] = "active" 
    b2["state"] = "active" 
    b3["state"] = "active"
    b4["state"] = "active" 
    b5["state"] = "active" 
    l1.config(text = "Player            ") 
    l3.config(text = "Computer") 
    l4.config(text = "") 


#disable buttons 
def button_disable(): 
    b1["state"] = "disable" 
    b2["state"] = "disable" 
    b3["state"] = "disable" 
    b4["state"] = "disable" 
    b5["state"] = "disable"


    

#player selects rock 
def player_rock(): 
    c_v = comp_choice[str(random.randint(0,4))] 
    if c_v == "Rock": 
        match_result = "Tie!" 
    elif c_v == "Paper": 
        match_result = "Paper covers Rock! Computer Wins!"
    elif c_v =="Scissors": 
        match_result = "Rock crushes Scissors! Player Wins!"
    elif c_v == "Lizard":
        match_result = "Rock crushes Lizard! You win!"
    elif c_v == "Spock":
        match_result = "Spock vaporizes Rock! Computer wins!"
    l4.config(text = match_result) 
    l1.config(text = "Rock            ") 
    l3.config(text = c_v) 
    button_disable() 

#player selects paper 
def player_paper(): 
    c_v = comp_choice[str(random.randint(0, 4))] 
    if c_v == "Rock": 
        match_result = "Paper covers Rock! You win!" 
    elif c_v == "Paper": 
        match_result = "Tie!"
    elif c_v =="Scissors": 
        match_result = "Scissors cuts Paper! Computer wins!!"
    elif c_v == "Lizard":
        match_result = "Lizard eats Paper! Computer wins!"
    elif c_v == "Spock":
        match_result = "Paper disproves Spock! You win!" 
    l4.config(text = match_result) 
    l1.config(text = "Paper            ") 
    l3.config(text = c_v) 
    button_disable() 

#player selects scissors 
def player_scissors(): 
    c_v = comp_choice[str(random.randint(0,4))] 
    if c_v == "Rock": 
        match_result = "Rock crushes Scissors! Computer wins!" 
    elif c_v == "Paper": 
        match_result = "Scissors cuts Paper! You win!"
    elif c_v =="Scissors": 
        match_result = "Tie!"
    elif c_v == "Lizard":
        match_result = "Scissors decapitates Lizard! You win!"
    elif c_v == "Spock":
        match_result = "Spock smashes Scissors! Computer wins!" 
    l4.config(text = match_result) 
    l1.config(text = "Scissors            ") 
    l3.config(text = c_v) 
    button_disable()

#player selects lizard
def player_lizard(): 
    c_v = comp_choice[str(random.randint(0,4))] 
    if c_v == "Rock": 
        match_result = "Rock crushes Lizard! Computer wins!" 
    elif c_v == "Paper": 
        match_result = "Lizard eats Paper! You win!"
    elif c_v =="Scissors": 
        match_result = "Scissors decapitates Lizard! Computer wins!"
    elif c_v == "Lizard":
        match_result = "Tie!"
    elif c_v == "Spock":
        match_result = "Lizard poisons Spock! You win!" 
    l4.config(text = match_result) 
    l1.config(text = "Lizard            ") 
    l3.config(text = c_v) 
    button_disable()
    
#player selects spock
def player_spock(): 
    c_v = comp_choice[str(random.randint(0,4))] 
    if c_v == "Rock": 
        match_result = "Spock vaporizes Rock! You win!" 
    elif c_v == "Paper": 
        match_result = "Paper disproves Spock! Computer wins!"
    elif c_v =="Scissors": 
        match_result = "Spock smashes Scissors! You win!"
    elif c_v == "Lizard":
        match_result = "Lizard poisons Spock! Computer wins!"
    elif c_v == "Spock":
        match_result = "Tie!" 
    l4.config(text = match_result) 
    l1.config(text = "Spock            ") 
    l3.config(text = c_v) 
    button_disable()



#Label for game title 
tkinter.Label(root, 
    text = "Let's play Rock, Paper, Scissors, Lizard, Spock! Pick your choice.", 
    font = "Garamond",
    fg = "red",
    bg = "black").pack(pady = 20)  

#frame for text
frame = tkinter.Frame(root)
frame.pack() 
    
l1 = tkinter.Label(frame, 
    text = "Player            ", 
    font = 15,
    bg = "black",
    fg = "light slate blue") 

l2 = tkinter.Label(frame, 
    text = "VS	", 
    font = "Consolas",
    bg = "black",
    fg = "light slate blue") 

l3 = tkinter.Label(frame,
    text = "Computer",
    font = 15,
    bg = "black",
    fg = "light slate blue") 

l1.pack(side = 'left') 
l2.pack(side = 'left') 
l3.pack(side = 'right') 

#display of results
l4 = tkinter.Label(root, 
        text = "", 
        font = "Garamond", 
        bg = "black",
        fg = "white", 
        width = 50 , 
        borderwidth = 2,
        relief = "solid") 
l4.pack(pady = 20,)

#frame for buttons
frame1 = tkinter.Frame(root,
        bg = "black") 
frame1.pack() 

b1 = tkinter.Button(frame1, text = "Rock", 
            font = 8, width = 7, bg = "HotPink1", relief = "groove",
            command = player_rock) 

b2 = tkinter.Button(frame1, text = "Paper ", 
            font = 8, width = 7, bg = "tan1", relief = "groove",
            command = player_paper) 

b3 = tkinter.Button(frame1, text = "Scissors", 
            font = 8, width = 7, bg = "LightGoldenrod1", relief = "groove", 
            command = player_scissors)

b4 = tkinter.Button(frame1, text = "Lizard", 
            font = 8, width = 7, bg = "DarkOliveGreen1", relief = "groove",
            command = player_lizard)

b5 = tkinter.Button(frame1, text = "Spock", 
            font = 8, width = 7, bg = "light blue", relief = "groove",
            command = player_spock)

b1.pack(side = 'left', padx = 10) 
b2.pack(side = 'left', padx = 10) 
b3.pack(side = 'left', padx = 10)
b4.pack(side = 'left', padx = 10) 
b5.pack(side = 'left', padx = 10) 

#play again button
tkinter.Button(root, text = "Play Again", 
        font = "Garamond", fg = "red", relief = "flat", 
        bg = "black", command = reset_game).pack(pady = 20)


#execute tkinter 
root.mainloop() 
