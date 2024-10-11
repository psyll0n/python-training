import tkinter


window = tkinter.Tk()
window.title("My First Python GUI")
window.minsize(width=500, height=300)


# Label
label = tkinter.Label(text="This is a Label", font=("Arial", 18, "bold"))

# The .pack() method, geometry management system,
# is necessary to display an element onto the Tkinter window.
label.pack()


window.mainloop()
