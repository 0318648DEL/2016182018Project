from tkinter import *
from tkinter import font
import tkinter.messagebox
tk=Tk()
tk.geometry("400x600+750+200")
DataList=[]
TitleFont=font

def InitTopText():
    TempFont=font.Font(tk,size=20,weight='bold',family='Consolas')
    MainText=Label(tk,font=TempFont,text="[서울시 근린시설 검색 App]")
    MainText.pack()
    MainText.place(x=20)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar=Scrollbar(tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150,y=50)
