from tkinter import *
from tkinter import ttk

c0 = '#050e22'
c1 = '#8386bc'

window = Tk()
window.title('BMI CALCULATOR')
window.geometry('295x230')
window.configure(bg=c0)

# header
header = Frame(window, width=295, height=50, bg=c0, pady=0, padx=0, relief="flat")
header.grid(row=0, column=0, sticky=NSEW)
header_title = Label(header, text="BMI Calculator", width=23, height=1, padx=0, relief="flat", anchor="center",
                     font='Ivy 16 bold', bg=c0, fg=c1)
header_title.place(x=0, y=2)
hd_line = Label(header, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font='Arial 1',
                bg=c1, fg=c1)
hd_line.place(x=0, y=35)

# calculator
calculator = Frame(window, width=295, height=200, bg=c0, pady=0, padx=0, relief="flat", )
calculator.grid(row=1, column=0, sticky=NSEW)

# weight
c_weight = Label(calculator, text="Enter your weight", height=1, padx=0, relief="flat", anchor="center",
                 font='Ivy 10 bold', bg=c0, fg=c1)
c_weight.grid(row=0, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_weight = Entry(calculator, width=5, font='Ivy 10 bold', justify='center', relief='solid')
e_weight.grid(row=0, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

# heigh
c_heigh = Label(calculator, text="Enter your heigh", height=1, padx=0, relief="flat", anchor="center",
                font='Ivy 10 bold', bg=c0, fg=c1)
c_heigh.grid(row=1, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_heigh = Entry(calculator, width=5, font='Ivy 10 bold', justify='center', relief='solid')
e_heigh.grid(row=1, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

# results
l_results = Label(calculator, width=5, text="---", height=1, padx=6, pady=12, relief="flat", anchor="center",
                  font='Ivy 24 bold', bg=c1, fg=c0)
l_results.place(x=175, y=10)
l_results_text = Label(calculator, width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center",
                       font='Ivy 10 bold', bg=c0, fg=c1)
l_results_text.place(x=0, y=85)

# button
button_c = Button(calculator, text="Calculate", width=34, height=1, overrelief='solid', bg=c1, fg=c0,
                  font='Ivy 10 bold', anchor="center", relief='raised')
button_c.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

style = ttk.Style(window)
style.theme_use("clam")


# calculating


def calculating():
    weight = float(e_weight.get())
    heigh = float(e_heigh.get()) ** 2
    results = weight / heigh

    if results < 18.6:
        l_results_text['text'] = "Your BMI is: Under weight"
    elif 18.5 <= results < 24.9:
        l_results_text['text'] = "Your BMI is: Normal"
    elif 25 <= results < 29.9:
        l_results_text['text'] = "Your BMI is: Overweight"
    elif 30 <= results < 39.9:
        l_results_text['text'] = "Your BMI is: Obesity"
    else:
        l_results_text['text'] = "Your BMI is: Severe obesity"

    l_results['text'] = "{:.{}f}".format(results, 2)


button_calc = Button(calculator, command=calculating, text="Calculate", width=34, height=1, overrelief='solid', bg=c1,
                     fg=c0, font='Ivy 10 bold', anchor="center", relief='raised')
button_calc.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)


window.mainloop()
