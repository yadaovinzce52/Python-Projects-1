from tkinter import *

FONT = ('Arial', 12, 'normal')
KM = 1.609344

def calculate():
    temp_to_convert = int(entry.get())
    temp_to_convert *= KM
    converted_label.config(text=f'{round(temp_to_convert)}')


window = Tk()
window.title('Mile to Km Converter')
window.minsize(height=100, width=300)
window.config(padx=50, pady=10)

# Miles Entry
entry = Entry(width=5)
entry.insert(END, string='0')
entry.grid(row=0, column=1)

# Labels
equal_label = Label(text='is equal to', font=FONT)
equal_label.grid(row=1, column=0)

miles_label = Label(text='Miles', font=FONT)
miles_label.grid(row=0, column=2)

converted_label = Label(text='0', font=FONT)
converted_label.grid(row=1, column=1)

km_label = Label(text='Km', font=FONT)
km_label.grid(row=1, column=2)

# Calculate Button
calc_button = Button(text='Calculate', command=calculate)
calc_button.grid(row=2, column=1)

window.mainloop()
