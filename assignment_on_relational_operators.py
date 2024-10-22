score=85
if(score>=90):
    print("your grade is A")
elif(score>=80 and score<90):
    print("your grade is B")
elif(score>=70 and score<80):
    print("your grade is C")
elif(score>=60 and score<70):
    print("your grade is D")
elif(score<60):
    print("your grade is E")

#with tkinter
from tkinter import*
from tkinter import messagebox



window=Tk()
window.config(bg="blue")
window.geometry("200x250")

def grad():
    score=int(e1.get())
    if score >= 90:
        print("your grade is A")
    elif score >= 80 and score < 90:
        print("your grade is B")
    elif score >= 70 and score < 80:
        print("your grad is C")
    elif score >= 60 and score < 70:
        print("your grad is D")
    else:
        print("your grad is E")
    messagebox.showinfo("grad",grad)


l1=Label(window,text="ENTER THE SCORE:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)
'''l2=Label(window,text="Enter the HEIGHT:")
l2.grid(row=1,column=0)
e2=Entry(window)
e2.grid(row=1,column=1)'''

b1=Button(window,text="grad",command=grad)
b1.grid(row=2,column=0)
'''b2=Button(window,text="Perimeter")
b2.grid(row=2,column=1)'''

window.mainloop()


'''write a python program to calculate a discount for a customer  based on  the purchased amount
using tkinter
conditions:
purchase>=$500: 20% discount
purchase>=200 and <$500: 10% discount
purchase<$200: NO Discount
input: text box in tkinter window
purchase=int(e1.get())'''
from tkinter import*
from tkinter import messagebox

window=Tk()
window.config(bg="blue")
window.geometry("200x200")

def discount():
    purchase=int(e1.get())
    if purchase>=500:
        messagebox.showinfo("RESULT","20 % DISCOUNT U WILL GET")
        Total_amount=purchase*0.2
    elif purchase>=200 and purchase<500:
        messagebox.showinfo("RESULT", "20 % DISCOUNT U WILL GET")
        Total_amount=purchase*0.1

    else:
        messagebox.showinfo("RESULT", "20 % DISCOUNT U WILL GET")
        Total_amount=purchase




l1=Label(window,text="ENTER THE AMOUNT:")
l1.grid(row=0,column=0)
e1=Entry(window)
e1.grid(row=0,column=1)

b1=Button(window,text="Discount",command=discount)
b1.grid(row=2,column=0)


window.mainloop()


def calculate_discount():
    try:
        purchase = float(purchase_entry.get())
        if purchase >= 500:
            discount = 0.20  # 20% discount
        elif purchase >= 200:
            discount = 0.10  # 10% discount
        else:
            discount = 0.0  # No discount

        discount_amount = purchase * discount
        final_amount = purchase - discount_amount

        messagebox.showinfo("Discount Result", f"Discount: ${discount_amount:.2f}\nFinal Amount: ${final_amount:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid purchase amount.")

root = Tk.tk()
root.title("Discount Calculator")

Tk.Label(root, text="Enter Purchase Amount:").pack(pady=10)

purchase_entry = Tk.Entry(root)
purchase_entry.pack(pady=10)

calculate_button = Tk.Button(root, text="Calculate Discount", command=calculate_discount)
calculate_button.pack(pady=20)
root.mainloop()

