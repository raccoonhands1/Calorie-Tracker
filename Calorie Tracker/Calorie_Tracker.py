from tkinter import CURRENT
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("../Calorie Tracker/Color_Scheme2.json")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("OpenCal")
app.minsize(400,200)

def water_formula(event):
    return int((float(weight_input(event)/2))*29.574)
 #person's weight in lbs converted to mL of water per day   

def weight_input(event):
    weight = weight_input_entry.get()
    if weight.isdigit():
        return int(weight)
    else:
        print("IS NOT A NUMBER")
        return 0 # Return a string to update the text box with a value

def button_press(event): #on key release event
    cw = weight_input(event) 
    if(cw == 0):
        return 0 #exit if there's not a real number
    water_formula_textbox.configure(text=str(water_formula(event)/1000) + " L of water")  # Update the text of the label

def activity_input_dropdown_callback(choice):
    activity_input_dropdown_var = choice
    print("option menu callback: " + activity_input_dropdown_var)

weight_input_entry = customtkinter.CTkEntry(master=app, placeholder_text="enter your current weight in pounds")
weight_input_entry.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)
weight_input_entry.bind("<KeyRelease>", weight_input)

water_formula_textbox = customtkinter.CTkLabel(app, text="", fg_color="transparent")
water_formula_textbox.place(relx=0.2, rely=0.2, anchor=customtkinter.CENTER)
weight_input_entry.bind("<KeyRelease>", button_press) #on key release, button press

activity_input_dropdown_var = customtkinter.StringVar(value="--LEVEL OF ACTIVITY--")
activity_input_dropdown = customtkinter.CTkOptionMenu(app, values=["sedentary", 
                                                                   "lightly active", 
                                                                   "moderately active", 
                                                                   "very active", 
                                                                   "extremely active"],
                                                     command=activity_input_dropdown_callback,
                                                     variable=activity_input_dropdown_var)
activity_input_dropdown.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

def unit_sbutton_event(value):
    unit_sbutton_var = value
    print("button toggled: " + unit_sbutton_var)

unit_sbutton_var = customtkinter.StringVar(value="ft/in")
unit_sbutton = customtkinter.CTkSegmentedButton(app, values=["ft/in","cm"], 
                                                command=unit_sbutton_event,
                                                variable=unit_sbutton_var)
unit_sbutton.set("ft/in")
unit_sbutton.place(relx=0.3, rely=0.3, anchor=customtkinter.CENTER)

def height_input_event(event):
    return 0




 
#def male_tdee_formula(weight=weight_input(), height=height_input(), age=age_input(), activity_level=activity_input()):
 #   male_tdee=66+(6.23*weight)+(12.7*height)-(6.8*age)
  #  if activity_level==sedentary:
 #       return male_tdee*1.2
 #   if activity_level==lightly_active:
  #      return male_tdee*1.375
  #  if activity_level==moderately_active:
  #      return male_tdee*1.55
  #  if activity_level==very_active:
  #      return male_tdee*1.725
  #  if activity_level==extremely_active:
 #       return male_tdee*1.9 
#should return the TDEE (total daily energy expenditure or maintenance) calories based off the male user's weight, height, age, and lifestyle

#def female_tdee_formula(weight=weight_input(), height=height_input(), age=age_input(), activity_level=activity_input()):
 #   female_tdee=655+(4.3*weight)+(4.7*height)-(4.7*age)
  #  if activity_level==sedentary:
   #     return female_tdee*1.2
  #  if activity_level==lightly_active:
   #     return female_tdee*1.375
   # if activity_level==moderately_active:
   #     return female_tdee*1.55
   # if activity_level==very_active:
   #     return female_tdee*1.725
   # if activity_level==extremely_active:
    #    return female_tdee*1.9
#should return the TDEE calories based off the female user's weight, height, age, and lifestyle



app.mainloop()

