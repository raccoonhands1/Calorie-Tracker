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




def water_formula():
    return (weight_input()/2)*29.574
 #person's weight in lbs converted to mL of water per day   


def male_tdee_formula(weight=weight_input(), height=height_input(), age=age_input(), activity_level=activity_input()):
    male_tdee=66+(6.23*weight)+(12.7*height)-(6.8*age)
    if activity_level==sedentary:
        return male_tdee*1.2
    if activity_level==lightly_active:
        return male_tdee*1.375
    if activity_level==moderately_active:
        return male_tdee*1.55
    if activity_level==very_active:
        return male_tdee*1.725
    if activity_level==extremely_active:
        return male_tdee*1.9
#should return the TDEE (total daily energy expenditure or maintenance) calories based off the male user's weight, height, age, and lifestyle

def female_tdee_formula(weight=weight_input(), height=height_input(), age=age_input(), activity_level=activity_input()):
    female_tdee=655+(4.3*weight)+(4.7*height)-(4.7*age)
    if activity_level==sedentary:
        return female_tdee*1.2
    if activity_level==lightly_active:
        return female_tdee*1.375
    if activity_level==moderately_active:
        return female_tdee*1.55
    if activity_level==very_active:
        return female_tdee*1.725
    if activity_level==extremely_active:
        return female_tdee*1.9
#should return the TDEE calories based off the female user's weight, height, age, and lifestyle

def daily_calorie_goal()


app.mainloop()

