
#setting
import PySimpleGUI as sg
import webbrowser
from playsound import playsound

#Functions for the mood buttons and Ailment window.
def quiz():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/quiz.py').read())
   
def prescription():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/prescription.py').read())

def sad():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/sad.py').read())
   
def tired():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/tired.py').read())
   
def anxious():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/anxious.py').read())
   
def angry():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/angry.py').read())
   
def cold():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/cold.py').read())
   
def cough():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/cough.py').read())
   
def fever():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/fever.py').read())
   
def diarrhoea():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/diarrhoea.py').read())
   
def sorethroat():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/sorethroat.py').read())
   
def redeyes():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/redeyes.py').read())
   
def nausea():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/nausea.py').read())
   
def headache():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/headache.py').read())
   
def bodypain():
   exec(open('C:/Users/sharo/Desktop/python project/testing python/bodypain.py').read())
   

#The main window layout

sg.theme("Material1")
layout=[[sg.Image(r'C:\Users\sharo\Desktop\python project\testing python\baymax.gif',key='_IMAGE_',size=(400,500),background_color=None,tooltip="Hi! I am baymax,your Personal Assistant")],[sg.Button('Next',key='next',enable_events=True)],[sg.Button("Info",key='audio',enable_events=True)],[sg.Button('Exit',key='exit',button_color=('blue','red'))]]
mainwindow=sg.Window("Main Window",location=(500,90),size=(400,800)).Layout(layout)
mainwinactive = True

#Mood window layout
layout1=[[sg.Text("Tell me what you feel:")],[sg.Radio("Happy",1,key='a',enable_events=True)],[sg.Radio("Sad",1,key='b',enable_events=True)],[sg.Radio("Angry",1,key='c',enable_events=True)],[sg.Radio("Stressed",1,key='d',enable_events=True)],[sg.Radio("Tired",1,key='f',enable_events=True)],[sg.Radio("Sick",1,key='e',enable_events=True)],[sg.Radio("Anxiety",1,key='g',enable_events=True)],[sg.Button("DETAILS",key='audio',enable_events=True)],[sg.Button("Exit",key='exit',enable_events=True,button_color=('blue','red'))]]
moodwindow=sg.Window("Mood Window",layout1,size=(300,300))
moodwinactive = True

#key
mood={'a':"Happy",'b':"Sad",'c':"Angry",'d':"Stressed",'e':"Sick",'f':"Tired",'g':'Anxiety'}

while True:
    if mainwinactive == True:
        event,values = mainwindow.Read(timeout=300)
        mainwindow.FindElement("_IMAGE_").UpdateAnimation("baymax.gif",time_between_frames=50)
        
#window close event
    if event == sg.WIN_CLOSED:
        mainwinactive = False
        mainwindow.Close()
        print("SG.Win_Closed")
        break
    
#Exit button for Main window.        
    if event == 'exit':
        mainwinactive = False
        mainwindow.Close()
        break
    
#Audio for intro.
    if event =='audio':
        print("Audio")
        playsound("C:/Users/sharo/Desktop/python project/testing python/intro.mp3")
        
    
#Launch 2nd window
    if event =='next':
        
        while True:
            if moodwinactive == True:
                event,values=moodwindow.read()
                
#Mood window's window close event.                
            if event == sg.WIN_CLOSED:
                moodwinactive = False
                moodwindow.close()
                break
 
 #Mood window's exit button.           
            if event =='exit':
                moodwinactive = False
                moodwindow.close()
                break
            
#Mood window's audio
            if event =='audio':
                playsound("C:/Users/sharo/Desktop/python project/testing python/mood.mp3")
                
#Happy button(radio button).
            if event=='a':
                layout2=[[sg.Button("Play Games",key='games',enable_events=True)],[sg.Button("Go shopping",key='shop',enable_events=True)],[sg.Button("Order food",key='food',enable_events=True)],[sg.Button("Exit",key='exit',enable_events=True,button_color=('blue','red'))]]
                window2=sg.Window("Symed",layout2)
                win2active=True
                
                while True:
                    if win2active == True:
                        event,values=window2.read()
#window close event for happy window.
                    if event == sg.WIN_CLOSED:
                        win2active=False
                        window2.close()
                        break
