import tkinter as tk
import random
from tkinter import ttk
app=tk.Tk()
app.title('ODD OR EVEN')
app.geometry('240x200')
app.configure(bg="black")
def change_b1_text():                                   
    global i_name
    i_name=e_name.get()
    b1_name.config(text='Replay ')
    tos=tk.Tk()
    tos.title('Toss')
    tos.geometry('500x400')

    def button_click(button):
        global buttn_click
        buttn_click=button
       
        if button=='Odd':
            l0dd=tk.Label(tos,text='Odd ah...ok')
            l0dd.grid(row=5,column=4)    
            oddd.config(state="normal",background='green')
            evenn.config(state="disabled",background='red')
            choose_a_no=tk.Label(tos,text=' choose a number for toss',background='blue',fg='white')
            choose_a_no.grid(row=6,column=4)
        if button=='Eve':
            leve1=tk.Label(tos,text='Eve ah...ok')
            leve1.grid(row=5,column=4)
            evenn.config(state="normal",background='green')
            oddd.config(state="disabled",background='red')
            choose_a_no=tk.Label(tos,text='choose a number for toss',background='blue',fg='white')
            choose_a_no.grid(row=6,column=4)

    def on_button_click(button_number):
        ai=random.randint(1,10)                                        
        toss=ai+button_number            
        ai_num=tk.Label(tos,text=f"AI's number for toss is {ai}")
        ai_num.grid(row=15,column=4)
        global tag
        
        def Batting_second_ai():
            bowlin=tk.Tk()
            bowlin.title('Bowling')
            bowlin.geometry('500x300')
            batt=tk.Label(bowlin,text='Chasing for Me',font='Calibri 15 bold')
            batt.grid(row=0,column=3)
            target=tk.Label(bowlin,text=f'Target to score={tag+1}')
            target.grid(row=0,column=5)
            global asco
            def button_click(number):
                
                ai=random.randint(1,10)
                if number!=ai:
                    run=int(asco['text'])
                    asco['text']=run+ai
                    runn=tk.Label(bowlin,text=f'AI Runs={ai}')
                    runn.grid(row=1,column=5)
                    if int(asco['text'])>tag:
                        iwon=tk.Label(bowlin,text='I Won the Match')
                        iwon.grid(row=3,column=4)
                   
                if number==ai:
                    out=tk.Label(bowlin,text='I got out')
                    out.grid(row=3,column=4)
                    if int(asco['text'])<tag:
                        hwon=tk.Label(bowlin,text='You Won the Match')
                        hwon.grid(row=3,column=4)
                    if int(asco['text'])==tag:
                        hdrew=tk.Label(bowlin,text=' Match Drew')
                        hdrew.grid(row=3,column=4)

                    bowlin.mainloop()
                        
                    
            asc=tk.Label(bowlin,text='       score=')
            asc.grid(row=1,column=3)
            asco=tk.Label(bowlin,text='0')
            asco.grid(row=1,column=4)
            u1=tk.Button(bowlin,text='1', command=lambda:button_click(1),height=2,width=3)
            u1.grid(row=5,column=4, padx=0, pady=0)
            u2=tk.Button(bowlin,text='2', command=lambda:button_click(2),height=2,width=3)
            u2.grid(row=5,column=5, padx=0, pady=0)
            u3=tk.Button(bowlin,text='3', command=lambda:button_click(3),height=2,width=3)
            u3.grid(row=5,column=6, padx=0, pady=0)
            u4=tk.Button(bowlin,text='4', command=lambda:button_click(4),height=2,width=3)
            u4.grid(row=7,column=4, padx=0, pady=0)
            u5=tk.Button(bowlin,text='5', command=lambda:button_click(5),height=2,width=3)
            u5.grid(row=7,column=5, padx=0, pady=0)
            u6=tk.Button(bowlin,text='6', command=lambda:button_click(6),height=2,width=3)
            u6.grid(row=7,column=6, padx=0, pady=0)
            u7=tk.Button(bowlin,text='7', command=lambda:button_click(7),height=2,width=3)
            u7.grid(row=9,column=4, padx=0, pady=0)
            u8=tk.Button(bowlin,text='8', command=lambda:button_click(8),height=2,width=3)
            u8.grid(row=9,column=5, padx=0, pady=0)
            u9=tk.Button(bowlin,text='9', command=lambda:button_click(9),height=2,width=3)
            u9.grid(row=9,column=6, padx=0, pady=0)
            u10=tk.Button(bowlin,text='10', command=lambda:button_click(10),height=2,width=5)
            u10.grid(row=11,column=5,padx=0, pady=0)
        global tar
        def Bowling_second_ai():
            battin=tk.Tk()
            battin.title('Batting')
            battin.geometry('500x300')
            bowll=tk.Label(battin,text='Chasing for YOU',font='Calibri 15 bold')
            bowll.grid(row=0,column=3)
            
            target=tk.Label(battin,text=f'Target to score={tar+1}')
            target.grid(row=0,column=5)
            global usco 
            def buton_click(number):
                ai=random.randint(1,10)
                if number!=ai:
                    ran=int(usco['text'])
                    usco['text']=ran+number
                    ruun=tk.Label(battin,text=f'AI ball={ai}')
                    ruun.grid(row=1,column=6)
                    if int(usco['text'])>tar:
                        hwon=tk.Label(battin,text='You Won the Match')
                        hwon.grid(row=3,column=4)
                   
                if number==ai:
                    out=tk.Label(battin,text='YOU got out')
                    out.grid(row=3,column=4)
                    if int(usco['text'])<tar:
                        iwon=tk.Label(battin,text='I Won the Match')
                        iwon.grid(row=3,column=4)
                    if int(usco['text'])==tar:
                        hdrew=tk.Label(battin,text=' Match Drew')
                        hdrew.grid(row=3,column=4)

                    battin.mainloop()
                    
            usc=tk.Label(battin,text='      score=')
            usc.grid(row=1,column=3)
            usco=tk.Label(battin,text='0')
            usco.grid(row=1,column=4)
            u1=tk.Button(battin,text='1', command= lambda:buton_click(1),height=2,width=3)
            u1.grid(row=5,column=4, padx=0, pady=0)
            u2=tk.Button(battin,text='2', command= lambda:buton_click(2),height=2,width=3)
            u2.grid(row=5,column=5, padx=0, pady=0)
            u3=tk.Button(battin,text='3', command= lambda:buton_click(3),height=2,width=3)
            u3.grid(row=5,column=6, padx=0, pady=0)
            u4=tk.Button(battin,text='4', command= lambda:buton_click(4),height=2,width=3)
            u4.grid(row=7,column=4, padx=0, pady=0)
            u5=tk.Button(battin,text='5', command= lambda:buton_click(5),height=2,width=3)
            u5.grid(row=7,column=5, padx=0, pady=0)
            u6=tk.Button(battin,text='6', command= lambda:buton_click(6),height=2,width=3)
            u6.grid(row=7,column=6, padx=0, pady=0)
            u7=tk.Button(battin,text='7', command= lambda:buton_click(7),height=2,width=3)
            u7.grid(row=9,column=4, padx=0, pady=0)
            u8=tk.Button(battin,text='8', command= lambda:buton_click(8),height=2,width=3)
            u8.grid(row=9,column=5, padx=0, pady=0)
            u9=tk.Button(battin,text='9', command= lambda:buton_click(9),height=2,width=3)
            u9.grid(row=9,column=6, padx=0, pady=0)
            u10=tk.Button(battin,text='10', command= lambda:buton_click(10),height=2,width=5)
            u10.grid(row=11,column=5,padx=0, pady=0)
            
      
        def Bowling_first_you():
            bowling=tk.Tk()
            bowling.title('Bowling')
            bowling.geometry('500x300')
            batt=tk.Label(bowling,text='You Chose Bowling First',font='Calibri 15 bold')
            batt.grid(row=0,column=3)
            global asco
            def button_click(number):
                
                ai=random.randint(1,10)
                if number!=ai:
                    run=int(asco['text'])
                    asco['text']=run+ai
                    runn=tk.Label(bowling,text=f'AI Runs={ai}')
                    runn.grid(row=1,column=5)
                    
                if number==ai:
                    out=tk.Label(bowling,text='I got out')
                    out.grid(row=3,column=4)
                    global tar
                    tar=int(asco['text'])
                    change=Bowling_second_ai()
                    bowling.mainloop()
            asc=tk.Label(bowling,text='       score=')
            asc.grid(row=1,column=3)
            asco=tk.Label(bowling,text='0')
            asco.grid(row=1,column=4)
            u1=tk.Button(bowling,text='1', command=lambda:button_click(1),height=2,width=3)
            u1.grid(row=5,column=4, padx=0, pady=0)
            u2=tk.Button(bowling,text='2', command=lambda:button_click(2),height=2,width=3)
            u2.grid(row=5,column=5, padx=0, pady=0)
            u3=tk.Button(bowling,text='3', command=lambda:button_click(3),height=2,width=3)
            u3.grid(row=5,column=6, padx=0, pady=0)
            u4=tk.Button(bowling,text='4', command=lambda:button_click(4),height=2,width=3)
            u4.grid(row=7,column=4, padx=0, pady=0)
            u5=tk.Button(bowling,text='5', command=lambda:button_click(5),height=2,width=3)
            u5.grid(row=7,column=5, padx=0, pady=0)
            u6=tk.Button(bowling,text='6', command=lambda:button_click(6),height=2,width=3)
            u6.grid(row=7,column=6, padx=0, pady=0)
            u7=tk.Button(bowling,text='7', command=lambda:button_click(7),height=2,width=3)
            u7.grid(row=9,column=4, padx=0, pady=0)
            u8=tk.Button(bowling,text='8', command=lambda:button_click(8),height=2,width=3)
            u8.grid(row=9,column=5, padx=0, pady=0)
            u9=tk.Button(bowling,text='9', command=lambda:button_click(9),height=2,width=3)
            u9.grid(row=9,column=6, padx=0, pady=0)
            u10=tk.Button(bowling,text='10', command=lambda:button_click(10),height=2,width=5)
            u10.grid(row=11,column=5,padx=0, pady=0)

            
        def Batting_first_you():
            batting=tk.Tk()
            batting.title('Batting')
            batting.geometry('500x300')
            bowll=tk.Label(batting,text='You Chose Batting First',font='Calibri 15 bold')
            bowll.grid(row=0,column=3)
            global usco 
            def buton_click(number):
                ai=random.randint(1,10)
                if number!=ai:
                    ran=int(usco['text'])
                    usco['text']=ran+number
                    ruun=tk.Label(batting,text=f'AI ball={ai}')
                    ruun.grid(row=1,column=6)
                   
                if number==ai:
                    out=tk.Label(batting,text='YOU got out')
                    out.grid(row=3,column=4)
                    global tag
                    tag=int(usco['text'])
                    change=Batting_second_ai()
                    batting.mainloop()
            usc=tk.Label(batting,text='       score=')
            usc.grid(row=1,column=3)
            usco=tk.Label(batting,text='0')
            usco.grid(row=1,column=4)
            u1=tk.Button(batting,text='1', command= lambda:buton_click(1),height=2,width=3)
            u1.grid(row=5,column=4, padx=0, pady=0)
            u2=tk.Button(batting,text='2', command= lambda:buton_click(2),height=2,width=3)
            u2.grid(row=5,column=5, padx=0, pady=0)
            u3=tk.Button(batting,text='3', command= lambda:buton_click(3),height=2,width=3)
            u3.grid(row=5,column=6, padx=0, pady=0)
            u4=tk.Button(batting,text='4', command= lambda:buton_click(4),height=2,width=3)
            u4.grid(row=7,column=4, padx=0, pady=0)
            u5=tk.Button(batting,text='5', command= lambda:buton_click(5),height=2,width=3)
            u5.grid(row=7,column=5, padx=0, pady=0)
            u6=tk.Button(batting,text='6', command= lambda:buton_click(6),height=2,width=3)
            u6.grid(row=7,column=6, padx=0, pady=0)
            u7=tk.Button(batting,text='7', command= lambda:buton_click(7),height=2,width=3)
            u7.grid(row=9,column=4, padx=0, pady=0)
            u8=tk.Button(batting,text='8', command= lambda:buton_click(8),height=2,width=3)
            u8.grid(row=9,column=5, padx=0, pady=0)
            u9=tk.Button(batting,text='9', command= lambda:buton_click(9),height=2,width=3)
            u9.grid(row=9,column=6, padx=0, pady=0)
            u10=tk.Button(batting,text='10', command= lambda:buton_click(10),height=2,width=5)
            u10.grid(row=11,column=5,padx=0, pady=0)
            
             
        if toss%2==0:
        
            if buttn_click=='Eve':
                l1won=tk.Label(tos,text='You won the toss choose to??')
                l1won.grid(row=16,column=4, padx=10, pady=10)
                bat=tk.Button(tos,text='Batting')
                bat.config(command=Batting_first_you)
                bat.grid(row=17,column=3,columnspan=1)
                bowl=tk.Button(tos,text='Bowling',)
                bowl.config(command=Bowling_first_you)
                bowl.grid(row=17,column=5,columnspan=1)    

            if buttn_click=='Odd':
                l2won=tk.Label(tos,text='I won')
                l2won.grid(row=16,column=4, padx=10, pady=10)
                bat_or_bowl=random.randint(1,2)
                if bat_or_bowl==1:
                    c_bat=tk.Label(tos,text='I chose Batting First')
                    c_bat.grid(row=17,column=4)
                    bowling=tk.Tk()
                    bowling.title('Bowling')
                    bowling.geometry('500x300')
                    batt=tk.Label(bowling,text='I Chose Batting First ',font='Calibri 15 bold')
                    batt.grid(row=0,column=3)
                    global asco
                    def button_click(number):
                
                        ai=random.randint(1,10)
                        if number!=ai:
                            run=int(asco['text'])
                            asco['text']=run+ai
                            runn=tk.Label(bowling,text=f'AI Runs={ai}')
                            runn.grid(row=1,column=5)
                    
                        if number==ai:
                            out=tk.Label(bowling,text='I got out')
                            out.grid(row=3,column=4)
                            global tar
                            tar=int(asco['text'])
                            change=Bowling_second_ai()
                            bowling.mainloop()
                    asc=tk.Label(bowling,text='      score=')
                    asc.grid(row=1,column=3)
                    asco=tk.Label(bowling,text='0')
                    asco.grid(row=1,column=4)
                    u1=tk.Button(bowling,text='1', command=lambda:button_click(1),height=2,width=3)
                    u1.grid(row=5,column=4, padx=0, pady=0)
                    u2=tk.Button(bowling,text='2', command=lambda:button_click(2),height=2,width=3)
                    u2.grid(row=5,column=5, padx=0, pady=0)
                    u3=tk.Button(bowling,text='3', command=lambda:button_click(3),height=2,width=3)
                    u3.grid(row=5,column=6, padx=0, pady=0)
                    u4=tk.Button(bowling,text='4', command=lambda:button_click(4),height=2,width=3)
                    u4.grid(row=7,column=4, padx=0, pady=0)
                    u5=tk.Button(bowling,text='5', command=lambda:button_click(5),height=2,width=3)
                    u5.grid(row=7,column=5, padx=0, pady=0)
                    u6=tk.Button(bowling,text='6', command=lambda:button_click(6),height=2,width=3)
                    u6.grid(row=7,column=6, padx=0, pady=0)
                    u7=tk.Button(bowling,text='7', command=lambda:button_click(7),height=2,width=3)
                    u7.grid(row=9,column=4, padx=0, pady=0)
                    u8=tk.Button(bowling,text='8', command=lambda:button_click(8),height=2,width=3)
                    u8.grid(row=9,column=5, padx=0, pady=0)
                    u9=tk.Button(bowling,text='9', command=lambda:button_click(9),height=2,width=3)
                    u9.grid(row=9,column=6, padx=0, pady=0)
                    u10=tk.Button(bowling,text='10', command=lambda:button_click(10),height=2,width=5)
                    u10.grid(row=11,column=5,padx=0, pady=0)
                    
                if bat_or_bowl==2:
                    c_bowl=tk.Label(tos,text='I chose Bowling First')
                    c_bowl.grid(row=17,column=4)
                    #---------ai chose bowling----------
                    batting=tk.Tk()
                    batting.title('Batting')
                    batting.geometry('500x300')
                    bowll=tk.Label(batting,text='I Chose Bowling First',font='Calibri 15 bold')
                    bowll.grid(row=0,column=3)
                    global usco 
                    def buton_click(number):
                        ai=random.randint(1,10)
                        if number!=ai:
                            ran=int(usco['text'])
                            usco['text']=ran+number
                            ruun=tk.Label(batting,text=f'AI ball={ai}')
                            ruun.grid(row=1,column=6)
                        if number==ai:
                            out=tk.Label(batting,text='YOU got out')
                            out.grid(row=3,column=4)
                            global tag
                            tag=int(usco['text'])
                            change=Batting_second_ai()
                            batting.mainloop()
                    usc=tk.Label(batting,text='       score=')
                    usc.grid(row=1,column=3)
                    usco=tk.Label(batting,text='0')
                    usco.grid(row=1,column=4)
                    u1=tk.Button(batting,text='1', command= lambda:buton_click(1),height=2,width=3)
                    u1.grid(row=5,column=4, padx=0, pady=0)
                    u2=tk.Button(batting,text='2', command= lambda:buton_click(2),height=2,width=3)
                    u2.grid(row=5,column=5, padx=0, pady=0)
                    u3=tk.Button(batting,text='3', command= lambda:buton_click(3),height=2,width=3)
                    u3.grid(row=5,column=6, padx=0, pady=0)
                    u4=tk.Button(batting,text='4', command= lambda:buton_click(4),height=2,width=3)
                    u4.grid(row=7,column=4, padx=0, pady=0)
                    u5=tk.Button(batting,text='5', command= lambda:buton_click(5),height=2,width=3)
                    u5.grid(row=7,column=5, padx=0, pady=0)
                    u6=tk.Button(batting,text='6', command= lambda:buton_click(6),height=2,width=3)
                    u6.grid(row=7,column=6, padx=0, pady=0)
                    u7=tk.Button(batting,text='7', command= lambda:buton_click(7),height=2,width=3)
                    u7.grid(row=9,column=4, padx=0, pady=0)
                    u8=tk.Button(batting,text='8', command= lambda:buton_click(8),height=2,width=3)
                    u8.grid(row=9,column=5, padx=0, pady=0)
                    u9=tk.Button(batting,text='9', command= lambda:buton_click(9),height=2,width=3)
                    u9.grid(row=9,column=6, padx=0, pady=0)
                    u10=tk.Button(batting,text='10', command= lambda:buton_click(10),height=2,width=5)
                    u10.grid(row=11,column=5,padx=0, pady=0)

                    
                    
        if toss%2!=0:
            if buttn_click=='Odd':
                l1won=tk.Label(tos,text='You won the toss choose to??')
                l1won.grid(row=16,column=4, padx=10, pady=10)
                bat=tk.Button(tos,text='Batting')
                bat.config(command=Batting_first_you)
                bat.grid(row=17,column=3,columnspan=1)
                bowl=tk.Button(tos,text='Bowling')
                bowl.config(command=Bowling_first_you)
                bowl.grid(row=17,column=5,columnspan=1)
                
            if buttn_click=='Eve':
                l2won=tk.Label(tos,text='I won')
                l2won.grid(row=16,column=4, padx=10, pady=10)
                bat_or_bowl=random.randint(1,2)
                if bat_or_bowl==1:
                    c_bat=tk.Label(tos,text='I chose Batting First')
                    c_bat.grid(row=17,column=4)
                    bowling=tk.Tk()
                    bowling.title('Bowling')
                    bowling.geometry('500x300')
                    batt=tk.Label(bowling,text='I Chose Batting First',font='Calibri 15 bold')
                    batt.grid(row=0,column=3)
                    global asca
                    def button_click(number):
                
                        ai=random.randint(1,10)
                        if number!=ai:
                            run=int(asca['text'])
                            asca['text']=run+ai
                            run=tk.Label(bowling,text=f'AI Runs={ai}')
                            run.grid(row=1,column=5)
                    
                        if number==ai:
                            out=tk.Label(bowling,text='I got out')
                            out.grid(row=3,column=4)
                            global tar
                            tar=int(asca['text'])
                            change=Bowling_second_ai()
                            bowling.mainloop()
                    asc=tk.Label(bowling,text='       score=')
                    asc.grid(row=1,column=3)
                    asca=tk.Label(bowling,text='0')
                    asca.grid(row=1,column=4)
                    u1=tk.Button(bowling,text='1', command=lambda:button_click(1),height=2,width=3)
                    u1.grid(row=5,column=4, padx=0, pady=0)
                    u2=tk.Button(bowling,text='2', command=lambda:button_click(2),height=2,width=3)
                    u2.grid(row=5,column=5, padx=0, pady=0)
                    u3=tk.Button(bowling,text='3', command=lambda:button_click(3),height=2,width=3)
                    u3.grid(row=5,column=6, padx=0, pady=0)
                    u4=tk.Button(bowling,text='4', command=lambda:button_click(4),height=2,width=3)
                    u4.grid(row=7,column=4, padx=0, pady=0)
                    u5=tk.Button(bowling,text='5', command=lambda:button_click(5),height=2,width=3)
                    u5.grid(row=7,column=5, padx=0, pady=0)
                    u6=tk.Button(bowling,text='6', command=lambda:button_click(6),height=2,width=3)
                    u6.grid(row=7,column=6, padx=0, pady=0)
                    u7=tk.Button(bowling,text='7', command=lambda:button_click(7),height=2,width=3)
                    u7.grid(row=9,column=4, padx=0, pady=0)
                    u8=tk.Button(bowling,text='8', command=lambda:button_click(8),height=2,width=3)
                    u8.grid(row=9,column=5, padx=0, pady=0)
                    u9=tk.Button(bowling,text='9', command=lambda:button_click(9),height=2,width=3)
                    u9.grid(row=9,column=6, padx=0, pady=0)
                    u10=tk.Button(bowling,text='10', command=lambda:button_click(10),height=2,width=5)
                    u10.grid(row=11,column=5,padx=0, pady=0)
                 



                if bat_or_bowl==2:
                    c_bowl=tk.Label(tos,text='I chose Bowling First')
                    c_bowl.grid(row=17,column=4)
                    batting=tk.Tk()
                    batting.title('Batting')
                    batting.geometry('500x300')
                    bowll=tk.Label(batting,text='I Chose Bowling First',font='Calibri 15 bold')
                    bowll.grid(row=0,column=3)
                    global uscu 
                    def buton_click(number):
                        ai=random.randint(1,10)
                        if number!=ai:
                            ran=int(uscu['text'])
                            uscu['text']=ran+number
                            ruun=tk.Label(batting,text=f'AI ball={ai}')
                            ruun.grid(row=1,column=6)
                        if number==ai:
                            out=tk.Label(batting,text='YOU got out')
                            out.grid(row=3,column=4)
                            global tag
                            tag=int(uscu['text'])
                            change=Batting_second_ai()
                            batting.mainloop()
                    usc=tk.Label(batting,text='         score=')
                    usc.grid(row=1,column=3)
                    uscu=tk.Label(batting,text='0')
                    uscu.grid(row=1,column=4)
                    u1=tk.Button(batting,text='1', command= lambda:buton_click(1),height=2,width=3)
                    u1.grid(row=5,column=4, padx=0, pady=0)
                    u2=tk.Button(batting,text='2', command= lambda:buton_click(2),height=2,width=3)
                    u2.grid(row=5,column=5, padx=0, pady=0)
                    u3=tk.Button(batting,text='3', command= lambda:buton_click(3),height=2,width=3)
                    u3.grid(row=5,column=6, padx=0, pady=0)
                    u4=tk.Button(batting,text='4', command= lambda:buton_click(4),height=2,width=3)
                    u4.grid(row=7,column=4, padx=0, pady=0)
                    u5=tk.Button(batting,text='5', command= lambda:buton_click(5),height=2,width=3)
                    u5.grid(row=7,column=5, padx=0, pady=0)
                    u6=tk.Button(batting,text='6', command= lambda:buton_click(6),height=2,width=3)
                    u6.grid(row=7,column=6, padx=0, pady=0)
                    u7=tk.Button(batting,text='7', command= lambda:buton_click(7),height=2,width=3)
                    u7.grid(row=9,column=4, padx=0, pady=0)
                    u8=tk.Button(batting,text='8', command= lambda:buton_click(8),height=2,width=3)
                    u8.grid(row=9,column=5, padx=0, pady=0)
                    u9=tk.Button(batting,text='9', command= lambda:buton_click(9),height=2,width=3)
                    u9.grid(row=9,column=6, padx=0, pady=0)
                    u10=tk.Button(batting,text='10', command= lambda:buton_click(10),height=2,width=5)
                    u10.grid(row=11,column=5,padx=0, pady=0)

        
    
    def handle_button_click(button_number):
        on_button_click(button_number)
        


    tosl=tk.Label(tos,text='Toss for the match',font='Calibri 15 bold')
    tosl.grid(row=0,column=4)
    l3=tk.Label(tos,text=f'{i_name}  Odd or Eve ??')
    l3.grid(row=2,column=4)
    #odd butt and even butt
    oddd=tk.Button(tos,text='Odd')
    evenn=tk.Button(tos,text='Eve')
    oddd.config(command=lambda: button_click('Odd'),height=2,width=20)
    evenn.config(command=lambda: button_click('Eve'),height=2,width=20)
    oddd.grid(row=4,column=3)
    evenn.grid(row=4,column=5)
    # Create buttons
    bu1=tk.Button(tos,text='1', command=lambda: handle_button_click(1),height=2,width=3)
    bu1.grid(row=9,column=3, padx=0, pady=0)
    bu2=tk.Button(tos,text='2', command=lambda: handle_button_click(2),height=2,width=3)
    bu2.grid(row=9,column=4, padx=0, pady=0)
    bu3=tk.Button(tos,text='3', command=lambda: handle_button_click(3),height=2,width=3)
    bu3.grid(row=9,column=5, padx=0, pady=0)
    bu4=tk.Button(tos,text='4', command=lambda: handle_button_click(4),height=2,width=3)
    bu4.grid(row=10,column=3, padx=0, pady=0)
    bu5=tk.Button(tos,text='5', command=lambda: handle_button_click(5),height=2,width=3)
    bu5.grid(row=10,column=4, padx=0, pady=0)
    bu6=tk.Button(tos,text='6', command=lambda: handle_button_click(6),height=2,width=3)
    bu6.grid(row=10,column=5, padx=0, pady=0)
    bu7=tk.Button(tos,text='7', command=lambda:handle_button_click(7),height=2,width=3)
    bu7.grid(row=12,column=3, padx=0, pady=0)
    bu8=tk.Button(tos,text='8', command=lambda:handle_button_click(8),height=2,width=3)
    bu8.grid(row=12,column=4, padx=0, pady=0)
    bu9=tk.Button(tos,text='9', command=lambda:handle_button_click(9),height=2,width=3)
    bu9.grid(row=12,column=5, padx=0, pady=0)
    bu10=tk.Button(tos,text='10', command=lambda:handle_button_click(10),height=2,width=5)
    bu10.grid(row=14,column=4,padx=0, pady=0)
                            
    tos.mainloop()



l1=tk.Label(master=app,text='Lets Odd or Eve',font='Calibri 15 bold',fg="white",bg="black")
l1.pack()
#asking name
l2=tk.Label(app,text='What is your name??',bg="black",fg="magenta")
l2.pack(pady=8)
e_name=tk.Entry(app,)
e_name.pack()
#player name button
b1_name=tk.Button(app,text='Enter',command=change_b1_text)
b1_name.pack(pady=8)


