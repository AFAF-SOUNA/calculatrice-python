from tkinter import *
window = Tk()
window.title('calculatrice')
window.geometry('400x300')

labelA = Label(window,text='Valeur de A: ')
labelA.grid(column=0,row=0,sticky='w')
v1= StringVar()
entreeA=Entry(window,textvariable=v1)
entreeA.grid(column=1,row=0,sticky='w')
entreeA.focus_set()

labelB = Label(window,text='Valeur de B: ')
labelB.grid(column=0,row=1,sticky='w')
v2 = StringVar()
entreeB=Entry(window,textvariable=v2)
entreeB.grid(column=1,row=1,sticky='w')
entreeB.focus_set()

def calcul(operation):
    try:
        a=float(v1.get())
        b=float(v2.get())
        resultat=0
        if operation=='+':
            resultat =a+b
        elif operation=='-':
            resultat =a-b
        elif operation=='*':
            resultat =a*b
        elif operation=='/':
            if b==0:
                v3.set("erreur division par 0")
                return
            resultat =a/b

        v3.set(str(resultat))
    except ValueError:
        v3.set("erreur : entrer les nbres")

bouton1 = Button(window,text="+",command=lambda: calcul('+'))
bouton1.grid(column=0,row=3,sticky='w')

bouton2 = Button(window,text="-",command=lambda: calcul('-'))
bouton2.grid(column=1,row=3,sticky='w')

bouton3 = Button(window,text ="*",command=lambda: calcul('*'))
bouton3.grid(column=2,row=3,sticky='w')

bouton4 = Button(window,text="/",command=lambda: calcul('/'))
bouton4.grid(column=3,row=3,sticky='w')

labelR=Label(window,text='resultat:')
labelR.grid(column=0, row=4, sticky ='w')

v3 = StringVar()
entreeR=Entry(window,textvariable=v3)
entreeR.grid(column=1,row=4,sticky='w')
entreeR.focus_set()
window.mainloop()
