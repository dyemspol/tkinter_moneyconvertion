from tkinter import *
from tkinter import ttk 

windows = Tk()  
windows.title("Currency Convertion by EPOY ")
windows.geometry("490x450")

def convert():
    amount = float(entryfirst.get())
    result = 0

    dollar = 58.64  
    won_rate = 24.48  
    cny_rate = 8.06
    pab_rate = 58.64  

  
    if fromOperation.get() == 'PHP' and toOperation.get() == 'USD':
        result = amount / dollar
    elif fromOperation.get() == 'USD' and toOperation.get() == 'PHP':
        result = amount * dollar
    elif fromOperation.get() == 'PHP' and toOperation.get() == 'PAB':
        result = amount / pab_rate
    elif fromOperation.get() == 'PAB' and toOperation.get() == 'PHP':
        result = amount * pab_rate
    elif fromOperation.get() == 'PHP' and toOperation.get() == 'WON':
        result = amount * won_rate
    elif fromOperation.get() == 'WON' and toOperation.get() == 'PHP':
        result = amount / won_rate
    elif fromOperation.get() == 'PHP' and toOperation.get() == 'CNY':
        result = amount / cny_rate
    elif fromOperation.get() == 'CNY' and toOperation.get() == 'PHP':
        result = amount * cny_rate
    elif fromOperation.get() == 'USD' and toOperation.get() == 'CNY':
        result = (amount * dollar) / cny_rate
    elif fromOperation.get() == 'CNY' and toOperation.get() == 'USD':
        result = (amount * cny_rate) / dollar
    elif fromOperation.get() == 'USD' and toOperation.get() == 'WON':
        result = (amount * dollar) * won_rate
    elif fromOperation.get() == 'WON' and toOperation.get() == 'USD':
        result = (amount / won_rate) / dollar
    elif fromOperation.get() == 'USD' and toOperation.get() == 'PAB':
        result = amount  
    elif fromOperation.get() == 'PAB' and toOperation.get() == 'USD':
        result = amount  
    elif fromOperation.get() == 'PAB' and toOperation.get() == 'CNY':
        result = (amount * pab_rate) / cny_rate
    elif fromOperation.get() == 'CNY' and toOperation.get() == 'PAB':
        result = (amount * cny_rate) / pab_rate
    elif fromOperation.get() == 'PAB' and toOperation.get() == 'WON':
        result = (amount * pab_rate) * won_rate
    elif fromOperation.get() == 'WON' and toOperation.get() == 'PAB':
        result = (amount / won_rate) / pab_rate
    else:
        txtResult.set("Invalid Conversion")
        return

    txtResult.set(f"{result:.3f}")

    

def clear():
     fromOperation.set('')
     toOperation.set('')
     entryfirst.delete(0, END)  
     txtResult.set('') 

def exit():
    windows.quit()

label_title = Label(windows, text='CURRENCY CONVERTER', font=("Arial", 20), bg="#26acff",padx="200", pady="50")
label_title.pack()

fromLabel = Label(windows, text="FROM:", font=("Arial, 12"))
fromLabel.place(x=30, y=150)
fromOperation = ttk.Combobox(windows, values =('USD','PAB','WON','CNY','PHP'), font = ("Arial", 10))
fromOperation.place(x=32, y=175)
toLabel = Label(windows, text='TO:', font=("Arial, 12") )
toLabel.place(x=300, y=150)
toOperation = ttk.Combobox(windows, values =('USD','PAB','WON','CNY','PHP'), font = ("Arial", 10))
toOperation.place(x=300, y=175)


amountLabel = Label(windows, text='AMOUNT:', font=("Arial"  , 12))
amountLabel.place(x=32,y=215)
entryfirst = Entry(windows, font = " Arial ", width=14)
entryfirst.place(x=32,y=250)


txtResult = StringVar()
resultLabel = Label(windows, font=('Arial', 12), text='RESULT:').place(x=300, y=215)
result = Entry(windows, font = " Arial ", width=14, textvariable=txtResult)
result.place(x=300, y=250)
result.config(state = DISABLED)


clear_btn = Button(windows, text='Clear', padx = '10', bg= "#26acff", font=("Arial, 10"), command=clear).place(x=134,y=400)
convert_button = Button(windows, text='Convert', padx='10', bg="#26acff", font=("Arial, 10"), command=convert).place(x=195,y=400)
exit =  Button(windows, text='Exit', padx = '10', bg= "#26acff", font=("Arial, 10"), command=exit).place(x=269,y=400)
windows.mainloop()  
