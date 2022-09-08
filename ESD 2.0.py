import sqlite3
import tkinter
from tkinter import *
from tkinter import scrolledtext
from serial import *

conn = sqlite3.connect(r'D:/my/workers.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS allworkers (
   userid TEXT PRIMARY KEY,
   name TEXT,
   flag TEXT);
    """)
conn.commit()


def clicked1():  # Команда добавления пользователя

    def adduser():
        name = [txt2.get(), txt1.get(), 'false']

        cur.execute("""INSERT INTO allworkers VALUES(?, ?, ?);""", name)
        conn.commit()
        txt1.delete(0, tkinter.END)
        txt2.delete(0, tkinter.END)
        txt1.focus()

    window = tkinter.Toplevel()
    window.title("Добавление пользователя")
    window.geometry('600x320')
    window["bg"] = "dark green"
    lbl = Label(window, text="ФИО", font=("Arial Bold", 20), bg="dark green")
    lbl.place(x=30, y=30, height="50", width="110")
    lbl = Label(window, text="QR-code", font=("Arial Bold", 20), bg="dark green")
    lbl.place(x=30, y=100, height="50", width="110")
    btn = Button(window, text="Добавить", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
                 command=adduser)
    btn.place(x=30, y=170, height="50", width="545")
    txt1 = Entry(window, width=10, font=("Arial Bold", 20))
    txt1.place(x=175, y=30, height="50", width="400")
    txt1.focus()
    txt2 = Entry(window, width=10, font=("Arial Bold", 20))
    txt2.place(x=175, y=100, height="50", width="400")
    window.mainloop()


def clicked2():  # Команда удаления пользователя
    def deluser():
        name = txt1.get()
        cur.execute(f"DELETE FROM allworkers WHERE name='{name}';")
        conn.commit()
        txt1.delete(0, tkinter.END)
        txt1.focus()

    window = tkinter.Toplevel()
    window.title("Удаление пользователя")
    window.geometry('600x200')
    window["bg"] = "dark green"
    lbl = Label(window, text="ФИО", font=("Arial Bold", 20), bg="dark green")
    lbl.place(x=30, y=30, height="50", width="110")
    btn = Button(window, text="Удалить", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
                 command=deluser)
    btn.place(x=30, y=100, height="50", width="545")
    txt1 = Entry(window, width=10, font=("Arial Bold", 20))
    txt1.place(x=175, y=30, height="50", width="400")
    txt1.focus()
    window.mainloop()


def clicked3():  # Вызов списка отметившихся пользователей
    window = tkinter.Toplevel()
    window.title("Список отметившихся")
    window.geometry('400x400')
    window["bg"] = "dark green"
    f = open('D:/my/esd.txt', 'r')
    s = f.read()
    f.close()
    txt = scrolledtext.ScrolledText(window, width=40, height=10)
    txt.place(x=30, y=30, width=340, height=340)
    txt.insert(INSERT, s)

    window.mainloop()


def clicked4():  # Запуск программы сканирования

    def okey(event):
        id = txt.get()
        cur.execute(f"""UPDATE allworkers SET flag='true' WHERE userid='{id}';""")
        conn.commit()
        cur.execute(f"""SELECT name FROM allworkers WHERE userid = '{id}';""")
        name1 = cur.fetchone()
        cur.execute(f"""SELECT flag FROM allworkers WHERE userid = '{id}';""")
        flag = cur.fetchone()

        txt.delete(0, tkinter.END)
        txt.focus()
        txt.bind('<Return>', okey)
        if 'true' in flag:
            lbl1.configure(text=(str(name1[0]) + " успешно прошел ESD-контроль."), font=("Arial Bold", 20), )
            f = open('D:/my/esd.txt', 'a')
            f.write(str(name1[0]) + '\n')
            f.close()
        else:
            window = tkinter.Toplevel()
            window.title("Результат сканирования")
            window.geometry('500x100')
            lbl = Label(window, text="Попробуйте еще раз", font=("Arial Bold", 20), bg="dark green")
            lbl.place(x=0, y=0, height="100", width="500")
        txt.delete(0, tkinter.END)
        txt.focus()

    def okey1():
        id = txt.get()
        cur.execute(f"""UPDATE allworkers SET flag='true' WHERE userid='{id}';""")
        conn.commit()
        cur.execute(f"""SELECT name FROM allworkers WHERE userid = '{id}';""")
        name1 = cur.fetchone()
        cur.execute(f"""SELECT flag FROM allworkers WHERE userid = '{id}';""")
        flag = cur.fetchone()

        txt.delete(0, tkinter.END)
        txt.focus()
        txt.bind('<Return>', okey)
        if 'true' in flag:
            lbl1.configure(text=(str(name1[0]) + " успешно прошел(a) ESD-контроль."), font=("Arial Bold", 20), )
            f = open('D:/my/esd.txt', 'a')
            f.write(str(name1[0]) + '\n')
            f.close()
        else:
            window = tkinter.Toplevel()
            window.title("Результат сканирования")
            window.geometry('500x100')
            lbl = Label(window, text="Попробуйте еще раз", font=("Arial Bold", 20), bg="dark green")
            lbl.place(x=0, y=0, height="100", width="500")
        txt.delete(0, tkinter.END)
        txt.focus()

    window = tkinter.Toplevel()
    window.title("Сканирование сотрудников")
    window.geometry('900x250')
    window["bg"] = "dark green"
    lbl1 = Label(window, text="Результат сканирования", font=("Arial Bold", 20), bg="dark green")
    lbl1.place(x=30, y=30, height="50", width="900")
    lbl = Label(window, text="QR-code", font=("Arial Bold", 20), bg="dark green")
    lbl.place(x=200, y=100, height="50", width="110")
    btn = Button(window, text="OK", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4", command=okey1)
    btn.place(x=200, y=170, height="50", width="545")
    txt = Entry(window, width=10, font=("Arial Bold", 20))
    txt.place(x=345, y=100, height="50", width="400")
    txt.bind('<Return>', okey)
    txt.focus()
    window.mainloop()


def clicked5():
    conn1 = sqlite3.connect(r'O:/SMT/ESD/workers.db')
    cur1 = conn1.cursor()
    cur1.execute("""CREATE TABLE IF NOT EXISTS allworkers (
       userid TEXT PRIMARY KEY,
       name TEXT,
       flag TEXT);
        """)
    conn1.commit()

    cur1.execute(f"""UPDATE allworkers SET flag='false' WHERE userid LIKE "user";""")
    conn1.commit()

    open('O:/SMT/ESD/esd.txt', 'w').close()


window = Tk()
window.title("ESD контроль")
window.geometry('800x800')
window["bg"] = "dark green"
btn = Button(window, text="Добавить пользователя", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
             command=clicked1)
btn.place(x=30, y=30, height="100", width="740")
btn = Button(window, text="Удалить пользователя", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
             command=clicked2)
btn.place(x=30, y=180, height="100", width="740")
btn = Button(window, text="Список отметившихся", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
             command=clicked3)
btn.place(x=30, y=330, height="100", width="740")
btn = Button(window, text="Сканирование сотрудников", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
             command=clicked4)
btn.place(x=30, y=630, height="100", width="740")
btn = Button(window, text="Очистить список", font=("Arial Bold", 20), bg="khaki", activebackground="khaki4",
             command=clicked5)
btn.place(x=30, y=480, height="100", width="740")
window.mainloop()