#Exit button of happy window.                    
                    if event =='exit':
                        win2active=False
                        window2.close()
                        break
                    
                      #Go shopping button.
                    if event == 'shop':
                        new=2
                        url="https://www.amazon.in"
                        webbrowser.open(url,new=new)
                        break
                    #Order food button.
                    if event =='food':
                        new=2
                        url="https://www.zomato.com"
                        webbrowser.open(url,new=new)
                        break
                        
                    #Play games
                    if event == 'games':
                         layout2_1=[[sg.Text("Single player")],[sg.Radio("chess",1,key='chess',enable_events=True)],[sg.Text("Multiplayer")],[sg.Radio("Uno",1,key='Uno',enable_events=True)],[sg.Button('Exit',key='exit',enable_events=True,button_color=('blue','red'))]]
                         window2_1=sg.Window("Symed",layout2_1)
                    gamewinactive = True
                    while True:
                        if gamewinactive == True:
                            event,values=window2_1.read()
#Exit button of games window.
                        if event =='exit':
                            gamewinactive=False
                            window2_1.close()
                            break
#Window close event of games window.                        
                        if event == sg.WIN_CLOSED:
                            gamewinactive=False
                            window2_1.close()
                            break
                        #chess(radio button)
                        elif event =='chess':
                            new=2
                            url="https://lichess.org/"
                            webbrowser.open(url,new=new)
                        #UNO(radio button)        
                        elif event == 'Uno':
                            new=2
                            url="https://www.mattelgames.com/games/en-in/play-games/uno-game-demo"
                            webbrowser.open(url,new=new)
            
#Sad button.(radio button)
            elif event=='b':
                layout3=[[sg.Text("Please choose:")],[sg.Button("Riddle",key='quiz')],[sg.Button("Sad",key='s')],[sg.Button("Exit",key='exit',enable_events=True,button_color=('blue','red'))]]
                window3=sg.Window("Symed",layout3)
                win3active = True 
           
                while True:
                        if win3active == True:
                            event,values=window3.read()
 #window close event for sad window.                          
                        if event == sg.WIN_CLOSED:
                            win3active=False
                            window3.close()
                            break
#Exit button for sad window.
                        if event =='exit':
                            win3active=False
                            window3.close()
                            break
                        
                        #quiz
                        if event=='quiz':
                            quiz()
                            
                        #sad's html
                        if event=='s':
                            sad()    
            
             #tired button
            elif event=='f':
                tired()
                
                    
            #Anxiety button
            elif event=='g':
                anxious()
            
            #Angry button   
            elif event=='c':
                angry()
                
            #Stressed button   
            elif event=='d':
                layout5=[[sg.Button("Play songs",key='songs',enable_events=True)],[sg.Button("Exit",key='exit',enable_events=True,button_color=('blue','red'))]]
                window5=sg.Window("Symed",layout5,size=(300,300))
                win5active=True
                while True:
                    if win5active == True:
                        event,values=window5.read()
                        
#window close event for stressed window                        
                    if event == sg.WIN_CLOSED:
                        win5active=False
                        window5.close()
                        break
#Exit button for stressed window                        
                    if event=='exit':
                        win5active=False
                        window5.close()
                        break
                    #song's button. 
                    if  event =='songs':
                        new=2
                        url="https://open.spotify.com/"
                        webbrowser.open(url,new=new)
                        break
                
                           
            #sick(Ailments window)
            elif event=='e':
                layout6=[[sg.Text("What are you experiencing?"),sg.Button("DETAILS",key='talk',button_color=('blue','yellow'))],[sg.Button("Headache",key='headache'),sg.Button("Fever",key='fever'),sg.Button("Diarrhoea",key='diarrhoea')],[sg.Button("Cold",key='cold'),sg.Button("Nausea",key='nausea'),sg.Button("Body pain",key='bodypain')],[sg.Button("Sore throat",key='sorethroat'),sg.Button("Cough",key='cough'),sg.Button("Red eyes",key='redeyes')],[sg.Button("Exit",key='exit',button_color=('blue','red'))]]
                window6=sg.Window("Sickness Diagnosis",layout6) 
                win6active = True
                while True:    
                    if win6active==True:
                        event,values=window6.read()
                        
#Window close event for sick window
                    if event == sg.WIN_CLOSED:
                        win6active=False
                        break
#Exit button for sick window.
                    if event == 'exit':
                        win6active=False
                        window6.close()
                        break
                    elif event =='talk':
                        
                    #play audio(sick):
                        playsound("C:/Users/sharo/Desktop/python project/testing python/sick.mp3")
                        
#HTML links of different ailments                   
                    elif event=='headache':
                        headache() 
                    elif event=='cold':
                        cold()
                    elif event=='cough':
                        cough()
                    elif event=='fever':
                        fever()
                    elif event=='diarrhoea':
                        diarrhoea()
                    elif event=='sorethroat':
                        sorethroat()
                    elif event=='bodypain':
                        bodypain()
                    elif event=='redeyes':
                        redeyes()
                    elif event=='nausea':
                        nausea() 
