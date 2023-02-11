import sqlite3
import tkinter

try:
    cnt=sqlite3.connect('e:/shop.db')
    print("opened database successfully!")
except:
    print("Error!")

islogin=False
#-------------------create users table-----------------------------
##query='''CREATE TABLE users
##    (ID INTEGER PRIMARY KEY,
##    user CHAR(25) NOT NULL,
##    password CHAR(25) NOT NULL,
##    addr CHAR(50) NOT NULL
##    )'''
##cnt.execute(query)
##cnt.close()

#-------------------insert date to users table----------------------

##query='''INSERT INTO users (user,password,addr)
##    VALUES ("admin","123456789","rasht")'''
##cnt.execute(query)
##cnt.commit()
##cnt.close()
#-----------------------functions----------------------------
def login():
    global user
    global pas
    global islogin
    user=txt_user.get()
    pas=txt_pass.get()
    
    if(len(user)==0):
        lbl_msg.configure(text="please fill the blank",fg="red")
        return
        
    query='''SELECT id FROM  users WHERE user=? AND password=? '''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    btn_login.configure(state="disabled")
    islogin=True
    lbl_msg.configure(text="welcome to your account!",fg="green")
    btn_delete.configure(state="normal")
    btn_logout.configure(state="normal")
    
    
def submit():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    win2=tkinter.Toplevel(win)
    win2.geometry("300x300")
    
    lbl_user2=tkinter.Label(win2,text="username: ")
    lbl_user2.pack()

    txt_user2=tkinter.Entry(win2,width=15)
    txt_user2.pack()

    lbl_pass2=tkinter.Label(win2,text="password: ")
    lbl_pass2.pack()

    txt_pass2=tkinter.Entry(win2,width=15)
    txt_pass2.pack()

    lbl_addr=tkinter.Label(win2,text="address: ")
    lbl_addr.pack()

    txt_addr=tkinter.Entry(win2,width=15)
    txt_addr.pack()

    lbl_msg2=tkinter.Label(win2,text="")
    lbl_msg2.pack()

    btn_submit2=tkinter.Button(win2,text="Submit",command=submit2)
    btn_submit2.pack(pady=10)
    
    
    win2.mainloop()

def submit2():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    user2=txt_user2.get()
    pas2=txt_pass2.get()
    addr=txt_addr.get()
    query='''SELECT id FROM users WHERE user=?'''
    result=cnt.execute(query,(user2,))
    rows=result.fetchall()

    if(len(user2)==0):
        lbl_msg2.configure(text="please fill the blank",fg="red")
        return

    if(len(rows)!=0):
        lbl_msg2.configure(text="you have already have an account with this username!",fg="red")
        return
    if(len(pas2)<8):
        lbl_msg2.configure(text="password lenght should be at least  characters",fg="red")
        return
    
    query2='''INSERT INTO users(user,password,addr)
    VALUES(?,?,?)'''
    cnt.execute(query2,(user2,pas2,addr))
    cnt.commit()
    lbl_msg2.configure(text="submit done!!!",fg="green")
    
    
def delete():
    global lbl_msg5
    win3=tkinter.Toplevel(win)
    win3.geometry("300x300")
    lbl_msg=tkinter.Label(win3,text="are you sure you want to delete your account?")
    lbl_msg.pack()
    
    btn_yes=tkinter.Button(win3,text="Yes",command=yes)
    btn_yes.pack(pady=30)

    btn_no=tkinter.Button(win3,text="No",command=no)
    btn_no.pack(pady=15)

    lbl_msg5=tkinter.Label(win3,text="")
    lbl_msg5.pack()

def yes():
    global lbl_msg5
    global user
    global pas
    global islogin
    if(islogin==True):
        query='''Delete FROM users WHERE user=? AND password=?'''
        cnt.execute(query,(user,pas))
        cnt.commit()
        lbl_msg5.configure(text="your account has been deleted successfully",fg="green")
        btn_login.configure(state="normal")
        btn_delete.configure(state="disable")
        btn_logout.configure(state="disable")
def no():
    global lbl_msg5
    lbl_msg5.configure(text="activity canceled",fg="red")
    return


def logout():
    user3=txt_user.get()
    pas3=txt_pass.get()
    query='''SELECT id FROM  users WHERE user=? AND password=? '''
    result=cnt.execute(query,(user3,pas3))
    rows=result.fetchall()
    if(len(rows)!=0):
        
        btn_login.configure(state="normal")
        lbl_msg.configure(text="you logged out successuflly",fg="green")
        btn_logout.configure(state="disable")
        btn_delete.configure(state="disable")
    
    else:
        lbl_msg.configure(text="there is no account with this username and password",fg="red")

#------------------------Main---------------------------------
    
win=tkinter.Tk()
win.geometry("400x300")

lbl_user=tkinter.Label(text="username: ")
lbl_user.pack()

txt_user=tkinter.Entry(width=25)
txt_user.pack()

lbl_pass=tkinter.Label(text="password: ")
lbl_pass.pack()

txt_pass=tkinter.Entry(width=25)
txt_pass.pack()


lbl_msg=tkinter.Label(text="")
lbl_msg.pack()

btn_login=tkinter.Button(text="Login",command=login)
btn_login.pack(pady=10)

btn_submit=tkinter.Button(text="Submit",command=submit)
btn_submit.pack(pady=10)

btn_delete=tkinter.Button(text="Delete",command=delete)
btn_delete.pack(pady=10)
btn_delete.configure(state="disabled")

btn_logout=tkinter.Button(text="logout",command=logout)
btn_logout.pack(pady=10)
btn_logout.configure(state="disabled")

win.mainloop()


