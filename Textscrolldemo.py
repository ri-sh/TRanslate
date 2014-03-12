from Tkinter import *

def cipher():
    data = text_area.get("1.0",END)

    As,Ts,Cs,Gs, = 0,0,0,0

    for x in data:
        if 'A' == x:
            As+=1
        elif x == 'T':
            Ts+=1
        elif x =='C':
            Cs+=1
        elif x == 'G':
            Gs+=1
    result.set('Num As: '+str(As)+' Num of Ts: '+str(Ts)+' Num Cs: '+str(Cs)+' Num Gs: '+str(Gs))

window = Tk()

frame=Frame(window)
frame.pack()

text_area = Text(frame)
text_area.pack()

result = StringVar()
result.set('Num As: 0 Num of Ts: 0 Num Cs: 0 Num Gs: 0')
label=Label(window,textvariable=result)
label.pack()

button=Button(window,text="Count", command=cipher)
button.pack()

window.mainloop()
