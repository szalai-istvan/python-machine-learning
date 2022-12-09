import tkinter

def configure(element, col, row):
    element.grid(column=col, row=row, padx=5, pady=5)
    return element

def milesToKm():
    miles = float(mileEntry.get())
    km = round(miles * 1.609, 3)
    kmEntry.config(text=f'{km}')

window = tkinter.Tk()
window.title('Miles to km converter')
window.config(width=300, height=150)

milesLabel = configure(tkinter.Label(text='Miles'), 2, 0)
kmLabel = configure(tkinter.Label(text='km'), 2, 1)
equalsToLabel = configure(tkinter.Label(text='Equals to: '), 0, 1)
mileEntry = configure(tkinter.Entry(), 1, 0)
kmEntry = configure(tkinter.Label(), 1, 1)

button = configure(tkinter.Button(text='convert', command=milesToKm), 1, 2)
window.mainloop()