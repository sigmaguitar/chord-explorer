#import sys
#import os
#module_path=os.path.abspath("/Users/s-jak/Documents/repositories/chord-explorer/src/backend")
#sys.path.append(module_path)

import customtkinter as ctk

from scales import *

root = ctk.CTk()
root.title("Chord Explorer")
root.geometry('650x450')

ctk.set_appearance_mode("dark") # system / light / dark
ctk.set_default_color_theme("dark-blue") # dark-blue / green / blue

tabview = ctk.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)
tabview.add("Scales")

def update_dropdown():
    selected_value = combobox.get()
    user_input = my_entry.get()
    if selected_value in dropdown_map:
        output = dropdown_map[selected_value](my_entry)
        output_scales.configure(text=output)


title_scales = ctk.CTkLabel(master=tabview.tab("Scales"), text=" Explore SCALES", font=("TimesNewRoman", 18))
title_scales.pack(pady=0, padx=0)

my_entry = ctk.CTkEntry(master=tabview.tab("Scales"),placeholder_text="   Choose a KEY  ", font=("TimesNewRoman", 16))
my_entry.pack(pady=10,padx=10)

combobox = ctk.CTkComboBox(master=tabview.tab("Scales"), values=[" Major | Minor", "   Pentatonic "], font=("TimesNewRoman", 16,))
combobox.pack(pady=0, padx=0, anchor="center")

dropdown_map = {" Major | Minor": major_minor_scale , "   Pentatonic ": pentatonic}


my_button = ctk.CTkButton(master=tabview.tab("Scales"), text="Explore",command=update_dropdown,font=("TimesNewRoman", 16))
my_button.pack(pady=20)

output_scales = ctk.CTkLabel(master=tabview.tab("Scales"), text=" TEXTFIELD ", font=("Arial", 17))
output_scales.pack(side="top", pady=0)


root.mainloop()

print(sys.path)
