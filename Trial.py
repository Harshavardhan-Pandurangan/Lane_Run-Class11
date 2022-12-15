#Importing all modules
from tkinter import *
import tkinter.messagebox
import time
import random

#Initial theme definition
theme_bg='Black'
theme_fg='White'
theme_ob='Gray'

#Function: Closing all windows at a time
def close_window():
    Start.destroy()
    Play_.destroy()
    Settings_.destroy()
#Creating all the windows
#1 Creating the Start page
Start = Tk()
Start.title('Start Page')
Start.geometry('600x400+383+184')
Start.resizable(0,0)
Start.configure(bg=theme_bg)
Start.protocol('WM_DELETE_WINDOW',close_window)

#2 Creating the Game page
Play_ = Tk()
Play_.title('Play')
Play_.geometry('600x400+383+184')
Play_.resizable(0,0)
Play_.configure(bg=theme_bg)
Play_.withdraw()
Play_.protocol('WM_DELETE_WINDOW',close_window)

#3 Creating the Settings page
Settings_ = Tk()
Settings_.title('Settings')
Settings_.geometry('600x400+383+184')
Settings_.resizable(0,0)
Settings_.configure(bg=theme_bg)
Settings_.withdraw()
Settings_.protocol('WM_DELETE_WINDOW',close_window)

#Creating contents of Play window
#1 Creating the canvas for the game (@Play)
game_canvas=Canvas(Play_,height=400,width=600,bg=theme_bg)
game_canvas.pack()

#2 Creating the three paths (@Play)
Path=game_canvas.create_polygon(300,100,0,400,600,400,fill=theme_fg,tags='Path')
Path_lineL=game_canvas.create_line(300,100,200,400,fill=theme_bg,width=5)
Path_lineR=game_canvas.create_line(300,100,400,400,fill=theme_bg,width=5)

#Creating the Ball (@Play)
Ball=game_canvas.create_oval(260,290,340,370,fill=theme_bg)

#Windows linking functions
def click1(to_do):
    if to_do=='Play':
        Start.withdraw()
        Play_.deiconify()
        pos_b=1
        global points
        points=0
        x=random.randint(0,2)
        start_game(x)
    elif to_do=='Settings':
        Start.withdraw()
        Settings_.deiconify()
    elif to_do=='How':
        tkinter.messagebox.showinfo('How to Play','''Use the left and right arrow keys to direct the ball,
dodging maximum no. of obstacles.
All the best!!!''')
    elif to_do=='Start':
        try:
            Settings_.withdraw()
        except:
            Play_.withdraw()
        Start.deiconify()

#Creating links to game and settings page
#1 Play button (@Start)
Play=Button(Start,text='PLAY',font='Elephant 20 bold',height=1,width=5,command=lambda: click1('Play'),fg=theme_bg,bg=theme_fg)
Play.place(x=250,y=165)

#2 Settings button (@Start)
Logo_settings=PhotoImage(file='settings logo.gif')
Settings=Button(Start,image=Logo_settings,command=lambda: click1('Settings'),fg=theme_bg,bg=theme_fg)
Settings.pack(anchor=NE)

#3 How to play button (@Start)
How=Button(Start,text='How to Play',font='Elephant 15',height=1,width=10,command=lambda: click1('How'),fg=theme_bg,bg=theme_fg)
How.place(x=228,y=250)

#4 Back to Start button (@Settings)
Back1=Button(Settings_,text='<',command=lambda: click1('Start'),font='none 15 bold',width=3,fg=theme_bg,bg=theme_fg)
Back1.pack(anchor=NW)

#Settings page controls
#Theme changing button (@Settings_)
Themes=['Theme 1','Theme 2','Theme 3']
Theme_colors={0:['Black','White','Gray'],1:['White','Black','Gray'],2:['Red','Blue','Yellow']}
theme_=StringVar(Settings_)
theme_.set('Theme 1')

