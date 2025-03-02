#toDo

import tkinter as tk
import customtkinter as ctk

from triads_function import *
from chords_function import chords
from scales_function import *


root = ctk.CTk()
root.title("GUI PRACTICE")
root.geometry('650x450')

ctk.set_appearance_mode("dark") # system / light / dark
ctk.set_default_color_theme("dark-blue") # dark-blue / green / blue


def update_label():
    user_input = my_entry.get()
    result = triads(user_input)
    label1.configure(text=result)

def update_label2():
    user_input2 = my_entry2.get()
    result =chords(user_input2)
    label2.configure(text=result)

def update_label3():
    user_input3 = my_entry3.get()
    result =pentatonic(user_input3)
    if user_input3 in maj:
        label4.configure(text=result)
    elif user_input3 in min:
        label3.configure(text=result)

def update_dropdown():
    selected_value = combobox.get()
    user_input4 = my_entry4.get()
    if selected_value in dropdown_map:
        output = dropdown_map[selected_value](user_input4)
        label5.configure(text=output)


#frame = ctk.CTkFrame(master= root , fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
#frame.pack(expand=True)

tabview = ctk.CTkTabview(master=root)
tabview.pack(padx=20, pady=20)

tabview.add("Triads")
tabview.add("Chords")
tabview.add("Scales")
tabview.add("Dropdown")


# heading

my_label = ctk.CTkLabel(master=tabview.tab("Triads"), text="TRIADS", font=("Arial", 20))
my_label.pack(pady=20, padx=20)

my_label2 = ctk.CTkLabel(master=tabview.tab("Chords"), text="CHORDS", font=("Arial", 20))
my_label2.pack(pady=20, padx=20)

my_label3 = ctk.CTkLabel(master=tabview.tab("Scales"), text=" PENTATONIC SCALE", font=("TimesNewRoman", 20))
my_label3.pack(pady=20, padx=20)

my_label4 = ctk.CTkLabel(master=tabview.tab("Dropdown"), text=" Major / Natural minor / Pentatonic ", font=("TimesNewRoman", 20))
my_label4.pack(pady=20, padx=20)


# textboxes

my_entry = ctk.CTkEntry(master=tabview.tab("Triads"),placeholder_text="   Key of Choice  ", font=("TimesNewRoman", 16))
my_entry.pack(pady=20,padx=10)

my_entry2 = ctk.CTkEntry(master=tabview.tab("Chords"),placeholder_text=" Your Chosen Key  ", font=("TimesNewRoman", 16))
my_entry2.pack(pady=20,padx=10)

my_entry3 = ctk.CTkEntry(master=tabview.tab("Scales"),placeholder_text=" Your Chosen Key  ", font=("TimesNewRoman", 16))
my_entry3.pack(pady=20,padx=10)

my_entry4 = ctk.CTkEntry(master=tabview.tab("Dropdown"),placeholder_text="   Chosen Key  ", font=("TimesNewRoman", 16))
my_entry4.pack(pady=0,padx=10)


# buttons

my_button = ctk.CTkButton(master=tabview.tab("Triads"), text="Explore",command=lambda:[update_label(), label_reset()], font=("TimesNewRoman", 16))
my_button.pack(pady=10)

my_button2 = ctk.CTkButton(master=tabview.tab("Chords"), text="Explore",command=update_label2, font=("TimesNewRoman", 16))
my_button2.pack(pady=10)

my_button3 = ctk.CTkButton(master=tabview.tab("Scales"), text="Explore",command=lambda:[update_label3(), label_reset()], font=("TimesNewRoman", 16))
my_button3.pack(pady=10)

my_button4 = ctk.CTkButton(master=tabview.tab("Dropdown"), text="Explore", command=update_dropdown, font=("TimesNewRoman", 16))
my_button4.pack(pady=70)


dropdown_map = {"Major / Minor Scale": major_minor_scale, "Pentatonic Scale": pentatonic}

combobox = ctk.CTkComboBox(master=tabview.tab("Dropdown"), values=["Major / Minor Scale", "Pentatonic Scale"], font=("TimesNewRoman", 14,))
combobox.place(relx=0.5, rely=0.5, anchor="center")

combobox.bind("<<ComboboxSelected>>", update_dropdown)


#reset_button = ctk.CTkButton(master=tabview.tab("Scales"), text="RESET", font=("TimesNewRoman", 16))
#reset_button.pack(pady=5)

maj_pentatonic_txt =" Major Pentatonic // 1-2-3-5-6"
min_pentatonic_txt="Minor Pentatonic // 1-b3-4-5-b7"
triads_txt ="Root Position - 1st Inversion - 2nd Inversion"

click_count = 0

def label_reset():
    global click_count
    click_count += 1
    if click_count == 2:
        label1.configure(text=triads_txt)
        label3.configure(text=maj_pentatonic_txt)
        label4.configure(text=min_pentatonic_txt)
        click_count = 0

enter_count = 0

def clear_entry(event=None):
    global enter_count
    enter_count += 1
    if enter_count == 1:
        my_entry.delete(0, tk.END)
        my_entry2.delete(0, tk.END)
        my_entry3.delete(0, tk.END)
        enter_count = 0


root.bind("<Return>", lambda event:[update_label(),update_label2(),update_label3(),clear_entry])
#root.bind("<Return>", clear_entry)

label1 = ctk.CTkLabel(master=tabview.tab("Triads"), text= triads_txt, font=("Arial", 17))
label1.pack(pady=15)

label2 = ctk.CTkLabel(master=tabview.tab("Chords"), text="Diatonic Chords", width=180, height=25,
                      corner_radius=8 ,font=("Arial", 17))
label2.pack(pady=15)

label3 = ctk.CTkLabel(master=tabview.tab("Scales"), text= maj_pentatonic_txt, font=("Arial", 17))
label3.pack(pady=10)

label4 = ctk.CTkLabel(master=tabview.tab("Scales"), text= min_pentatonic_txt, font=("Arial", 17))
label4.pack(pady=9)

label5 = ctk.CTkLabel(master=tabview.tab("Dropdown"), text=" DROPWDOWN", font=("Arial", 17))
label5.pack(side="top", pady=0)




root.mainloop()