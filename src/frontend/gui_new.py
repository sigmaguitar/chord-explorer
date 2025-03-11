import customtkinter as ctk
import json
import os
import sys

from backend.chords import chords
from backend.triads import triad

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, '..','backend', 'data', "scales.json")

with open(json_path, 'r', encoding='utf-8') as file:
     data = json.load(file)

module_path=os.path.abspath("/Users/s-jak/Documents/repositories/chord-explorer/src/backend")
sys.path.append(module_path)

from scales import *

root = ctk.CTk()
root.title("Chord Explorer")
root.geometry('650x450')

ctk.set_appearance_mode("dark") # system / light / dark
ctk.set_default_color_theme("dark-blue") # dark-blue / green / blue

tabview = ctk.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)
tabview.add("Triads")
tabview.add("Scales")
tabview.add("Chords")


def update_triads():
    user_input = my_entry_triads.get()
    output = triad(user_input, data)
    output_triads.configure(text=output)

def update_dropdown():
    selected_value = combobox.get()
    user_input = my_entry.get()
    if selected_value in dropdown_map:
        output = dropdown_map[selected_value](user_input, data)
        output_scales.configure(text=output)

def update_chords():
    user_input = my_entry_chords.get()
    output1, output2 = chords(user_input, data)
    output_chords.configure(text=output1)
    output_chords2.configure(text=output2)



title_scales = ctk.CTkLabel(master=tabview.tab("Scales"), text=" Explore Scales", font=("TimesNewRoman", 18))
title_scales.pack(pady=0, padx=0)

title_triads = ctk.CTkLabel(master=tabview.tab("Triads"), text=" Explore Triads", font=("TimesNewRoman", 18))
title_triads.pack(pady=0, padx=0)

title_chords = ctk.CTkLabel(master=tabview.tab("Chords"), text=" Explore Chords ", font=("TimesNewRoman", 18))
title_chords.pack(pady=0, padx=0)


my_entry = ctk.CTkEntry(master=tabview.tab("Scales"),placeholder_text="   Choose a KEY  ", font=("TimesNewRoman", 16))
my_entry.pack(pady=10,padx=10)

my_entry_triads = ctk.CTkEntry(master=tabview.tab("Triads"),placeholder_text="   Choose a KEY  ", font=("TimesNewRoman", 16))
my_entry_triads.pack(pady=10,padx=10)

my_entry_chords = ctk.CTkEntry(master=tabview.tab("Chords"),placeholder_text="   Choose a KEY  ", font=("TimesNewRoman", 16))
my_entry_chords.pack(pady=10,padx=10)

combobox = ctk.CTkComboBox(master=tabview.tab("Scales"), values=[" Major | Minor", " Pentatonic", " Melodic Minor",
                                                                 " Harmonic Minor", " Blues Scale"], font=("TimesNewRoman", 16,))
combobox.pack(pady=0, padx=0, anchor="center")

dropdown_map = {" Major | Minor": major_minor_scale , " Pentatonic": pentatonic, " Melodic Minor": melodic_minor_scale,
                " Harmonic Minor": harmonic_minor_scale, " Blues Scale": blues_scale}


my_button = ctk.CTkButton(master=tabview.tab("Scales"), text="Explore",command=update_dropdown,font=("TimesNewRoman", 16))
my_button.pack(pady=20)

my_button_triads = ctk.CTkButton(master=tabview.tab("Triads"), text="Explore",command=update_triads,font=("TimesNewRoman", 16))
my_button_triads.pack(pady=5)

my_button_chords = ctk.CTkButton(master=tabview.tab("Chords"), text="Explore",command=update_chords,font=("TimesNewRoman", 16))
my_button_chords.pack(pady=5)


output_scales = ctk.CTkLabel(master=tabview.tab("Scales"), text="  ", font=("Arial", 17))
output_scales.pack(side="top", pady=0)

output_triads = ctk.CTkLabel(master=tabview.tab("Triads"), text=" TRIADS ", font=("Arial", 17))
output_triads.pack(side="top", padx=10, pady=10)

output_chords = ctk.CTkLabel(master=tabview.tab("Chords"), text="  ", font=("Arial", 17))
output_chords.pack(side="top", padx=10, pady=10)

output_chords2 = ctk.CTkLabel(master=tabview.tab("Chords"), text="  ", font=("Arial", 17))
output_chords2.pack(side="top", padx=10, pady=10)

root.mainloop()

print(sys.path)