def Theme_change():
    global x
    x=theme_.get()
    x=Themes.index(x)
    x+=1
    x%=3
    curr_theme=x
    x=Themes[x]
    theme_.set(x)
    curr_bg=Theme_colors[curr_theme][0]
    curr_fg=Theme_colors[curr_theme][1]
    theme_ob=Theme_colors[curr_theme][2]
    Start.configure(bg=curr_bg)
    Play_.configure(bg=curr_bg)
    Settings_.configure(bg=curr_bg)
    Play.configure(bg=curr_fg,fg=curr_bg)
    How.configure(bg=curr_fg,fg=curr_bg)
    Back1.configure(bg=curr_fg,fg=curr_bg)
    theme_label1.configure(bg=curr_bg,fg=curr_fg)
    theme_label2.configure(bg=curr_fg,fg=curr_bg)
    theme_change.configure(bg=curr_fg,fg=curr_bg)
    volume_label1.configure(bg=curr_bg,fg=curr_fg)
    volume_label2.configure(bg=curr_fg,fg=curr_bg)
    volume_change.configure(bg=curr_fg,fg=curr_bg)
    difficulty_label1.configure(bg=curr_bg,fg=curr_fg)
    difficulty_label2.configure(bg=curr_fg,fg=curr_bg)
    difficulty_change.configure(bg=curr_fg,fg=curr_bg)
    about.configure(bg=curr_bg,fg=curr_fg)
    game_canvas.configure(bg=curr_bg)
    game_canvas.delete('all')
    Path=game_canvas.create_polygon(300,100,0,400,600,400,fill=curr_fg)
    Path_lineL=game_canvas.create_line(300,100,200,400,fill=curr_bg,width=5)
    Path_lineR=game_canvas.create_line(300,100,400,400,fill=curr_bg,width=5)
    Ball=game_canvas.create_oval(260,290,340,370,fill=curr_bg)
    global pos_b
    pos_b=1
    def MoveBall_L(event):
        global pos_b
        if pos_b>0:
            pos_b-=1
            game_canvas.move(Ball,-150,0)
        else:
            pass
    def MoveBall_R(event):
        global pos_b
        if pos_b<2:
            pos_b+=1
            game_canvas.move(Ball,150,0)
        else:
            pass
    game_canvas.bind_all('<Left>',MoveBall_L)
    game_canvas.bind_all('<Right>',MoveBall_R)

theme_label1=Label(Settings_,text='Theme      :',font='Elephant 18',bg=theme_bg,fg=theme_fg)
theme_label1.place(x=159,y=80)
theme_label2=Label(Settings_,textvariable=theme_,font='Elephant 15',width=10,bg=theme_fg,fg=theme_bg)
theme_label2.place(x=300,y=82)
theme_change=Button(Settings_,text='>',command=Theme_change,font='none 13 bold',bg=theme_fg,fg=theme_bg)
theme_change.place(x=448,y=82)

#Volume checkbox (@Settings_)
Volumes=['Off','On']
volume_=StringVar(Settings_)
volume_.set('Off')

def Volume_change():
    global y
    y=volume_.get()
    y=Volumes.index(y)
    y+=1
    y%=2
    y=Volumes[y]
    volume_.set(y)
    
volume_label1=Label(Settings_,text='Sounds     :',font='Elephant 18',bg=theme_bg,fg=theme_fg)
volume_label1.place(x=159,y=140)
volume_label2=Label(Settings_,textvariable=volume_,font='Elephant 15',width=10,bg=theme_fg,fg=theme_bg)
volume_label2.place(x=300,y=142)
volume_change=Button(Settings_,text='>',command=Volume_change,font='none 13 bold',bg=theme_fg,fg=theme_bg)
volume_change.place(x=448,y=142)

#Difficulty changing button (@Settings_)
Difficulties=['Easy','Medium','Hard']
difficulty_=StringVar(Settings_)
difficulty_.set('Easy')

def Difficulty_change():
    global z
    z=difficulty_.get()
    z=Difficulties.index(z)
    z+=1
    z%=3
    z=Difficulties[z]
    difficulty_.set(z)
    
difficulty_label1=Label(Settings_,text='Difficulty :',font='Elephant 18',bg=theme_bg,fg=theme_fg)
difficulty_label1.place(x=159,y=200)
difficulty_label2=Label(Settings_,textvariable=difficulty_,font='Elephant 15',width=10,bg=theme_fg,fg=theme_bg)
difficulty_label2.place(x=300,y=202)
difficulty_change=Button(Settings_,text='>',command=Difficulty_change,font='none 13 bold',bg=theme_fg,fg=theme_bg)
difficulty_change.place(x=448,y=202)

#About the game
about=Label(Settings_,bg=theme_bg,fg=theme_fg,font='Elephant 10',text='''Game built using Python, tkinter, time and random.
Game built by Harshavardhan P.
Credits: Srinidhi (PSBBMS), stackoverflow.com, geeksforgeeks.com,
'Python Programming lessons Complete' YouTube.''')
about.place(x=80,y=280)

