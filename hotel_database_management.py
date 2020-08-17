from tkinter import *
import time
import datetime
from tkinter import ttk

# ====================================Calculator Function=========================
def btn(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)
def clear():
    global operator
    operator = ''
    txt_input.set('')
    Display.insert(0,'Start Calculating............')
def Equal():
    global  operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''
# ==========================================Total function ============================
def TotalResult():
    #=====================cost of meal======================================
    varme1 =Mealdicator.get()
    varme2 = Meal1.get()
    if varme1 == 'Fried Rice':
        varme3 = (varme2*1.8)
        cost.set(varme3)
    elif varme1 == 'Fired Rice and Chicken':
        varme3 = (varme2*3)
        cost.set(varme3)
    elif varme1 == 'Burger':
        varme3 = (varme2 * 0.8)
        cost.set(varme3)
    elif varme1 == 'Butter Panner':
        varme3 = (varme2*3)
        cost.set(varme3)
    elif varme1 == 'Shaahi Panner':
        varme3 = (varme2*4)
        cost.set(varme3)
    elif varme1 == 'Fish Fry':
        varme3 = (varme2 * 4)
        cost.set(varme3)
    else:
        varme3 = (varme2 * 0)
        cost.set(varme3)
# =====================cost of Drinks======================================
    vardi1 =Drinkdicator.get()
    vardi2 = Drink1.get()
    if vardi1 == 'Bottled Water':
        vardi3 = (vardi2*0.3)
        Drinks.set(vardi3)
    elif vardi1 == 'Coca cola':
        vardi3 = (vardi2*1)
        Drinks.set(vardi3)
    elif vardi1 == 'red wine':
        vardi3 = (vardi2 * 4)
        Drinks.set(vardi3)
    elif vardi1 == 'pepsi':
        vardi3 = (vardi2*1)
        Drinks.set(vardi3)
    elif vardi1 == 'beer':
        vardi3 = (vardi2*2)
        Drinks.set(vardi3)
    else:
        vardi3 = (vardi2 * 0)
        Drinks.set(vardi3)

# ===============================Delivery Cost================================
    num1 = float(cost.get())
    num2 = float(Drinks.get())
    Delivery = (num1+num2)*0.2
# =============================Cost Of rooms=====================================
    room = v.get()
    null = 0.0
    rvip = 10.0 # Cost of VIP room
    rvip1 = Delivery/(10*0.5)# delivery cost
    rnormal = 5.0 # Cost of Normal Room
    rnormal1 = Delivery/(5*2.5)# delivery cost

    if room == 1:
        if chk1.get() == 1:
            Service_charge.set(rvip1)
            roomcost.set(rvip)
            DelCost.set(Delivery)
        else:
            Service_charge.set(null)
            roomcost.set(null)
            DelCost.set(10.0)

    elif room == 2:
        if chk1.get() == 1:
            Service_charge.set(rnormal)
            roomcost.set(5.0)
            DelCost.set(Delivery)
        else:
            Service_charge.set(null)
            roomcost.set(null)
            DelCost.set(5.0)

    elif room == 3:
        if chk1.get() == 1:
            Service_charge.set(null)
            roomcost.set(null)
            DelCost.set(null)
        else:
            Service_charge.set(null)
            roomcost.set(null)
            DelCost.set(null)

    #=====================Total Result==============================================
    num3 = round(float(DelCost.get()),2)
    num4 = round(float(roomcost.get()),2)
    num5 = round(float(Service_charge.get()),2)

    Mytotal = num1+num2+num3+num4+num5
    Total.set(Mytotal)
    FinalTotal = f"Total =  ${Mytotal}"
    num6 = Total.get()
    Display.delete(0,END)
    Display.insert(0,FinalTotal)

    if num6 <= '0.0':
        Display.delete(0,END)
        Display.insert(0,"please make an order")
def Convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2 == 'China':
        var4 = ('Yuan',(var3*6.95))
        Display.delete(0, END)
        Display.insert(0,var4)
    elif var2 == 'France':
        var4 = ('Euro',(var3*0.84))
        Display.delete(0, END)
        Display.insert(0,var4)
    elif var2 == 'Mexico':
        var4 = ('Pesos',(var3*21.97))
        Display.delete(0, END)
        Display.insert(0,var4)
    elif var2 == 'Ghanna':
        var4 = ('Cedi', (var3 * 4.98))
        Display.delete(0, END)
        Display.insert(0, var4)
    elif var2 == 'Nigeria':
        var4 = ('Nyra', (var3 * 361.01))
        Display.delete(0, END)
        Display.insert(0, var4)
    elif var2 == 'India':
        var4 = ('Rupees', (var3 * 74.85))
        Display.delete(0, END)
        Display.insert(0, var4)
    else:
        Display.delete(0,END)
        Display.insert(0,"Error Select a Country!!")
