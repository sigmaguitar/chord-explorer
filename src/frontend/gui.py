import customtkinter as ctk
import json
import os
import sys

from backend.chords import chords
from backend.triads import triad
from src.backend.scales import *

# Load data
JSON_PATH = os.path.join('..','backend', 'data', "scales.json")

with open(JSON_PATH, 'r', encoding='utf-8') as file:
	data = json.load(file)

# Init GUI
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

# Helper Function

def input_check(input_string, tonalities, data):
    valid_inputs = []

    for tonality in tonalities:
        valid_inputs += data[tonality].keys()

    if input_string in valid_inputs:
        return input_string
    else:
        return None

# Callback functions
def update_triads():
    user_input = key_input_triads.get().strip().lower()
    user_input = input_check(user_input, ["maj", "min", "dim", "aug"], data)
    if user_input:
        root_pos, first_inv, second_inv = triad(user_input, data)
        description = (
        f"][  {' - '.join(root_pos)}  ]"
        f"[  {' - '.join(first_inv)}   ]"
        f"[  {' - '.join(second_inv)}  ]["
        )
        output_triads.configure(text=description)
    else:
        output_triads.configure(text= "Invalid Input")

def update_triads_description():
    user_input = key_input_triads.get().strip().lower()

    if user_input in data["maj"]:
        description = "][  1 - 3 - 5   ][   3 - 5 - 1   ][   5 - 3 - 1  ]["

    elif user_input in data["min"]:
        description = "][  1 - b3 - 5   ][   b3 - 5 - 1   ][   5 - b3 - 1 ]["

    elif user_input in data["dim"]:
        description = "][  1 - b3 - b5   ][   b3 - b5 - 1   ][   b5 - b3 - 1  ]["

    elif user_input in data["aug"]:
        description = "][  1 - 3 - #5   ][   3 - #5 - 1   ][   #5 - 3 - 1  ]["

    else:
        description = "Please enter: maj, min, dim, or aug"

    output_triads_build.configure(text=description)

def triads_output():
    update_triads()
    update_triads_description()

def update_dropdown():
    DROPDOWN_MAP = {" Major | Minor": major_minor_scale ,
                    " Pentatonic": pentatonic,
                    " Melodic Minor": melodic_minor_scale,
                    " Harmonic Minor": harmonic_minor_scale,
                    " Blues Scale": blues_scale}
    selected_value = dropdown_scales.get() or ""
    if selected_value in (" Major | Minor", " Pentatonic"):
        tonalities = ["maj", "min"]
    else:
        tonalities = ["min"]

    user_input = key_input_scales.get().strip().lower()
    user_input = input_check(user_input, tonalities, data)

    if user_input:
        scale_function = DROPDOWN_MAP[selected_value]
        output = scale_function(user_input, data)
        output = f"[  {' - '.join(output)}  ]"
        output_scales.configure(text=output)
    else:
        output_scales.configure(text= "Invalid Input")

    if selected_value in " Major | Minor" and user_input in data["maj"]:
        scale_description = " [ R - 2 - 3 - 4 - 5 - 6 - 7 ]"
        scale_title = f'{user_input.title()} Major Scale '
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)

    elif selected_value in " Major | Minor" and user_input in data["min"]:
        scale_description = " [ R - 2 - b3 - 4 - 5 - b6 - b7 ]"
        scale_title = f'{user_input[0].title()} Natural Minor Scale'
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)

    elif selected_value in " Pentatonic" and user_input in data["maj"]:
        scale_description = " [ R - 2 - 3 - 5 - 6 ]"
        scale_title = f'{user_input[0].title()} Major Pentatonic Scale'
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)

    elif selected_value in " Pentatonic" and user_input in data["min"]:
        scale_description = " [ R - b3 - 4 - 5 - b7 ]"
        scale_title = f'{user_input[0].title()} Minor Pentatonic Scale'
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)

    elif selected_value in " Melodic Minor" and user_input in data["min"]:
        scale_description = " [ R - 2 - b3 - 4 - 5 - 6 - 7 ]"
        output_scales_build.configure(text=scale_description)
        scale_title = f'{user_input[0].title()}  Melodic Minor Scale'
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)

    elif selected_value in " Harmonic Minor" and user_input in data["min"]:
        scale_description = " [ R - 2 - b3 - 4 - 5 - b6 - 7 ]"
        scale_title = f'{user_input[0].title()} Harmonic Minor Scale'
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)

    elif selected_value in " Blues Scale" and user_input in data["min"]:
        scale_description = " [ R - b3 - 4 - b5 - 5 - b7]"
        scale_title = f'{user_input[0].title()} Blues Scale'
        output_scales_title.configure(text=scale_title)
        output_scales_build.configure(text=scale_description)


    else:
        scale_description = " "
        output_scales_title.configure(text=scale_description)
        output_scales_build.configure(text=scale_description)