#Start of game building
global pos_b
pos_b=1
#Controlling the Ball (@Play)
def MoveBall_L(event):
    global pos_b
    if pos_b>0:
        pos_b-=1
        game_canvas.move(Ball,-150,0)
    else:
        pass
def MoveBall_R(event):
    global pos_b
    if pos_b<2:
        pos_b+=1
        game_canvas.move(Ball,150,0)
    else:
        pass

#Creating obstacles
class Obstacle:
    def __init__(self,lane):
        self.lane=lane
        self.psn=1
        self.id=game_canvas.create_rectangle(299,99,301,101,fill='Gray')

    #Points scorer
    def destroy(self):
        self.id=None
        global points
        points+=1
        
    #Movement of lane 0
    def lane0(self):
        x0,y0,x1,y1=game_canvas.coords(self.id)
        if self.psn%3==0:
            x1-=2
        y1+=2
        if self.psn%4==0:
            pass
        else:
            y0+=2
        x0-=2
        game_canvas.coords(self.id,x0,y0,x1,y1)
        game_canvas.update()
        self.psn+=1

    #Movement of lane 1
    def lane1(self):
        x0,y0,x1,y1=game_canvas.coords(self.id)
        if self.psn%3==0:
            x1+=2
            x0-=2
        y1+=2
        if self.psn%4==0:
            pass
        else:
            y0+=2
        game_canvas.coords(self.id,x0,y0,x1,y1)
        game_canvas.update()
        self.psn+=1

    #Movement of lane 2
    def lane2(self):
        x0,y0,x1,y1=game_canvas.coords(self.id)
        if self.psn%3==0:
            x0+=2
            
        y1+=2
        if self.psn%4==0:
            pass
        else:
            y0+=2
        x1+=2
        game_canvas.coords(self.id,x0,y0,x1,y1)
        game_canvas.update()
        self.psn+=1

game_canvas.focus_set()
game_canvas.bind_all('<Left>',MoveBall_L)
game_canvas.bind_all('<Right>',MoveBall_R)

#Each obstacle takes 402 cycles to reach out
#so each of them can be dropped on 399st cycle

def start_game(LaneO):
    t=0.01
    Obs0=Obstacle(LaneO)
    for i in range(50):
        if Obs0.lane==0:
            Obs0.lane0()
        elif Obs0.lane==1:
            Obs0.lane1()
        else:
            Obs0.lane2()
        time.sleep(0.01)
    Obs1=Obs0
    LaneN=random.randint(0,2)
    if LaneN==LaneO:
        LaneN=random.randint(0,2)
    Obs0=Obstacle(LaneN)
    for i in range(50):
        if Obs1.lane==0:
            Obs1.lane0()
        elif Obs1.lane==1:
            Obs1.lane1()
        else:
            Obs1.lane2()
        if Obs0.lane==0:
            Obs0.lane0()
        elif Obs0.lane==1:
            Obs0.lane1()
        else:
            Obs0.lane2()
        time.sleep(0.01)
    Obs2=Obs1
    Obs1=Obs0
    Obs0=None
    Obs3=None
    Obs2_count=0
    LaneO=LaneN
    while True:
        if Obs0==None:
            LaneN=random.randint(0,2)
            if LaneN==LaneO:
                LaneN=random.randint(0,2)
            Obs0=Obstacle(LaneN)
            LaneO=LaneN
        if Obs0.lane==0:
            Obs0.lane0()
        elif Obs0.lane==1:
            Obs0.lane1()
        else:
            Obs0.lane2()
        if Obs1.lane==0:
            Obs1.lane0()
        elif Obs1.lane==1:
            Obs1.lane1()
        else:
            Obs1.lane2()
        if Obs2.lane==0:
            Obs2.lane0()
        elif Obs2.lane==1:
            Obs2.lane1()
        else:
            Obs2.lane2()
        Obs2_count+=1
        if Obs2_count==50:
            Obs0,Obs1,Obs2,Obs3=None,Obs0,Obs1,Obs2
            Obs2_count=0
            Obs3_count=0
        if Obs3!=None:
            Obs3_count+=1
            if Obs3.lane==0:
                Obs3.lane0()
            elif Obs3.lane==1:
                Obs3.lane1()
            else:
                Obs3.lane2()
            if Obs3_count==50:
                Obs3=None
                global points
                points+=1
                print(points)
        time.sleep(0.001)

#Mainloop statements
Start.mainloop()
Play_.mainloop()