# ===================================Reset Button=================================================
def Hotel():
    Display.delete(0,END)
    Display.insert(0,"Jagdamb Hotel........")
def Powered():
    Display.delete(0,END)
    Display.insert(0,"Powered By Python....")
def Reset():
    Display.delete(0, END)
    Display.insert(0, "System Resetting......")
    Display.after(2000,Hotel)
    Display.after(4000,Powered)
    Display.after(6000,Rest)

def Rest():
    clear()
    Display.delete(0,END)
    Display.insert(0,'Hello! Welcome      ')
    Mealdicator.set(value='Delicious Meal')
    Drinkdicator.set(value='Fresh Drinks')
    indicator.set(value='Choose Country')
    txtQtofMeal.delete(0,END)
    txtQtofMeal.insert(0,0)
    txtQtofDrink.delete(0,END)
    txtQtofDrink.insert(0,0)
    txtAmount.delete(0,END)
    txtAmount.insert(0,0)
    roomcost.set(0.0)
    Total.set(0.0)
    Service_charge.set(0.0)
    Drinks.set(0.0)
    cost.set(0.0)
    chk1.set(0)
    v.set(3)
    DelCost.set(0.0)

# =====================================Clear  Button=====================================================
def ClearScreen():
    Display.delete(0,END)
    roomcost.set('')
    Total.set('')
    Service_charge.set('')
    Drinks.set('')
    cost.set('')
    DelCost.set('')

#=======================================Exit Button=======================================================
def Stop():
    root.destroy()
def Exit():
    Display.delete(0,END)
    Display.insert(0,"Thanks for Coming....")
    Display.after(3000,Stop)

root=Tk()
root.geometry('1600x800+0+0')
root.title("Hotel Management System")

# ======================================Window Partition======================
Tops = Frame(root, width=1600, height=100, bg='#25cff4', relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=400, height=800, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=800, relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root, width=1, height=800, relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root, width=400, height=800, relief=SUNKEN)
f4.pack(side=LEFT)

# =============================Main Screen========================================
txt_input = StringVar(value='Hotel Jagdamb!!!     ' )
Display = Entry(Tops, font=('arial', 85, 'bold'), fg='#000000', bd=45, bg='#f86808', justify='right',
                textvariable=txt_input)
Display.grid(columnspan=4)
# ================================Date and Time======================================
def tick():
    d = datetime.datetime.now()
    Today = '{: %B, %d, %Y}'.format(d)
    mytime = time.strftime('%I,%M,%S%p')
    txtScroll.config(text=(mytime+' '+Today))
    txtScroll.after(200,tick)


txtScroll = Label(f2,font=('arial',14,'bold'),fg='white',bd=7,bg='black',width=25)
txtScroll.grid(row=0,column=0,columnspan=4)
tick()
# ============================Row 1=====================================================
operator=''
btn7 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='7',
              command=lambda:btn(7)).grid(row=1,column=0)
btn8 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='8',
              command=lambda:btn(8)).grid(row=1,column=1)
btn9 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='9',
              command=lambda:btn(9)).grid(row=1,column=2)
btnC = Button(f2,padx=11,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='C',bg='#00ff04',
              command=clear).grid(row=1,column=3)

# ============================Row 2=====================================================
btn4 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='4',
              command=lambda:btn(4)).grid(row=2,column=0)
btn5 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='5',
              command=lambda:btn(5)).grid(row=2,column=1)
btn6 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='6',
              command=lambda:btn(6)).grid(row=2,column=2)
btnplus = Button(f2,padx=12,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='+',bg='#25cff4',
                 command=lambda:btn('+')).grid(row=2,column=3)

# ============================Row 3=====================================================
btn1 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='1',
              command=lambda:btn(1)).grid(row=3,column=0)
btn2 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='2',
              command=lambda:btn(2)).grid(row=3,column=1)
btn3 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='3',
              command=lambda:btn(3)).grid(row=3,column=2)
btnminus = Button(f2,padx=12,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='-',bg='#25cff4',
                  command=lambda:btn('-')).grid(row=3,column=3)

# ============================Row 4=====================================================
btn0 = Button(f2,padx=8,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='0',
              command=lambda:btn(0)).grid(row=4,column=0)