def update_chords():
    user_input = key_input_chords.get().strip().lower()
    user_input = input_check(user_input, ["maj", "min"], data)
    if user_input:
        scale, scale_with_7 = chords(user_input, data)
        scale = f"[  {' - '.join(scale)}  ]"
        output_chords1.configure(text=scale)
        scale_with_7 = f"[  {' - '.join(scale_with_7)}  ]"
        output_chords2.configure(text=scale_with_7)
    else:
        output_chords1.configure(text= "Invalid Input")
        output_chords2.configure(text= "")

def hit_enter(event):
  triads_output()
  update_dropdown()
  update_chords()

root.bind("<Return>", hit_enter)

# Triads page
title_triads = ctk.CTkLabel(master=tabview.tab("Triads"), text=" Explore Triads", font=("Arial", 18))
title_triads.pack(pady=0, padx=0)

key_input_triads = ctk.CTkEntry(master=tabview.tab("Triads"),placeholder_text="   Choose a KEY  ", font=("Arial", 17))
key_input_triads.pack(pady=10,padx=10)

explore_button_triads = ctk.CTkButton(master=tabview.tab("Triads"), text="Explore",command=triads_output,font=("TimesNewRoman", 16))
explore_button_triads.pack(pady=5)

output_triads_description = ctk.CTkLabel(master=tabview.tab("Triads"), text="    ][    ROOT   ][   FIRST   ][   SECOND    ][", font=("Arial", 18))
output_triads_description.pack(side="top", padx=10, pady=10)

output_triads_build = ctk.CTkLabel(master=tabview.tab("Triads"), text="  ", font=("Arial", 18))
output_triads_build.pack(side="top", padx=10, pady=10)

output_triads = ctk.CTkLabel(master=tabview.tab("Triads"), text="  ", font=("Arial", 18))
output_triads.pack(side="top", padx=10, pady=10)


# Scales page
title_scales = ctk.CTkLabel(master=tabview.tab("Scales"), text=" Explore Scales", font=("TimesNewRoman", 18))
title_scales.pack(pady=0, padx=0)

key_input_scales = ctk.CTkEntry(master=tabview.tab("Scales"),placeholder_text="   Choose a KEY  ", font=("TimesNewRoman", 16))
key_input_scales.pack(pady=10,padx=10)

dropdown_scales = ctk.CTkComboBox(master=tabview.tab("Scales"), values=[" Major | Minor", " Pentatonic", " Melodic Minor",
                                                                 " Harmonic Minor", " Blues Scale"], font=("TimesNewRoman", 16,))
dropdown_scales.pack(pady=0, padx=0, anchor="center")

explore_button_scales = ctk.CTkButton(master=tabview.tab("Scales"), text="Explore",command=update_dropdown,font=("TimesNewRoman", 16))
explore_button_scales.pack(pady=20)

output_scales_title = ctk.CTkLabel(master=tabview.tab("Scales"), text=" ", font=("Arial", 18))
output_scales_title.pack(side="top", padx=0)

output_scales = ctk.CTkLabel(master=tabview.tab("Scales"), text=" Please choose a scale and a key", font=("Arial", 18))
output_scales.pack(side="top", pady=0)

output_scales_build = ctk.CTkLabel(master=tabview.tab("Scales"), text="Type 'C' or 'Cm' for 'Cmajor' or 'Cminor'", font=("Arial", 18))
output_scales_build.pack(side="top", padx=0)

# Chords page
title_chords = ctk.CTkLabel(master=tabview.tab("Chords"), text=" Diatonic Chords ", font=("TimesNewRoman", 18))
title_chords.pack(pady=0, padx=0)

key_input_chords = ctk.CTkEntry(master=tabview.tab("Chords"),placeholder_text="   Choose a KEY  ", font=("TimesNewRoman", 16))
key_input_chords.pack(pady=10,padx=10)

explore_button_chords = ctk.CTkButton(master=tabview.tab("Chords"), text="Explore",command=update_chords,font=("TimesNewRoman", 16))
explore_button_chords.pack(pady=5)

output_chords1 = ctk.CTkLabel(master=tabview.tab("Chords"), text="  ", font=("TimesNewRoman", 18))
output_chords1.pack(side="top", padx=10, pady=10)


output_chords2 = ctk.CTkLabel(master=tabview.tab("Chords"), text="  ", font=("TimesNewRoman", 18))
output_chords2.pack(side="top", padx=10, pady=10)

root.mainloop()