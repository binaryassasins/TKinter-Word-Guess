# @author MOHAMAD SYAFIQ ASYRAF BIN BHARUDIN, MUHAMMAD 'ILYAS AMIERRULLAH BIN AB KARIM
import tkinter as tk
from tkinter import font, ttk

# create tkinter frame instance
window = tk.Tk()
window.title("GREENBOT INTEL WORD GUESS")
window.geometry("500x250")

# create two frames in tkinter frame instance
main_frame = tk.Frame(window)
guess_frame = tk.Frame(window)

# configure font type
font_type = tk.font.Font(family="Arial", size=13, weight="bold")

greet = tk.Label(main_frame, text="Hello Student!\nChoose your category")
description = tk.Label(guess_frame, text="Guess as much word as you can\nin relation to the chosen category\n")

inputEntry = tk.Entry(guess_frame, width=40, relief="groove", font=("Arial 10"))

fig1 = tk.Label(guess_frame, text="HILARIAJUANANSINMMAJDMBU", font=("Arial 10 bold"))
fig2 = tk.Label(guess_frame, text="TRISTANSHICHIROAJYAGLKATIFZ", font=("Arial 10 bold"))
fig3 = tk.Label(guess_frame, text="KAATASHIFRLANKLYNHAUSNIAFAIHIH", font=("Arial 10 bold"))
fig4 = tk.Label(guess_frame, text="MALANDRAANAISSIAHHAIBUSIU", font=("Arial 10 bold"))
result = tk.Label(guess_frame, text="Result: Please enter your input", font=("Arial 10"))

counter = 0

# define counter display
matched = tk.Label(guess_frame, text=("Score: " + str(counter)), font=("Arial 10"))

# create category buttons
# using string as an argument in for loop requires an empty dictionary for it to iterate over (as list only allow integers and slices as its indices)
button_dict = {}
categories = ["ISLAMIC FIGURES", "IBADAH", "SURAH", "PROPHETS"]

# empty occurence list
input_occurence = []

# create ttk style instance
s = ttk.Style()
# configure ttk style instance (identifier, styling)
s.configure('my.TButton', font = ("Arial", 10))

def quitToMenu():
    # hide all widgets
    guess_frame.pack_forget()
    fig1.pack_forget()
    fig2.pack_forget()
    fig3.pack_forget()
    fig4.pack_forget()
    inputEntry.pack_forget()
    matched.pack_forget()
    result.pack_forget()
    submitBtn.pack_forget()
    quitBtn.pack_forget()
    # invoke mainframe func
    mainframe()

def getInput():
    global counter, input_occurence
    # store entered value in a variable
    inputText = inputEntry.get()
    print("User entered: " + str(inputText))

    # compare input with items in categories
    for ans in answers:
        if inputText == ans:
            exist_count = input_occurence.count(inputText)
            print("Exist: " + str(exist_count))
            if exist_count == 0:
                input_occurence.append(inputText)
                print(input_occurence)
                counter = counter + 1
                matched['text'] = 'Score: ' + str(counter)
                result.config(text="Result: Correct!")
                print("Score: " + str(counter))
                break;
            else:
                print("\tContinue...")
        else:
            result.config(text="Result: Incorrect!")

def guess(x):
    print("User click: " + x)
    main_frame.pack_forget()
    guess_frame.pack()
    description.configure(font = font_type)
    description.pack()
    global answers, submitBtn, quitBtn
    if x == "ISLAMIC FIGURES":
        answers = ["IBN SINA", "AL JURJANI", "MUHAMMAD", "IBN RUSHD"]
        # display scribbled word
        fig1.pack()
        # display input box
        inputEntry.pack()
        # display counter
        matched.pack()
        # display result
        result.pack()
        # display submit button
        submitBtn.pack()
        # display quit to menu button
        quitBtn.pack()
    elif x == "IBADAH":
        answers = ["SOLAT", "ZIKIR", "CHARITY", "FASTING", "HAJJ"]
        fig2.pack()
        inputEntry.pack()
        matched.pack()
        result.pack()
        submitBtn.pack()
        quitBtn.pack()
    elif x == "SURAH":
        answers = ["AL FATIHAH", "AL IKHLAS", "AN NUR", "AL KAHFI", "YAASIN"]
        fig3.pack()
        inputEntry.pack()
        matched.pack()
        result.pack()
        submitBtn.pack()
        quitBtn.pack()
    elif x == "PROPHETS":
        answers = ["NUH", "ADAM", "SULAIMAN", "ISA", "MUSA", "IBRAHIM"]
        fig4.pack()
        inputEntry.pack()
        matched.pack()
        result.pack()
        submitBtn.pack()
        quitBtn.pack()

def mainframe():
    start.pack_forget()
    
    # apply styling to greet instance
    greet.configure(font = font_type)
    greet.pack()

    # create category buttons
    for i in categories:
        def cat_func(x=i):
            for j in categories:
                button_dict[j].pack_forget()
            guess(x)
        
        button_dict[i] = ttk.Button(main_frame, text=i, command=cat_func, width=30, style='my.TButton')
        button_dict[i].pack()

    main_frame.pack()

# define start button
start = ttk.Button(window, text="START", command=mainframe, padding=20, width=35)
start.pack()

# define submit and quit buttons
submitBtn = ttk.Button(guess_frame, text="Check", command=getInput, width=20, style='my.TButton', padding=5)
quitBtn = ttk.Button(guess_frame, text="Return to main menu", command=quitToMenu, width=20, style='my.TButton', padding=5)

# loop events
window.mainloop()