btndot = Button(f2,padx=15,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='.',bg='#25cff4',
                command=lambda:btn('.')).grid(row=4,column=1)
btndivision = Button(f2,padx=12,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='/',bg='#25cff4',
                     command=lambda:btn('/')).grid(row=4,column=2)
btnmultiply = Button(f2,padx=12,pady=3,bd=8,fg='black',font=('arial',20,'bold'),text='x',bg='#25cff4',
                     command=lambda:btn('*')).grid(row=4,column=3)

# ============================Row 5=====================================================
btnequls = Button(f2,padx=50,pady=2,bd=8,fg='black',font=('arial',20,'bold'),text='=',bg='#00ff04',
                  command=Equal).grid(row=5,column=0,columnspan=2)
btnopenbracket = Button(f2,padx=13,pady=2,bd=8,fg='black',font=('arial',20,'bold'),text='(',bg='#25cff4',
                        command=lambda:btn('(')).grid(row=5,column=2)
btnclosebracke = Button(f2,padx=13,pady=2,bd=8,fg='black',font=('arial',20,'bold'),text=')',bg='#25cff4',
                        command=lambda:btn(')')).grid(row=5,column=3)

# =============================================Choose Meal======================================
Meal1 = IntVar()
Mealdicator = StringVar(value='Delicious MealS')
lblMeal = Label(f1, font=('arial', 14, 'bold'), text='Choose Meal', bd=7, anchor=W)
lblMeal.grid(row=0, column=0)
txt_meal = ttk.Combobox(f1, font=('arial', 14, 'bold'), textvariable=Mealdicator)
txt_meal['values'] = ('Fired Rice ', 'Fired Rice and Chicken', 'Burger', 'Butter Panner',
                    'Shaahi Panner', 'Fish Fry')
txt_meal.grid(row=0, column=1)
lblQtofMeal = Label(f1, font=('arial',14,'bold'),text='Qty. of Meal',bd=7,anchor=W)
lblQtofMeal.grid(row=1,column=0)
txtQtofMeal = Entry(f1, font=('arial',14,'bold'),textvariable=Meal1,bd=7,insertwidth=4,bg='white',justify='right')
txtQtofMeal.grid(row=1,column=1)
# ===================================Choose Drinks====================================================
Drink1 = IntVar()
Drinkdicator = StringVar(value='Fresh Drinks')
lblDrink = Label(f1, font=('arial', 14, 'bold'), text='Choose Drinks', bd=7, anchor=W)
lblDrink.grid(row=2, column=0)
txt_Drink = ttk.Combobox(f1, font=('arial', 14, 'bold'), textvariable=Drinkdicator)
txt_Drink['values'] = ('Bottled Water', 'Coca cola', 'pepsi', 'red wine', 'beer')
txt_Drink.grid(row=2, column=1)
lblQtofDrink = Label(f1, font=('arial',14,'bold'),text='Qty. of Drinks',bd=7,anchor=W)
lblQtofDrink.grid(row=3,column=0)
txtQtofDrink = Entry(f1, font=('arial',14,'bold'),textvariable=Drink1,bd=7,insertwidth=4,bg='white',justify='right')
txtQtofDrink.grid(row=3,column=1)
# ========================================Order Delivery=====================================
chk1 = IntVar()

