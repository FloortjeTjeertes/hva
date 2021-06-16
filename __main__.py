from tkinter import Message
from appJar import gui
import Florian_Tjeertes_main

app = gui()
app.addLabel("title", "space age",0,0,2)
app.setLabelBg("title", "#5BCEFA")
app.setResizable(canResize=False)
app.addLabelEntry("first name",2,0)
app.addLabelEntry("last name",2,1)
app.addLabelNumericEntry("year",3,0,0)
app.addMessage("message","",3,1,2)

  
def press(button):
    main = Florian_Tjeertes_main.Main
    if button == "Cancel":
        app.stop()
    else:
     if button=="Submit":
        fname = app.getEntry("first name")
        lname = app.getEntry("last name")
        date = app.getEntry("year")
     if(fname!="" or lname!="" or int(date)!=0):
        print(main.start(fname,lname,date))
        app.setMessage("message",main.start(fname,lname,date))        


app.addButtons(["Submit", "Cancel"], press,4,0,2)
app.go()