from tkinter import *

window=Tk()

window.title('Simple Interest Calculator')
window.geometry("520x400")
   
def calculate():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    
    result.destroy()
    
    message=Label(result_frame,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest), bg = "grey", font=("Calibri", 12), width=60)
    message.place(x=20,y=40)
    message.pack()

app_label=Label(window, text="Simple Interest Calculator", fg = "black", font=("Calibri", 20),bd=5)
app_label.place(x=20, y=20)

principle_label=Label(window, text="Principle in Rs.", fg = "black", font=("Calibri", 12),bd=1)
principle_label.place(x=20, y=92)

principle=Entry(window, text="", bd=2, width=22)
principle.place(x=200, y=92)

rate_label=Label(window, text="Rate of Interest in %", fg = "black", font=("Calibri", 12))
rate_label.place(x=20, y=140)

rate=Entry(window, text="", bd=2, width=15)
rate.place(x=200, y=142)

time_label=Label(window, text="Time in years", fg = "black", font=("Calibri", 12))
time_label.place(x=20, y=185)

time=Entry(window, text="", bd=2, width=15)
time.place(x=200, y=187)

calculate_button=Button(window,text="Calculate",fg = "black", bg = "grey",bd=4,command=calculate)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result",  font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result=Label(result_frame,text="Your result will be displayed here :",  font=("Calibri", 12), bg = "grey", width=60)
result.place(x=20,y=20)
result.pack()

window.mainloop()