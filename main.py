from tkinter import *
import tkinter.ttk
import http.client
import urllib

#일단 창 생성하기
window=Tk()
window.title("피바다")
window.geometry("800x600+900+700")
window.resizable(False,False)
#기본 윈도우 생성끝

#일단 기능이 2가지이니 노트북으로 창 2개 분리
notebook=tkinter.ttk.Notebook(window,width=750,height=550)
notebook.pack()
search_frame=Frame(window)
notebook.add(search_frame,text="검색")
news_frame=Frame(window)
notebook.add(news_frame,text="특보")

b1=Button(search_frame, text="(50, 50)")
b1.place(x=50, y=50)


window.mainloop()