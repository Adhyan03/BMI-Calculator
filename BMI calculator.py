import tkinter

root = tkinter.Tk()
# root.geometry('300x150')
root.title('BMI calculator')

#Function
def calculate_BMI():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2),2)
    lable_res['text'] = f"BMI: {bmi}"

# Creating GUI
#Weight
lable_kg = tkinter.Label(root,text = 'KG: ',width = 17,bg = '#ffff99')
lable_kg.grid(column = 0,row = 0)

entry_kg = tkinter.Entry(root,width = 24,bg = '#ffff78')
entry_kg.grid(column = 1,row = 0)
#Height
lable_h = tkinter.Label(root,text = 'HEIGHT (m): ',width = 17,bg = '#ffff99')
lable_h.grid(column = 0,row = 1)

entry_height = tkinter.Entry(root,width = 24,bg = '#ffff78')
entry_height.grid(column = 1,row = 1)

#Buttons

btn_cal = tkinter.Button(root,text = 'Calculate',command = calculate_BMI,bg = '#ffff99',width = 12)
btn_cal.grid(column = 0,row = 2)

#Result
lable_res = tkinter.Label(root,text = 'BMI: ',bg = '#ffff78')
lable_res.grid(column = 1,row = 2)




root.mainloop()