lblHomeDel = Label(f1, font=('arial',14,'bold'),text='Delivery',bd=7,anchor=W)
lblHomeDel.grid(row=4,column=0)
check1 = Checkbutton(f1, text='yes',variable=chk1,font=('arial',14,'bold'))
check1.grid(row=4,column=1)
# ======================================Book a Room=============================================
v=IntVar()
v.set(3)
lblroom=Label(f1, font=('arial',14,'bold'),text='Book A room',bd=7,anchor=W)
lblroom.grid(row=5,column=0)
MyRadios = Radiobutton(f1, text='VIP',font=('arial',14,'bold'),variable=v,value=1)
MyRadios.grid(row=5,column=1,sticky=W)
MyRadios = Radiobutton(f1, text='Normal',font=('arial',14,'bold'),variable=v,value=2)
MyRadios.grid(row=5,column=1)
MyRadios = Radiobutton(f1, text='No',font=('arial',14,'bold'),variable=v,value=3)
MyRadios.grid(row=5,column=1,sticky=E)
# =====================================Cost Display Screen=====================================
cost = StringVar()
lblMeal1 = Label(f1,font=('arial',12,'bold'),text='Cost of Meal($)',bd=14,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1 = Entry(f1,font=('arial',12,'bold'),textvariable=cost,fg='black',bd=7,insertwidth=2,bg='#f669cf',justify='right')
txtMeal1.grid(row=0,column=3)

Drinks = StringVar()
lblDrinks1 = Label(f1,font=('arial',12,'bold'),text='Cost of Drinks($)',bd=14,anchor=W)
lblDrinks1.grid(row=1,column=2)
txtDrinks1 = Entry(f1,font=('arial',12,'bold'),textvariable=Drinks,fg='black',bd=7,insertwidth=2,bg='#f669cf',justify='right')
txtDrinks1.grid(row=1,column=3)

DelCost = StringVar()
lblDel = Label(f1,font=('arial',12,'bold'),text='Cost of Delivery($)',bd=14,anchor=W)
lblDel.grid(row=2,column=2)
txtDel1 = Entry(f1,font=('arial',12,'bold'),textvariable=DelCost,fg='black',bd=7,insertwidth=2,bg='#f669cf',justify='right')
txtDel1.grid(row=2,column=3)

roomcost = StringVar()
lblroom1 = Label(f1,font=('arial',12,'bold'),text='Cost of Room($)',bd=14,anchor=W)
lblroom1.grid(row=3,column=2)
txtroom1 = Entry(f1,font=('arial',12,'bold'),textvariable=roomcost,fg='black',bd=7,insertwidth=4,bg='#f669cf',justify='right')
txtroom1.grid(row=3,column=3)

Service_charge = StringVar()
lblservice = Label(f1,font=('arial',12,'bold'),text='Service fee($)',bd=14,anchor=W)
lblservice.grid(row=4,column=2)
txtservice = Entry(f1,font=('arial',12,'bold'),textvariable=Service_charge,fg='black',bd=7,insertwidth=4,bg='#f669cf',justify='right')
txtservice.grid(row=4,column=3)

Total= StringVar()
lbltotal = Label(f1,font=('arial',12,'bold'),text='Total Cost ($)',bd=14,anchor=W)
lbltotal.grid(row=5,column=2)
txttotal = Entry(f1,font=('arial',12,'bold'),textvariable=Total,fg='black',bd=7,insertwidth=4,bg='#f669cf',justify='right')
txttotal.grid(row=5,column=3)
# ========================= Currency Converter=================================================================
var1 = IntVar()
indicator = StringVar(value='Choose Country')

lblCunCon = Label(f1, font=('arial',14,'bold'),text='----------------------------------------------------------Currency '
                                                    'Convertor----------------------------------------------------------'
                                                    '',bd=20,anchor=W)
lblCunCon.grid(row=6,column=0,columnspan=4)

lblCountry = Label(f1, font=('arial',11,'bold'),text='Nationality',bd=13,anchor=W)
lblCountry.grid(row=7,column=0)
txtCountry = ttk.Combobox(f1, font=('arial',11,'bold'),textvariable=indicator)
txtCountry['values']=('France','China','Mexico','Ghana','Nigeria','India')
txtCountry.grid(row=7,column=1)

lblAmount = Label(f1,font=('arial,',14,'bold'),bd=18,anchor=W)
lblAmount.grid(row=7,column=2)
txtAmount = Entry(f1, font=('arial',12,'bold'),textvariable=var1,bd=10,insertwidth=4,bg='white',justify='right')
txtAmount.grid(row=7,column=3)
# ========================================Control Buttons=============================================================
btnConvert = Button(f1, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#b463fb',width=10,text='Convert'
                    ,command=Convert)
btnConvert.grid(row=8,column=2)

btnTotal = Button(f4, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#b463fb',width=8,text='Total',
                  command=TotalResult)
btnTotal.grid(row=0,column=0)

btnScreen = Button(f4, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#55f540',width=8,text='Clear',
                   command=ClearScreen)
btnScreen.grid(row=1,column=0)

btnReset = Button(f4, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#457efb',width=8,text='Reset',
                  command=Reset)
btnReset.grid(row=2,column=0)

btnExit = Button(f4, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#ed1a1a',width=8,text='Exit',
                 command=Exit)
btnExit.grid(row=3,column=0)

btninsert = Button(f4, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#ed1a1a',width=8,text='Insert+')
btninsert.grid(row=4,column=0)

btnDelete = Button(f4, padx=4,pady=1,bd=10,fg='black',font=('arial',12,'bold'),bg='#ed1a1a',width=8,text='Delete')
btnDelete.grid(row=5,column=0)

# ===============================================Logo=====================================================
photo = PhotoImage(file='jg2.png')
myphoto = Label(f1,image=photo)
myphoto.grid(row=8,column=0)



root.mainloop()
