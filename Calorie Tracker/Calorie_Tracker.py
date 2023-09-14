import customtkinter

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("../Calorie Tracker/module1.json")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("Calorie Tracker")
app.minsize(400,200)

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)


def weight_input(event):
    if weight_input_button.get().isdigit():
        print("IS A NUMBER")
    else:
        print("IS NOT A NUMBER")

weight_input_button = customtkinter.CTkEntry(master=app, placeholder_text="enter your current weight")
weight_input_button.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)

weight_input_button.bind("<KeyRelease>", weight_input)


app.mainloop()

#WORKING 
#negawatt