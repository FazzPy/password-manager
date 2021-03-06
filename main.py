#MIT License

#Copyright (c) 2022 Fazz

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from tkinter import *
import string
from random import *
import smtplib
from email.message import EmailMessage

characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(7, 32)))

root = Tk()
root.geometry("700x500+500+150")
root.title("FazzTech | Password Manager")
root.iconbitmap("key.ico")
root.resizable(width=False, height=False)

sifre = "sifre"

list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

mailpassw =  "".join(choice(list1) for x in range(randint(6, 9)))
msg = EmailMessage()
msg.set_content(mailpassw)
msg['Subject'] = 'Two Factor'
msg['From'] = "E-Mail"
msg['To'] = "E-Mail"
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("E-Mail", "Password")
server.send_message(msg)
server.quit()

def sifremiUnuttum():
    msg = EmailMessage()
    msg.set_content(sifre)

    msg['Subject'] = 'Şifreniz :'
    msg['From'] = "E-Mail"
    msg['To'] = "E-Mail"


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("E-Mail", "password")
    server.send_message(msg)
    server.quit()
    giris1["text"] = "Şifre Gönderildi!"


def sifreolustur():
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(7, 32)))
    
    yazi1 = Label(text="Şifre Oluşturucu", font="Arial 12", bg="gray")
    yazi1.place(x=360, y=30)

    v = StringVar(value=password)
    sifre_olusturucu = Entry(textvariable=v, font="Arial 14",state="readonly")
    sifre_olusturucu.place(x=360, y=60)


def giris():
    if giris2.get() == sifre and giris5.get() == mailpassw:
        giris1.destroy()
        giris2.destroy()
        giris3.destroy()
        label1.destroy()
        giris4.destroy()
        giris5.destroy()
        label2.destroy()

        discord = Label(text="Discord : ", font="Arial 14")
        discord.place(x=20, y=10)

        discord_password = "discordpassword"
        discord_password_v = StringVar(value=discord_password)
        discordent = Entry(font="Verdana 12", state="readonly", textvariable=discord_password_v)
        discordent.place(x=100, y=15)


        Instagram = Label(text="Instagram : ", font="Arial 14")
        Instagram.place(x=20, y=45)

        insta_password = "instagrampassword"
        insta_password_v = StringVar(value=insta_password)
        instaent = Entry(font="Verdana 12", state="readonly", textvariable=insta_password_v)
        instaent.place(x=120, y=50)

        spotify = Label(text="Spotify : ", font="Arial 14")
        spotify.place(x=20, y=80)

        spotify_password = "spotifypassword"
        spotify_password_v = StringVar(value=spotify_password)
        spotifyent = Entry(font="Verdana 12", state="readonly", textvariable=spotify_password_v)
        spotifyent.place(x=100, y=85)

        label5 = Label(text="Made By Fazz Tech", fg="green", font="Impact 32")
        label5.place(x=300, y=250)

        yazi1 = Label(text="Şifre Oluşturucu", font="Arial 12", bg="gray")
        yazi1.place(x=360, y=30)

        v = StringVar(value=password)
        sifre_olusturucu = Entry(textvariable=v, font="Arial 14", state="readonly")
        sifre_olusturucu.place(x=360, y=60)

        buton2 = Button(text="Şifre Oluştur", command=sifreolustur)
        buton2.place(x=360, y=90)


    else:
        giris1["text"] = "Şifre yanlış!!!"


giris1 = Label(text="Şifre Giriniz : ", font="Impact 32")
giris1.place(x=250, y=140)

giris2 = Entry(width=20, font="Arial 16", show="*",bg="lightgray")
giris2.place(x=250, y=200)
giris2.focus()

giris3 = Button(text="Giriş", bg="gray", fg="yellow", font="Verdana 18", command=giris)
giris3.place(x=330, y=260)

label1 = Label(text="Fazz Tech", fg="green", font="12")
label1.place(x=2, y=480)

giris4 = Button(text="Şifremi Unuttum", fg="red", font="Verdana 14", command=sifremiUnuttum)
giris4.place(x=280, y=330)

label2 = Label(text="Mail Adresinize gelen kodu giriniz", fg="blue")
label2.place(x=280, y=380)

giris5 = Entry(bg="lightgray", fg="white", font="Arial 16")
giris5.place(x=250, y=410)



root.mainloop()
