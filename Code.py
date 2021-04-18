from tkinter import *
import datetime
from tkinter import messagebox
import mysql.connector #new
import random


mydb = mysql.connector.connect(host="localhost",user="root",passwd="Vrushit123",database='sql_restaurants')#new
mycursor = mydb.cursor()#new

root = Tk()
root.title("Zomato")
root.attributes('-fullscreen', True)
#root.minsize(1536,864)
img = PhotoImage(file=r"ZomatoWall.png")
img = img.subsample(1, 1)
background=Label(root,image=img,bd=0)
background.pack(fill='both',expand=True)
background.image=img

user_id=""
next_page_no=0
def exiticon():
    root.destroy()
exit=PhotoImage(file=r"exitnew.png")
exitbutton = Button(root,image=exit,command=exiticon,relief=FLAT,bg="#CB202D",bd=0,cursor="hand2")
exitbutton.place(x=1490,y=40)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    root1 = Toplevel()
    root1.resizable(width=FALSE, height=FALSE)
    root1.attributes('-fullscreen', True)
    root1.title("Zomato")
    root1.geometry('1900x1030+0+0')
    img1 = PhotoImage(file=r"ZomatoWall.png")
    img1 = img1.subsample(1, 1)
    background1 = Label(root1, image=img1, bd=0)
    background1.image = img1
    background1.pack(fill='both', expand=True)
    background1.image = img1

    def exiticon1():
        root1.destroy()


    exit = PhotoImage(file=r"exitnew.png")
    exitbutton = Button(root, image=exit, command=exiticon1, relief=FLAT, bg="#CB202D", bd=0,cursor="hand2")
    exitbutton.place(x=1490, y=40)
    login_button = Button(root1, text="Login", command=Login, width=15, height=2, bg="White", bd=4,cursor="hand2")
    login_button.place(x=633, y=550)
    signup_button = Button(root1, text="Sign Up", command=Sign_Up, width=15, height=2, bg="White", bd=4,cursor="hand2")
    signup_button.place(x=768, y=550)
    x = datetime.datetime.now()
    Label(root1, text=x.strftime("%H : %M "), relief=FLAT, bg="#CB202D", font='18').place(x=1410, y=740)
    Label(root1, text=x.strftime("%d  %B  %Y"), relief=FLAT, bg="#CB202D", font='18').place(x=1360, y=762)
    root1.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def profile1():
    profile = Toplevel()
    profile.title("Profile")
    profile.resizable(False, False)
    profile.geometry("400x700+970+70")

    global user_id
    mycursor_p = mydb.cursor()
    sql = "SELECT * FROM profile WHERE user_name = %s"
    p = (user_id,)
    mycursor_p.execute(sql,p)
    details = mycursor_p.fetchall()


    for phno,eid,prof,dob,gen,gold,age1,passw,zc,Gold_duration in details:
        if gen == 'F' and gold == 'N':
            pic = PhotoImage(file=r"profile_fn.png")
            background_profile = Label(profile, image=pic, bd=0)
            background_profile.pack(fill='both', expand=True)
        if gen == 'F' and gold == 'Y':
            pic = PhotoImage(file=r"profile_fg.png")
            background_profile = Label(profile, image=pic, bd=0)
            background_profile.pack(fill='both', expand=True)
        if gen == 'M' and gold == 'N':
            pic = PhotoImage(file=r"profile_mn.png")
            background_profile = Label(profile, image=pic, bd=0)
            background_profile.pack(fill='both', expand=True)
        if gen == 'M' and gold == 'Y':
            pic = PhotoImage(file=r"profile_mg.png")
            background_profile = Label(profile, image=pic, bd=0)
            background_profile.pack(fill='both', expand=True)

        Label(profile, text=prof, font="ErasLightITC 16", bg="#ff3347").place(x=190, y=318)
        Label(profile, text=eid, font="ErasLightITC 16", bg="#ff3347").place(x=165,y=368)
        Label(profile, text=phno, font="ErasLightITC 16", bg="#ff3347").place(x=230, y=420)
        Label(profile, text=dob, font="ErasLightITC 16", bg="#ff3347").place(x=230,y=471)
    def logout1():
        answer = messagebox.askquestion("LOGOUT", "Are You Sure?",icon='warning')
        if answer == 'yes':
            root.destroy()
        else:
            Main_Page1()
    logout=Button(profile,text="Logout",font="ErasLightITC 16 bold",relief=FLAT,bg="#f21e2c",cursor="hand2",command= logout1)
    logout.place(x=85,y=548)
    profile.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Main_Page1():

    # Login.withdraw()
    main_page = Toplevel(root)
    main_page.title("ZOMATO")
    main_page.geometry('1900x1030+0+0')
    main_page.resizable(width=FALSE, height=FALSE)
    main_page.attributes('-fullscreen', True)
    menubar = Menu(main_page)
    top = Frame(main_page)
    top.pack()
    left = Frame(main_page)
    left.pack(side="left")
    right = Frame(main_page)
    right.pack(side="right")

    def join_gold():
        gold = Toplevel()
        gold.title("ZOMATO GOLD")
        gold.geometry("342x654+590+100")
        gold.configure(bg="#CB202D")
        gold.resizable(width=FALSE, height=FALSE)
        zomatogold = PhotoImage(file=r"zomatogold.png")
        background = Label(gold, image=zomatogold, bd=0)
        background.pack(fill='both', expand=True)
        background.image = zomatogold

        global user_id
        mycursor_p = mydb.cursor()
        sql = "SELECT * FROM profile WHERE user_name = %s"
        p = (user_id,)
        mycursor_p.execute(sql, p)
        details = mycursor_p.fetchall()
        if details[0][5] == 'Y' :
            gold.destroy()
            main_page.destroy()
            messagebox.showinfo(title="Gold Membership", message="You are already a Gold Member")
            Main_Page1()
            return

        Label(gold, text="Select Your Membership", bg="White", font=12).place(x=50, y=420)
        Label(gold, text="*payment by ZomatoCASH", bg="White").place(x=180, y=625)

        def areyousure12():

            areyousure = Toplevel()
            areyousure.title("")
            areyousure.config(bg="#CB202D")
            areyousure.geometry("250x90+650+350")

            def yes():
                global user_id
                mycursor_p = mydb.cursor()
                sql = "Update profile SET Gold_Member='Y',Gold_Duration='12' WHERE user_name = %s"
                p = (user_id,)
                mycursor_p.execute(sql, p)

                mydb.commit()
                areyousure.destroy()
                gold.destroy()

            Label(areyousure, text="Are You Sure?", font=12, bg="#CB202D").place(x=55, y=10)
            Button(areyousure, text="YES", bd=4, height=1, width=10,command=yes).place(x=40, y=45)
            Button(areyousure, text="NO", bd=4, height=1, width=10,command=lambda : areyousure.destroy()).place(x=130, y=45)
            areyousure.mainloop()

        def areyousure6():
            areyousure = Toplevel()
            areyousure.title("")
            areyousure.config(bg="#CB202D")
            areyousure.geometry("250x90+650+350")

            def yes():
                global user_id
                mycursor_p = mydb.cursor()
                sql = "Update profile SET Gold_Member='Y',Gold_Duration='12' WHERE user_name = %s"
                p = (user_id,)
                mycursor_p.execute(sql, p)

                mydb.commit()
                areyousure.destroy()
                gold.destroy()

            Label(areyousure, text="Are You Sure?", font=12, bg="#CB202D").place(x=55, y=10)
            Button(areyousure, text="YES", bd=4, height=1, width=10, command=yes).place(x=40, y=45)
            Button(areyousure, text="NO", bd=4, height=1, width=10, command=lambda: areyousure.destroy()).place(x=130,y=45)
            areyousure.mainloop()

        Button(gold, text="12\nmonths\n\nRs.1800", bg="White", height=4, width=10, fg="#cc9900", font='bold', bd=3,command=areyousure12, cursor="hand2").place(x=28, y=460)
        Button(gold, text="6\nmonths\n\nRs.999", bg="White", height=4, width=10, fg="#cc9900", font='bold', bd=3,command=areyousure6, cursor="hand2").place(x=178, y=460)


        gold.mainloop()

    def canvas_call(frame_1,x):
        canvas = Canvas(frame_1, width=600, height=250, bd=2, relief="groove", bg='White')
        canvas.pack(anchor=W, padx=80)
        reg_no=x[0]

        menu_no = x[10]


        mycursor_p = mydb.cursor()
        sql = "SELECT Cuisine_name FROM cuisine natural join rest_cusine WHERE Menu_No = %s"
        p = (menu_no,)
        mycursor_p.execute(sql, p)
        details = mycursor_p.fetchall()
        cuisine=str("")
        for y in details:
            cuisine += y[0] + "   "


        food_text = "CASUAL DINING"
        if x[9] == 'Y':
            bar_text = "BAR"
        else:
            bar_text = ""


        dine_text = food_text + " , " + bar_text
        dine = Label(canvas, text=dine_text, bg="White", fg="#E7B000", font="SegoeUI 9")
        dine.place(x=25, y=7)

        name_text = x[1]
        name = Label(canvas, text=name_text, bg="White", fg="#CB202D", font="SegoeUI 22 bold")
        name.place(x=25, y=25)

        address_text = x[2]
        address = Label(canvas, text=address_text, bg="White", font="SegoeUI 10", fg="#636363")
        address.place(x=25, y=65)

        canvas.create_line(15, 95, 585, 95)

        cusine1 = Label(canvas, text="CUISINES : ", bg="White", fg="#636363")
        cusine1.place(x=25, y=100)

        cusine_text = cuisine
        cusine2 = Label(canvas, text=cusine_text, bg="White")
        cusine2.place(x=200, y=100)

        cost4two = Label(canvas, text="COST FOR TWO : ", bg="White", fg="#636363")
        cost4two.place(x=25, y=120)

        cost_text = x[4]
        cost = Label(canvas, text=cost_text, bg="White")
        cost.place(x=200, y=120)

        # if gold available then print gold is there otherwise gold is not available

        gold = Label(canvas, text="GOLD : ", bg="White", fg="#636363")
        gold.place(x=25, y=160)

        goldyn = x[8]
        if goldyn == 'N':
            gold_text = "        Not Available"
        else:
            gold_text = "Available --> 2+2 on Food\n                         --> 1+1 on Beverages"

        gold_dis = Label(canvas, text=gold_text, bg="White", fg="#24A604")
        gold_dis.place(x=175, y=160)

        valet1 = Label(canvas, text="VALET : ", bg="White", fg="#636363")
        valet1.place(x=25, y=140)

        valetyn = x[5]
        if valetyn == 'N':
            valet_text = "No"
        else:
            valet_text = "Yes"

        valet2 = Label(canvas, text=valet_text, bg="White")
        valet2.place(x=200, y=140)

        takes_order = x[7]
        table_booking = 'Y'

        def bookatable():

            booktable = Toplevel(root)
            booktable.title("Book A Table")
            booktable.geometry("380x800+120+20")
            booktable.resizable(width=False, height=False)
            img = PhotoImage(file=r"bookatable1.png")
            background = Label(booktable, image=img, bd=0)
            background.pack(fill='both', expand=True)
            background.image = img
            Label(booktable, text="What Day?", font=8, bg="#e82a2c").place(x=15, y=180)
            datevar = IntVar()
            datevar.set(1)
            x = datetime.datetime.now()
            date1 = Radiobutton(booktable, text=x.strftime("%d  %B"), relief=FLAT, bg="#e82a2c", variable=datevar,
                                value=1).place(x=15, y=215)
            y = x + datetime.timedelta(days=1)
            date2 = Radiobutton(booktable, text=y.strftime("%d  %B"), relief=FLAT, bg="#e82a2c", variable=datevar,
                                value=2).place(x=100, y=215)
            person = StringVar()
            person.set("2")
            Label(booktable, text="How Many People?", font=8, bg="#e82a2c").place(x=15, y=260)
            oneperson = Radiobutton(booktable, text="1", variable=person, value="1", bg="#e82a2c")
            oneperson.place(x=15, y=295)
            twoperson = Radiobutton(booktable, text="2", variable=person, value="2", bg="#e82a2c")
            twoperson.place(x=65, y=295)
            threeperson = Radiobutton(booktable, text="3", variable=person, value="3", bg="#e82a2c")
            threeperson.place(x=115, y=295)
            fourperson = Radiobutton(booktable, text="4", variable=person, value="4", bg="#e82a2c")
            fourperson.place(x=165, y=295)
            fiveperson = Radiobutton(booktable, text="5", variable=person, value="5", bg="#e82a2c")
            fiveperson.place(x=215, y=295)
            sixperson = Radiobutton(booktable, text="6", variable=person, value="6", bg="#e82a2c")
            sixperson.place(x=265, y=295)
            sevenperson = Radiobutton(booktable, text="7+", variable=person, value="7+", bg="#e82a2c")
            sevenperson.place(x=315, y=295)
            Label(booktable, text="What Time?", font=8, bg="#e82a2c").place(x=15, y=330)
            TimeList = ["12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00",
                        "22:00"]
            timedropdown = StringVar(booktable)
            timedropdown.set(TimeList[10])
            time = OptionMenu(booktable, timedropdown, *TimeList)
            time.place(x=15, y=370)

            global user_id
            mycursor_p = mydb.cursor()
            sql = "SELECT * FROM profile WHERE user_name = %s"
            p = (user_id,)
            mycursor_p.execute(sql, p)
            details = mycursor_p.fetchall()
            for phno, eid, prof, dob, gen, gold, age1, passw,zc,duration in details:
                name = prof
                phno = phno
                mailid = eid


            Label(booktable, text="Personal Details", font=8, bg="#e82a2c").place(x=175, y=330)
            Label(booktable, text=name, bg="#e82a2c").place(x=175, y=370)
            Label(booktable, text=phno, bg="#e82a2c").place(x=175, y=390)
            Label(booktable, text=mailid, bg="#e82a2c").place(x=175, y=410)


            def areyousure():
                areyousure = Toplevel()
                areyousure.title("")
                areyousure.config(bg="#CB202D")
                areyousure.geometry("250x90+650+350")

                def yes():

                    global user_id
                    mycursor_p = mydb.cursor()

                    if datevar.get() == 1:
                        da_te = x.strftime("%d  %B")

                    if datevar.get() == 2:
                        da_te = y.strftime("%d  %B")

                    np=person.get()
                    ti_me=timedropdown.get()


                    insert = "Insert into table_booking(Date,phone_no,email_id,No_person,Time,name) values(%s,%s,%s,%s,%s,%s)"
                    cuisine1 = [(da_te,phno,mailid,np,ti_me,name_text),]
                    mycursor_p.executemany(insert, cuisine1)
                    mydb.commit()


                    areyousure.destroy()
                    booktable.destroy()

                Label(areyousure, text="Are You Sure?", font=12, bg="#CB202D").place(x=55, y=10)
                Button(areyousure, text="YES", bd=4, height=1, width=10, command=yes).place(x=40, y=45)
                Button(areyousure, text="NO", bd=4, height=1, width=10, command=lambda: areyousure.destroy()).place(
                    x=130, y=45)
                areyousure.mainloop()


            book = Button(booktable, text="BOOK", height=2, width=15, bd=3, command=areyousure, bg="#de3051")
            book.place(x=65, y=630)

            def cancel():
                booktable.destroy()

            cancel = Button(booktable, text="CANCEL", height=2, width=15, bd=3, bg="#de3051", command=cancel)
            cancel.place(x=190, y=630)
            booktable.mainloop()

        if table_booking is 'Y':
            table_book = Button(canvas, text="Book a Table", bg="#3ABA1A", fg="White", font="SegoeUI 10 bold", width=24,
                                height=2, command=bookatable, cursor="hand2")
            table_book.place(x=200, y=210)
        else:
            table_book = Label(canvas, text=" Table Booking Is Offline", bg="#239B56", fg="White",
                               font="SegoeUI 13 bold", width=20, height=2)
            table_book.place(x=196, y=210)

        def onlineorder():
            orderrestaurant = Toplevel(root)
            orderrestaurant.title("Order Online")
            orderrestaurant.geometry("900x800+300+15")
            orderrestaurant.resizable(height=False,width=False)
            img = PhotoImage(file=r"Menu-900.png")
            background = Label(orderrestaurant, image=img, bd=0)
            background.pack(expand=True, fill='both')

            large1 = ("Trebuchet 20 underline")

            mycursor_r = mydb.cursor()
            sql = "SELECT * FROM menu_item WHERE Menu_No = %s"
            r = (menu_no,)
            mycursor_r.execute(sql, r)
            details = mycursor_r.fetchall()
            dish1 = details[0][1]
            dish2 = details[1][1]
            dish3 = details[2][1]
            dish4 = details[3][1]

            namerestaurant = Label(orderrestaurant, text=name_text, font=large1, bg="#383639", fg="White")
            namerestaurant.place(x=430, y=80)

            dish = "1. " + dish1 + "\n2. " + dish2 + "\n3. " + dish3 + "\n4. " + dish4
            foodmenu = Label(orderrestaurant, text=dish, justify=LEFT, font=12, relief=FLAT, bg="#383639", fg="White")
            foodmenu.place(x=400, y=235)

            pricemenu1 = str(details[0][2])
            pricemenu2 = str(details[1][2])
            pricemenu3 = str(details[2][2])
            pricemenu4 = str(details[3][2])

            pricemenu = pricemenu1 + "\n" + pricemenu2 + "\n" + pricemenu3 + "\n" + pricemenu4
            pricemenu = Label(orderrestaurant, text=pricemenu, font=12, justify=LEFT, fg="White", bg="#383639")
            pricemenu.place(x=820, y=235)

            bvg1 = details[4][1]
            bvg2 = details[5][1]

            bvg = "1. " + bvg1 + "\n2. " + bvg2
            beveragemenu = Label(orderrestaurant, text=bvg, justify=LEFT, font=12, bg="#383639", fg="White")
            beveragemenu.place(x=400, y=560)

            pricebvg1 = str(details[4][2])
            pricebvg2 = str(details[5][2])

            pricebvg = pricebvg1 + "\n" + pricebvg2
            beverageprice = Label(orderrestaurant, text=pricebvg, font=12, justify=LEFT, fg="White", bg="#383639")
            beverageprice.place(x=820, y=560)

            priceinrs = Label(orderrestaurant, text="*price in Rupees", bg="#383639", fg="White")
            priceinrs.place(x=750, y=710)

            quantitydish1 = Spinbox(orderrestaurant, from_=0, to=5, width=3)
            quantitydish1.place(x=750, y=240)

            quantitydish2 = Spinbox(orderrestaurant, from_=0, to=5, width=3)
            quantitydish2.place(x=750, y=265)

            quantitydish3 = Spinbox(orderrestaurant, from_=0, to=5, width=3)
            quantitydish3.place(x=750, y=290)

            quantitydish4 = Spinbox(orderrestaurant, from_=0, to=5, width=3)
            quantitydish4.place(x=750, y=315)

            quantitydish5 = Spinbox(orderrestaurant, from_=0, to=5, width=3)
            quantitydish5.place(x=750, y=565)

            quantitydish6 = Spinbox(orderrestaurant, from_=0, to=5, width=3)
            quantitydish6.place(x=750, y=590)

            def bill():
                if (int(quantitydish1.get())==0 and int(quantitydish2.get())==0 and int(quantitydish3.get())==0 and int(quantitydish4.get())==0 and int(quantitydish5.get())==0 and int(quantitydish6.get())==0):
                    Label(orderrestaurant,text="Select Quantity First",bg="#383639",fg="White").place(x=580,y=700)
                else:
                    orderrestaurant.withdraw()
                    bill = Toplevel(root)
                    bill.title("Bill")
                    bill.geometry("627x800+450+15")
                    bill.resizable(height=False,width=False)
                    img = PhotoImage(file=r"bill4.png")
                    Label(bill, image=img, bd=0).pack(fill='both', expand=True)
                    bill.image = img

                    namerestaurant = Label(bill, text=name_text, bg="White", font="SegoeUI 22 bold")
                    namerestaurant.place(x=20, y=25)
                    address = Label(bill, text=address_text, bg="White", font="SegoeUI 10")
                    address.place(x=20, y=65)
                    reg="Reg No : " + str(reg_no)
                    regno=Label(bill,text=reg,bg="White")
                    regno.place(x=20,y=85)


                    global user_id
                    mycursor_p = mydb.cursor()
                    sql = "SELECT * FROM profile WHERE user_name = %s"
                    p = (user_id,)
                    mycursor_p.execute(sql, p)
                    details = mycursor_p.fetchall()
                    for phno, eid, prof, dob, gen, gold, age1, passw,zc,gold_duration in details:
                        name = prof
                        phno = phno
                        mailid = eid

                    nameonbill = Label(bill, text=name, bg="White")
                    nameonbill.place(x=20, y=160)
                    phnoonbill = Label(bill, text=phno, bg="White")
                    phnoonbill.place(x=20, y=180)
                    mailonbill = Label(bill, text=mailid, bg="White")
                    mailonbill.place(x=20, y=200)
                    x = datetime.datetime.now()
                    Label(bill, text=x.strftime("%d  %B  "), relief=FLAT, bg="White", font='18').place(x=470, y=720)

                    qd1 = int(quantitydish1.get())
                    qd2 = int(quantitydish2.get())
                    qd3 = int(quantitydish3.get())
                    qd4 = int(quantitydish4.get())
                    qd5 = int(quantitydish5.get())
                    qd6 = int(quantitydish6.get())



                    dish1bill = Label(bill, text=dish1, bg="White")
                    dish1bill.place(x=50, y=275)
                    dishprice1bill = Label(bill, text=pricemenu1, bg="White")
                    dishprice1bill.place(x=400, y=275)
                    dishquantity1bill = Label(bill, text=qd1, bg="White")
                    dishquantity1bill.place(x=480, y=275)


                    dish2bill = Label(bill, text=dish2, bg="White")
                    dish2bill.place(x=50, y=305)
                    dishprice2bill = Label(bill, text=pricemenu2, bg="White")
                    dishprice2bill.place(x=400, y=305)
                    dishquantity2bill = Label(bill, text=qd2, bg="White")
                    dishquantity2bill.place(x=480, y=305)


                    dish3bill = Label(bill, text=dish3, bg="White")
                    dish3bill.place(x=50, y=337)
                    dishprice3bill = Label(bill, text=pricemenu3, bg="White")
                    dishprice3bill.place(x=400, y=337)
                    dishquantity3bill = Label(bill, text=qd3, bg="White")
                    dishquantity3bill.place(x=480, y=337)


                    dish4bill = Label(bill, text=dish4, bg="White")
                    dish4bill.place(x=50, y=367)
                    dishprice4bill = Label(bill, text=pricemenu4, bg="White")
                    dishprice4bill.place(x=400, y=367)
                    dishquantity4bill = Label(bill, text=qd4, bg="White")
                    dishquantity4bill.place(x=480, y=367)


                    bvg1bill = Label(bill, text=bvg1, bg="White")
                    bvg1bill.place(x=50, y=398)
                    bvg1pricebill = Label(bill, text=pricebvg1, bg="White")
                    bvg1pricebill.place(x=400, y=398)
                    bvg1quantitybill = Label(bill, text=qd5, bg="White")
                    bvg1quantitybill.place(x=480, y=398)


                    bvg2bill = Label(bill, text=bvg2, bg="White")
                    bvg2bill.place(x=50, y=429)
                    bvg2pricebill = Label(bill, text=pricebvg2, bg="White")
                    bvg2pricebill.place(x=400, y=429)
                    bvg2quantitybill = Label(bill, text=qd6, bg="White")
                    bvg2quantitybill.place(x=480, y=429)



                    totaldish1 = (qd1 * int(pricemenu1))
                    totaldish2 = (qd2 * int(pricemenu2))
                    totaldish3 = (qd3 * int(pricemenu3))
                    totaldish4 = (qd4 * int(pricemenu4))
                    totaldish5 = (qd5 * int(pricebvg1))
                    totaldish6 = (qd6 * int(pricebvg2))

                    totaldish1bill = Label(bill, text=totaldish1, bg="White")
                    totaldish1bill.place(x=545, y=275)
                    totaldish2bill = Label(bill, text=totaldish2, bg="White")
                    totaldish2bill.place(x=545, y=305)
                    totaldish3bill = Label(bill, text=totaldish3, bg="White")
                    totaldish3bill.place(x=545, y=337)
                    totaldish4bill = Label(bill, text=totaldish4, bg="White")
                    totaldish4bill.place(x=545, y=367)
                    totaldish5bill = Label(bill, text=totaldish5, bg="White")
                    totaldish5bill.place(x=545, y=398)
                    totaldish6bill = Label(bill, text=totaldish6, bg="White")
                    totaldish6bill.place(x=545, y=429)

                    finalprice = totaldish1 + totaldish2 + totaldish3 + totaldish4 + totaldish5 + totaldish6
                    Label(bill, text=finalprice, bg="White").place(x=532, y=555)

                    Label(bill, text="(TAX IS 5%)", bg="White").place(x=330, y=582)
                    taxprice = float(finalprice) * 0.05
                    output = round(taxprice, 2)
                    Label(bill, text=output, bg="White").place(x=525, y=585)

                    finalamount = finalprice + output
                    output1 = round(finalamount, 2)
                    Label(bill, text=output1, bg="White").place(x=525, y=615)

                    Label(bill, text="Select Payment Method", bg="White", font=12).place(x=20, y=590)

                    pay = StringVar()
                    pay.set("ZOMATO Cash")


                    cod=Radiobutton(bill, text="Cash On Delivery", bg="White", variable=pay, value="Cash On Delivery")
                    cod.place(x=20,y=620)
                    creditcard=Radiobutton(bill, text="Credit Card", bg="White", variable=pay, value="Credit Card")
                    creditcard.place(x=20,y=640)
                    debitcard=Radiobutton(bill, text="Debit Card", bg="White", variable=pay, value="Debit Card")
                    debitcard.place(x=20,y=660)
                    zomatocash=Radiobutton(bill, text="ZOMATO Cash", bg="White", variable=pay, value="ZOMATO Cash")
                    zomatocash.place(x=20,y=680)



                    def confirmmsgbox():
                        def areyousure():
                            areyousure = Toplevel()
                            areyousure.title("")
                            areyousure.config(bg="#CB202D")
                            areyousure.geometry("250x90+650+350")

                            def yes():
                                areyousure.destroy()

                                id="O0"+str(random.randint(1,100))
                                id="O001"

                                mycursor.execute("SELECT Order_Id FROM sql_restaurants.order")
                                ids = mycursor.fetchall()

                                for c in ids:
                                    if id in c:
                                        id="O0"+str(random.randint(1,100))


                                val1=(id,pay.get(),output1)
                                val2 = (reg_no,id)
                                val3 = (id,phno,mailid)


                                mycursor.execute("INSERT INTO sql_restaurants.order values(%s,%s,%s);",val1)

                                mycursor.execute("INSERT INTO sql_restaurants.takes_order values(%s,%s);", val2)

                                mycursor.execute("INSERT INTO sql_restaurants.place_order values(%s,%s,%s);", val3)


                                mydb.commit()

                                bill.destroy()
                            Label(areyousure, text="Are You Sure?", font=12, bg="#CB202D").place(x=55, y=10)
                            Button(areyousure, text="YES", bd=4, height=1, width=10, command=yes).place(x=40, y=45)
                            Button(areyousure, text="NO", bd=4, height=1, width=10,
                                   command=lambda: areyousure.destroy()).place(
                                x=130, y=45)
                            areyousure.mainloop()
                        areyousure()

                    confirm = Button(bill, text="Confirm", height=2, width=15, bg="White", bd=3, command=confirmmsgbox)
                    confirm.place(x=460, y=660)

                    bill.mainloop()

            place = Button(orderrestaurant, text="PLACE ORDER", fg="White", bg="#383639", width=15, height=2,
                           cursor="hand2", command=bill)
            place.place(x=580, y=650)

            orderrestaurant.mainloop()

        if takes_order is 'Y':
            order = Button(canvas, text="Order Now", bg="#3ABA1A", fg="White", font="SegoeUI 10 bold", width=24,
                           height=2, command=onlineorder, cursor="hand2")
            order.place(x=402, y=210)
        else:
            order = Label(canvas, text="Can't Take Orders", bg="#239B56", fg="White", font="SegoeUI 13 bold", width=20,
                          height=2)
            order.place(x=398, y=210)

        def menuformod():
            menurestaurant = Toplevel(root)
            menurestaurant.title("Menu")
            menurestaurant.geometry("700x700+450+65")
            menurestaurant.resizable(width=False, height=False)
            img = PhotoImage(file=r"Menu-700.png")
            img = img.subsample(1, 1)
            background1 = Label(menurestaurant, image=img, bd=0)
            background1.pack(expand=True, fill='both')
            background1.image = img
            large = ("Trebuchet 20 underline")

            mycursor_r = mydb.cursor()
            sql = "SELECT * FROM menu_item WHERE Menu_No = %s"
            r = (menu_no,)
            mycursor_r.execute(sql, r)
            details = mycursor_r.fetchall()

            dish1 = details[0][1]
            dish2 = details[1][1]
            dish3 = details[2][1]
            dish4 = details[3][1]


            namerestaurant = Label(menurestaurant, text=name_text, font=large, bg="#383639", fg="White")
            namerestaurant.place(x=387, y=51)



            dish = "1. " + dish1 + "\n2. " + dish2 + "\n3. " + dish3 + "\n4. " + dish4
            foodmenu = Label(menurestaurant, text=dish, justify=LEFT, font=12, relief=FLAT, bg="#383639", fg="White")
            foodmenu.place(x=360, y=180)

            pricemenu1 = str(details[0][2])
            pricemenu2 = str(details[1][2])
            pricemenu3 = str(details[2][2])
            pricemenu4 = str(details[3][2])


            pricemenu = pricemenu1 + "\n" + pricemenu2 + "\n" + pricemenu3 + "\n" + pricemenu4
            pricemenu = Label(menurestaurant, text=pricemenu, font=12, justify=LEFT, fg="White", bg="#383639")
            pricemenu.place(x=640, y=180)

            bvg1 = details[4][1]
            bvg2 = details[5][1]


            bvg = "1. " + bvg1 + "\n2. " + bvg2
            beveragemenu = Label(menurestaurant, text=bvg, justify=LEFT, font=12, bg="#383639", fg="White")
            beveragemenu.place(x=360, y=460)

            pricebvg1 = str(details[4][2])
            pricebvg2 = str(details[5][2])

            pricebvg = pricebvg1 + "\n" + pricebvg2
            beverageprice = Label(menurestaurant, text=pricebvg, font=12, justify=LEFT, fg="White", bg="#383639")
            beverageprice.place(x=640, y=460)


            priceinrs = Label(menurestaurant, text="*price in Rupees", bg="#383639", fg="White")
            priceinrs.place(x=600, y=580)

            menurestaurant.mainloop()

        menu = Button(canvas, text="Menu", bg="#3ABA1A", fg="White", font="SegoeUI 10 bold", width=24, height=2,
                      cursor="hand2", command=menuformod)
        menu.place(x=3, y=210)

        rating = str(x[3])
        rate_text = " " + rating + " "

        rate = Label(canvas, text=rate_text, bg="#5CEE37", bd=1, font="arial 9 ", relief=SOLID)
        rate.place(x=520, y=25)

        total_reviews = str(x[7])
        review_text = total_reviews + " Reviews"
        no_review = Label(canvas, text=review_text, bg="White", fg="Grey")
        no_review.place(x=497, y=50)

    def orderfood():
        main_page.withdraw()
        oder_f = Toplevel()
        oder_f.title("Order Online")
        oder_f.geometry('1900x1030+0+0')
        oder_f.resizable(width=FALSE, height=FALSE)
        oder_f.attributes('-fullscreen', True)
        top = Frame(oder_f)
        top.pack()

        left = Frame(oder_f)
        left.pack(side="left")

        right = Frame(oder_f)
        right.pack(side="right")

        head = PhotoImage(file=r"line.png")
        header = Label(top, image=head, border=0)
        header.pack(fill='x', expand=True)
        header.image = head

        t = ('SegoeUI', 30)
        searchentry = Entry(oder_f, width=25, font=t)
        searchentry.place(x=350, y=185)


        def search():
            search_rest = searchentry.get()
            mycursor_p = mydb.cursor()
            sql = "SELECT * FROM restaurants WHERE Name = %s and takes_order = 'Y'"
            p = (search_rest,)
            mycursor_p.execute(sql, p)
            details = mycursor_p.fetchall()

            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()

            i = 0
            list = []
            for x in details:
                if (i == 1):
                    break
                list.append(x)
                i += 1
                canvas_call(left, x)



        searchbutton = Button(oder_f, text="Search", bg="#CB202D", fg="white", width=20, height=2,font="Verdena 10 bold", border=5, relief="raised",command=search)
        searchbutton.place(x=930, y=185)


        def hommy():
            oder_f.withdraw()
            Main_Page1()


        home = Button(oder_f, text="Home", bg="#CB202D", fg="white", width=20, height=2, font="Verdena 10 bold",border=5, relief="raised",command = hommy)
        home.place(x=1135, y=185)


        order_only = "Select * from restaurants where takes_order = 'Y'"
        mycursor.execute(order_only)
        result = mycursor.fetchall()

        counter = 0
        list_order = []


        for i in range(0, 4):
            l = []
            for j in range(0, 4):
                if counter == len(result):
                    break
                l.append(result[counter])
                counter += 1
            list_order.append(l)
            if counter == len(result):
                break

        def one1():
            for widget in left.winfo_children():
                widget.destroy()
            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 0
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1

        def two2():
            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()

            count1 = 0
            i = 1
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1

        def three3():
            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 2
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1


        def four4():
            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 3
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1

        one= Button(oder_f, text="1", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=one1).place(x=680, y=800)
        two = Button(oder_f, text="2", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=two2).place(x=730, y=800)
        three = Button(oder_f, text="3", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=three3).place(x=780, y=800)
        four = Button(oder_f, text="4", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=four4).place(x=830, y=800)


        one1()

        # MenuBar ----->
        # ------------------------------------------------------------------------------------------
        menubar = Menu(oder_f)
        oder_f.config(menu=menubar)  # To config to fix it at top , ALways Have Parameter a menu=.....
        submenu = Menu(menubar)  # () conatins area where we want our sub menu like File,Edit,submenu is a name,Menu is Keyword,
        goldmenu = Menu(menubar)

        menubar.add_cascade(label='Menu', menu=submenu)  # To add Menu To the Bar use cascade keyword
        submenu.add_command(label='Order Food',command=orderfood)  # To add Items In Menu use command
        submenu.add_command(label='Zomato Gold',command=zomatogold)
        submenu.add_separator()  # add a border between open(above) and exit(below)
        submenu.add_command(label='Exit', command=lambda : oder_f.destroy())

        menubar.add_cascade(label='Gold', menu=goldmenu)  # To add File To the Bar use cascade keyword
        goldmenu.add_command(label='Join Gold',command=join_gold)

        # ------------------------------------------------------------------------------------------
    def zomatogold():

        main_page.withdraw()
        z_gold = Toplevel()
        z_gold.title("Zomato Gold")
        z_gold.geometry('1900x1030+0+0')
        z_gold.resizable(width=FALSE,height=FALSE)
        z_gold.attributes('-fullscreen', True)
        top = Frame(z_gold)
        top.pack()

        left = Frame(z_gold)
        left.pack(side="left")

        right = Frame(z_gold)
        right.pack(side="right")

        head = PhotoImage(file=r"line.png")
        header = Label(top, image=head, border=0)
        header.pack(fill='x', expand=True)
        header.image = head


        t = ('SegoeUI', 30)
        searchentry = Entry(z_gold, width=25, font=t)
        searchentry.place(x=350, y=185)


        def search():
            search_rest = searchentry.get()
            mycursor_p = mydb.cursor()
            sql = "SELECT * FROM restaurants WHERE Name = %s and Gold = 'Y'"
            p = (search_rest,)
            mycursor_p.execute(sql, p)
            details = mycursor_p.fetchall()

            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()

            i = 0
            list = []
            for x in details:
                if (i == 1):
                    break
                list.append(x)
                i += 1
                canvas_call(left, x)


        searchbutton = Button(z_gold, text="Search", bg="#CB202D", fg="white", width=20, height=2,font="Verdena 10 bold", border=5, relief="raised",command=search)
        searchbutton.place(x=930, y=185)

        def hommy():
            z_gold.withdraw()
            Main_Page1()


        home = Button(z_gold, text="Home", bg="#CB202D", fg="white", width=20, height=2, font="Verdena 10 bold",border=5, relief="raised",command = hommy)
        home.place(x=1135, y=185)


        order_only = "Select * from restaurants where Gold = 'Y'"
        mycursor.execute(order_only)
        result = mycursor.fetchall()

        counter = 0
        list_order = []


        for i in range(0, 4):
            l = []
            for j in range(0, 4):
                if counter == len(result):
                    break
                l.append(result[counter])
                counter += 1
            list_order.append(l)
            if counter == len(result):
                break



        def one1():
            for widget in left.winfo_children():
                widget.destroy()
            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 0
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1
        def two2():
            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 1
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1
        def three3():
            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 2
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1

        def four4():
            for widget in left.winfo_children():
                widget.destroy()

            for widget in right.winfo_children():
                widget.destroy()
            count1 = 0
            i = 3
            for x in list_order[i]:
                if count1 == 4:
                    break
                if count1 % 2 == 0:
                    canvas_call(left, x)
                else:
                    canvas_call(right, x)
                count1 += 1

        one= Button(z_gold, text="1", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=one1).place(x=680, y=800)
        two = Button(z_gold, text="2", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=two2).place(x=730, y=800)
        three = Button(z_gold, text="3", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=three3).place(x=780, y=800)
        four = Button(z_gold, text="4", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,command=four4).place(x=830, y=800)
        #five = Button(z_gold, text="5", bg="#CB202D", fg="white", width=2, font="Verdena 10 bold", border=5,relief=FLAT, command=five5).place(x=865, y=800)

        one1()

        # MenuBar ----->
        # ------------------------------------------------------------------------------------------
        menubar = Menu(z_gold)
        z_gold.config(menu=menubar)  # To config to fix it at top , ALways Have Parameter a menu=.....
        submenu = Menu(menubar)  # () conatins area where we want our sub menu like File,Edit,submenu is a name,Menu is Keyword,
        goldmenu = Menu(menubar)

        menubar.add_cascade(label='Menu', menu=submenu)  # To add Menu To the Bar use cascade keyword
        submenu.add_command(label='Order Food',command=orderfood)  # To add Items In Menu use command
        submenu.add_command(label='Zomato Gold',command=zomatogold)
        submenu.add_separator()  # add a border between open(above) and exit(below)
        submenu.add_command(label='Exit', command=lambda : z_gold.destroy())

        menubar.add_cascade(label='Gold', menu=goldmenu)  # To add File To the Bar use cascade keyword
        goldmenu.add_command(label='Join Gold',command=join_gold)

        # ------------------------------------------------------------------------------------------
    def enteredprofile(event):
        Label(main_page, text="View Profile").place(x=1430,y=270)

    def leftprofile(event):
        Label(main_page,text="                      ").place(x=1430,y=270)

    def enteredorder(event):
        Label(main_page, text="Online Delivering Restuarants").place(x=1060,y=270)

    def leftorder(event):
        Label(main_page,text="                                                      ").place(x=1060,y=270)

    def enteredgold(event):
        Label(main_page, text="Showing GOLD Restaurants").place(x=1230,y=270)

    def leftgold(event):
        Label(main_page,text="                                                ").place(x=1230,y=270)



    profile=PhotoImage(file=r"profile.png")
    profilebn=Button(main_page,text="Profile",width=116, height=37, image=profile,border=5, relief="raised",command=profile1,cursor="hand2",bg="#ffffff")
    profilebn.place(x=1400,y=220)
    profilebn.bind("<Enter>",enteredprofile)
    profilebn.bind("<Leave>",leftprofile)


    # MenuBar ----->
    # ------------------------------------------------------------------------------------------
    main_page.config(menu=menubar)  # To config to fix it at top , ALways Have Parameter a menu=.....
    submenu = Menu(menubar)  # () conatins area where we want our sub menu like File,Edit,submenu is a name,Menu is Keyword,
    goldmenu = Menu(menubar)
    menubar.add_cascade(label='Menu', menu=submenu)  # To add Menu To the Bar use cascade keyword
    submenu.add_command(label='Order Food',command=orderfood)  # To add Items In Menu use command
    submenu.add_command(label='Zomato Gold',command=zomatogold)
    submenu.add_separator()  # add a border between open(above) and exit(below)
    submenu.add_command(label='Exit', command= lambda : main_page.destroy())
    menubar.add_cascade(label='Gold', menu=goldmenu)  # To add File To the Bar use cascade keyword
    goldmenu.add_command(label='Join Gold',command=join_gold)
    # ------------------------------------------------------------------------------------------



    head = PhotoImage(file=r"line.png")
    header = Label(top, image=head, border=0)
    header.pack(fill='x', expand=True)
    header.image = head
    orderimg = PhotoImage(file=r"order.png")
    order = Button(main_page, text="Order Food", width=116, height=37, image=orderimg, border=5, relief="raised",cursor="hand2",command=orderfood)

    order.bind("<Enter>",enteredorder)
    order.bind("<Leave>",leftorder)

    goldimg = PhotoImage(file=r"gold.png")
    goldbuton = Button(main_page, text="Gold", width=116, height=37, image=goldimg, border=5, relief="raised",cursor="hand2",command=zomatogold)

    goldbuton.bind("<Enter>", enteredgold)
    goldbuton.bind("<Leave>", leftgold)

    t = ('SegoeUI', 30)
    e = Entry(main_page, width=25, font=t)
    e.place(x=400, y=300)

    def search():
        search_rest=e.get()
        mycursor_p = mydb.cursor()
        sql = "SELECT * FROM restaurants WHERE Name = %s"
        p = (search_rest,)
        mycursor_p.execute(sql, p)
        details = mycursor_p.fetchall()


        for widget in left.winfo_children():
            widget.destroy()

        for widget in right.winfo_children():
            widget.destroy()

        i=0
        list=[]
        for x in details:
            if(i==1):
                break
            list.append(x)
            i+=1
            canvas_call(left,x)

    def enteredsearch(event):
        Label(main_page, text="Search Restaurants").place(x=960,y=350)

    def leftsearch(event):
        Label(main_page,text="                                                ").place(x=960,y=350)

    searching = PhotoImage(file=r"search.png")
    searchbutton = Button(main_page,image=searching, bg="#CB202D", fg="white", width=50, height=37,font="Verdena 10 bold", border=5, relief="raised",cursor="hand2",command=search)
    searchbutton.bind("<Enter>", enteredsearch)
    searchbutton.bind("<Leave>", leftsearch)

    def hommy():
        main_page.destroy()
        Main_Page1()

    homepic = PhotoImage(file=r"profile.png")
    home = Button(main_page, text=homepic, width=116, height=37, image=profile, border=5, relief="raised",command=hommy, cursor="hand2", bg="#ffffff")
    home.place(x=1050, y=300)


    order.place(x=1080, y=220)
    goldbuton.place(x=1240, y=220)
    searchbutton.place(x=980, y=300)


    rest = "SELECT * FROM restaurants Order By Rating desc"
    mycursor.execute(rest)
    result = mycursor.fetchall()


    list_order=[]
    counter=0
    for i in range(0, 20):
        l = []
        for j in range(0, 2):
            if counter == len(result):
                break
            l.append(result[counter])
            counter += 1
        list_order.append(l)
        if counter == len(result):
            break



    global next_page_no
    next_page_no=-1



    def next_page():
        count = 0
        global next_page_no
        next_page_no += 1
        for widget in left.winfo_children():
            widget.destroy()

        for widget in right.winfo_children():
            widget.destroy()

        if next_page_no >= len(list_order) - 1:
            next_page_no = 0

        for x in list_order[next_page_no]:
            if count == 2:
                break
            if count % 2 == 0:
                canvas_call(left, x)
            else:
                canvas_call(right, x)
            count += 1



    def prev_page():
        count = 0
        global next_page_no
        next_page_no -= 1
        for widget in left.winfo_children():
            widget.destroy()

        for widget in right.winfo_children():
            widget.destroy()

        if next_page_no <= 0 :
            next_page_no=19
        for x in list_order[next_page_no]:
            if count == 2:
                break
            if count % 2 == 0:
                canvas_call(left, x)
            else:
                canvas_call(right, x)
            count += 1



    next_page()
    nextimg = PhotoImage(file=r"next.png")
    nextbutton= Button(main_page,image=nextimg, fg="white", width=50,height=37,border=5,relief=FLAT,command=next_page,cursor="hand2").place(x=770, y=800)
    previmg = PhotoImage(file=r"previous.png")
    prevbutton = Button(main_page,image=previmg, fg="white", width=50, height=37,border=5,relief=FLAT,command=prev_page,cursor="hand2").place(x=700, y=800)

    main_page.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Sign_Up():
    signup_window = Toplevel(root)
    signup_window.title("SIGNUP FORM")
    signup_window.geometry("1017x570+250+140")
    signup_window.configure(bg="#CB202D")
    signup_window.resizable(width=FALSE, height=FALSE)

    def previouswindowforsignup():
        signup_window.withdraw()

    def refreshbutton():
        signup_window.withdraw()
        Sign_Up()

    def enteredemail(event):
        Label(signup_window, text="EMAIL Requirements: Less Than 20 Characters, Should Have @ and .").grid(row=9,column=1)

    def leftemail(event):
        Label(signup_window,text="                                                                                                                                    ",bg="#CB202D").grid(row=9,column=1)

    def entered(event):
        Label(signup_window, text="Password Requirements: One UpperCase & LowerCase Letter &  One Digit").grid(row=3,column=2)

    def left(event):
        Label(signup_window,text="                                                                                                                                           ",bg="#CB202D").grid(row=3, column=2)

    back = PhotoImage(file=r"left-arrow.png")
    ref = PhotoImage(file=r"refresh.png")

    backbutton = Button(signup_window, image=back, command=previouswindowforsignup, relief=FLAT, bg="#CB202D", bd=0)
    backbutton.grid(row=0, padx=6)
    refresh = Button(signup_window, image=ref, command=refreshbutton, relief=FLAT, bg="#CB202D", bd=0)
    refresh.place(x=975, y=5)

    Label(signup_window, text="User ID :                                     ", bg="#CB202D", fg="White",font='6').grid(row=1, column=1, padx=55, pady=5)
    username_entry = Entry(signup_window, width=50)
    username_entry.grid(row=2, column=1, padx=50, pady=1)
    Label(signup_window, text="Email :                                        ", bg="#CB202D", fg="White",font='8').grid(row=7, column=1, padx=50, pady=5)
    email_entry = Entry(signup_window, width=50)
    email_entry.grid(row=8, column=1, padx=50, pady=1)
    email_entry.bind("<Enter>", enteredemail)
    email_entry.bind("<Leave>", leftemail)
    Label(signup_window, text="   Phone Number :                             ", bg="#CB202D", fg="White",font='8').grid(row=4, column=1, padx=50, pady=5)
    phno_entry = Entry(signup_window, width=50)
    phno_entry.grid(row=5, column=1, padx=50, pady=1)
    Label(signup_window, text="  Password :                                   ", bg="#CB202D", fg="White",font='8').grid(row=1, column=2, padx=50, pady=5)
    password_entry = Entry(signup_window, show='*', width=50)
    password_entry.grid(row=2, column=2, pady=1)
    password_entry.bind("<Enter>", entered)
    password_entry.bind("<Leave>", left)
    Label(signup_window, text="  Re-Enter Your Password :            ", bg="#CB202D", fg="White", font='8').grid(row=4,column=2,padx=50,pady=5)
    repassword_entry = Entry(signup_window, show='*', width=50)
    repassword_entry.grid(row=5, column=2, pady=1)


    gender_rb = StringVar()
    gender_rb.set("F")
    Label(signup_window, text="Gender :                                     ",bg="#CB202D",fg="White",font='8').grid(row=10, column=1, padx=50, pady=1)
    male_rb = Radiobutton(signup_window, text="M                                                                                            ", variable=gender_rb, value="M",bg="#CB202D")
    male_rb.grid(row=11, column=1, padx=50, pady=1)
    female_rb = Radiobutton(signup_window, text="F                                                                                              ", variable=gender_rb, value="F",bg="#CB202D")
    female_rb.grid(row=12, column=1, padx=50, pady=1)

    Label(signup_window, text="Date Of Birth :",bg="#CB202D",fg="White",font='8').grid(row=14, column=1, padx=50, pady=1)
    DateList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    datedropdown = StringVar(signup_window)
    datedropdown.set(DateList[0])
    date=OptionMenu(signup_window,datedropdown,*DateList)
    date.grid(row=15,column=1,padx=50,pady=1)
    MonthList=["January","February","March","April","May","June","July","August","September","October","November","December"]
    monthdropdown = StringVar(signup_window)
    monthdropdown.set(MonthList[0])
    month = OptionMenu(signup_window, monthdropdown, *MonthList)
    month.grid(row=16, column=1, padx=50, pady=1)
    YearList = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012"]
    yeardropdown = StringVar(signup_window)
    yeardropdown.set(YearList[10])
    year = OptionMenu(signup_window, yeardropdown, *YearList)
    year.grid(row=17,column=1,padx=50,pady=1)


    gold_rb=StringVar()
    gold_rb.set("YES")


    Label(signup_window, text="Want To Buy Zomato GOLD :    ",bg="#CB202D",fg="White",font='8').grid(row=10, column=2, padx=50, pady=1)
    yes_rb = Radiobutton(signup_window, text="YES                                                                                        ", variable=gold_rb, value="YES",bg="#CB202D")
    yes_rb.grid(row=11,column=2,padx=50,pady=1)
    no_rb = Radiobutton(signup_window, text="NO                                                                                         ", variable=gold_rb, value="NO",bg="#CB202D")
    no_rb.grid(row=12, column=2, padx=50, pady=1)
    empty=Label(signup_window,text="",bg="#CB2C0A")
    empty.grid(row=18,column=1)

    Label(signup_window,text="By continuing, you agree to our                                                                 ",bg="#CB202D").place(x=100,y=520)
    Label(signup_window, text="Terms of Service   Privacy Policy   Content Policy                                                          ", bg="#CB202D").place(x=60,y=540)
    Label(signup_window,text="*all fields are required",bg="#CB202D").grid(row=15,column=2)


    def Check():
        monthno = str(MonthList.index(monthdropdown.get()) + 1)
        dob1 = yeardropdown.get() + "-" + monthno + "-" + datedropdown.get()
        gender1 = gender_rb.get()
        gold1 = (gold_rb.get())[0:1]
        user = username_entry.get()
        phonenumber = phno_entry.get()
        emailid = email_entry.get()
        p1 = password_entry.get()
        p2 = repassword_entry.get()
        t = datetime.datetime.now()
        year = int(t.strftime(" %Y"))
        dyear = int(yeardropdown.get())
        age = year - dyear


        if (p1!=p2):
            Label(signup_window,text="PASSWORDS DONT MATCH !",bg="#CB202D").grid(row=6,column=2,padx=50,pady=1)
        if (len(user)==0):
            Label(signup_window,text="Enter Valid User ID",bg="#CB202D").grid(row=3,column=1)
        if (len(user)>0):
            Label(signup_window,text="                                 ",bg="#CB202D").grid(row=3,column=1)


        count = 0

        for x in phonenumber:
            if x.isdigit() is True:
                count += 1
            else:
                count = 0
                break


        if (count < 10 or count > 10):
            Label(signup_window, text="Enter A 10 Digit Phone Number", bg="#CB202D").grid(row=6, column=1)

        if (count == 10):
            Label(signup_window, text="                                                     ", bg="#CB202D").grid(row=6,column=1)

        if (len(emailid)==0) or "@" not in emailid or (len(emailid)>=20):
            Label(signup_window, text="Enter A Valid Email ID", bg="#CB202D").grid(row=9, column=1)

        if (len(emailid)>0 and "@" in emailid and (len(emailid)<20)):
            Label(signup_window, text="                                                   ", bg="#CB202D").grid(row=9, column=1)

        d = 0
        u = 0
        l = 0


        for char in p1:
            if char.isupper():
                u+=1
            if char.islower():
                l+=1
            if char.isdigit():
                d+=1


            if ((u==0 or l==0 or d==0) or (len(p1) == 0 or len(p2) == 0)):
                Label(signup_window, text="Enter A Valid Password", bg="#CB202D").grid(row=3, column=2)
            if ((u>0 and l> 0 and d>0) and (len(p1) != 0 or len(p2) != 0)):
                Label(signup_window, text="                                                   ", bg="#CB202D").grid(row=3, column=2)
            if (p1 == p2):
                Label(signup_window, text="                                                            ",bg="#CB202D").grid(row=6, column=2, padx=50, pady=1)
            if ((len(user) != 0) and count == 10 and (len(emailid) != 0) and "@" in emailid and (len(emailid)<20) and ((u>0 and l>0 and d>0) and (len(p1) != 0 or len(p2) != 0)) and p1 == p2):
                mycursor1 = mydb.cursor()
                mycursor1.execute("SELECT phone_no,email_id FROM profile")
                phno = mycursor1.fetchall()
                flag = -1


                for x,y in phno:
                    if str(phonenumber) == str(x):
                        flag = 1
                        break
                    if str(emailid) == str(y):
                        flag = 1
                        break
                if flag == -1:
                    mycursor.execute("Insert into profile() values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE user_name=%s", (phonenumber, emailid, user, dob1, gender1, gold1, age, p1,0,6,user))  # new
                    Label(signup_window, text="                                                                                 ", bg="#CB202D", font="10").grid(row=17, column=2)
                    Label(signup_window, text="New Account Created", bg="#CB202D", font="10").grid(row=17, column=2)
                    signup_window.after(2000, previouswindowforsignup)
                    mydb.commit()
                if flag != -1:
                    Label(signup_window, text="Duplicate Phone Number Or Email Id", bg="#CB202D", font="10").grid(row=17, column=2)


    signup_button=Button(signup_window, text="Submit",command=Check,bg="White",bd=3,cursor="hand2")
    signup_button.grid(row=16,column=2,padx=50,pady=1)

    x1=datetime.datetime.now()
    Label(signup_window,text=x1.strftime("  %H : %M "), relief=FLAT,bg="#CB202D",fg="White").place(x=945,y=520)
    Label(signup_window,text=x1.strftime("%d  %B  %Y"), relief=FLAT,bg="#CB202D",fg="White").place(x=920,y=540)
    signup_window.mainloop()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Login():
    login_window = Toplevel(root)
    login_window.title("LOGIN")
    login_window.geometry("400x170+100+100")
    login_window.configure(bg="#CB202D")
    login_window.resizable(width=FALSE, height=FALSE)

    Label(login_window,text="User Name : ",bg="#CB202D").place(x=80,y=25)
    user = Entry(login_window)
    user.place(x=180,y=25)
    Label(login_window, text="Password : ",bg="#CB202D").place(x=88,y=55)
    password = Entry(login_window,show='*')
    password.place(x=180,y=55)


    def previouswindowforlogin():
        login_window.withdraw()

    back1 = PhotoImage(file=r"leftarrow.png")
    backbuttonforlogin = Button(login_window, image=back1, command=previouswindowforlogin, relief=FLAT, bg="#CB202D",bd=0,cursor="hand2")
    backbuttonforlogin.grid(row=1, column=0, padx=6, pady=0)


    def test():
        p1=password.get()
        u1=user.get()

        mycursor.execute("SELECT user_name,password FROM profile")
        username = mycursor.fetchall()
        flag = 0
        for u, p in username:
            if u == u1:
                if p == p1:
                    Label(login_window, text="Logged In Successfully", bg="#CB202D").place(x=180,y=120)
                    login_window.after(2000, login_window.withdraw)
                    login_window.after(2000, Main_Page1)
                    flag = -1
                    global user_id
                    user_id = u1

        if flag == 0:
            Label(login_window, text="   Wrong Credentials   ", bg="#CB202D").place(x=180,y=120)


    submit=Button(login_window,text="Submit",command=test,cursor="hand2")
    submit.place(x=220,y=85)
    login_window.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


login_button = Button(root, text="Login", command=Login, width=15, height=2, bg="White", bd=4)
login_button.place(x=633, y=550)
signup_button = Button(root, text="Sign Up", command=Sign_Up, width=15, height=2, bg="White", bd=4)
signup_button.place(x=768, y=550)
x = datetime.datetime.now()
date = Label(root, text=x.strftime("%H : %M "), relief=FLAT, bg="#CB202D", font='18').place(x=1410, y=775)
date = Label(root, text=x.strftime("%d  %B  %Y"), relief=FLAT, bg="#CB202D", font='18').place(x=1360, y=797)


root.mainloop()


