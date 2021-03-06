## @file calc.py
# @author Ondřej Chromý, David Klajbl
# @brief Calculator GUI
# @version 0.4
# @date 2022-04-28

from .exp_parser import exp_parse
from .exp_parser import exp_eval
import os
from tkinter import *
import webbrowser


expression = ""

def showman():
    webbrowser.open_new(os.path.dirname(os.path.realpath(__file__)) + "/dokumentace.pdf")

def addtoExpression(num):
    global expression
    expression = expression + str(num)
    textbox.set(expression)
 
def equal():
    global expression

    final_expression = str(expression)
    
    try:
        exp_list = exp_parse.parse_expression(final_expression)
    
    except:
        textbox.set("InvalidExpression")
        final_expression = ""
        expression = ""
    
    else:    
        result = exp_eval.eval_expression(exp_list)    

        try:
            # test if result is float
            float(result)
            
            if result.find('e') != -1:
                result = "OverflowError"
                raise OverflowError()
            
               
            if result.find('.') == -1: 
                if len(result) > 22:
                    result = "OverflowError"
                    raise OverflowError()
            
            else:
                splitRes = result.split('.', 1)
                if len(splitRes[0]) >= 22:
                    result = "OverflowError"
                    raise OverflowError()
                elif len(result) <= 22:
                    result = str(splitRes[0] + '.' + splitRes[1][:10]) 
                    pass
                elif len(splitRes[1]) > 20-len(splitRes[0]):
                    result = str(splitRes[0] + '.' + splitRes[1][:10])
                    result = result[0:21] 
                    pass
                else:
                    result = "OverflowError"
                    raise OverflowError()
        
        except:
            textbox.set(result)
            final_expression = ""
            expression = ""

        else:
            textbox.set(result)
            expression = result
        
def c():
    global expression
    expression = ""
    textbox.set("")
    
def qt():
    exit()


    
calcapp = Tk()

img = PhotoImage(file = (os.path.dirname(os.path.realpath(__file__))+ "/calculateit_icon.gif"))
calcapp.iconphoto(False, img)

calcapp.configure(background="#AEA79F")
calcapp.title("CalculateIT Calculator")
calcapp.geometry("414x338")
calcapp.minsize(414, 338)
calcapp.maxsize(414, 338)

textbox = StringVar()
expression_field = Entry(calcapp, font=("Arial 19"),fg='#FFFFFF', bg='#080808', textvariable = textbox, state=DISABLED, disabledbackground='#080808', disabledforeground='#FFFFFF', width=22)
expression_field.grid(columnspan=4)

#button to open "help" (manual)
helpButton = Button(calcapp, text='?', command=lambda: showman(), fg='black', bg='#AEA79F', height=2 , width=6)
helpButton.grid(row=0, column=4)
calcapp.bind('h', lambda event: showman())


#number buttons
button1 = Button(calcapp, text='7', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('7'), height=2, width=7)
button1.grid(row=3, column=0)
calcapp.bind('<KP_7>', lambda event: addtoExpression('7'))
calcapp.bind('7', lambda event: addtoExpression('7'))

button2 = Button(calcapp, text='8', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('8'), height=2, width=7)
button2.grid(row=3, column=1)
calcapp.bind('<KP_8>', lambda event: addtoExpression('8'))
calcapp.bind('8', lambda event: addtoExpression('8'))

button3 = Button(calcapp, text='9', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('9'), height=2, width=7)
button3.grid(row=3, column=2)
calcapp.bind('<KP_9>', lambda event: addtoExpression('9'))
calcapp.bind('9', lambda event: addtoExpression('9'))

button4 = Button(calcapp, text='4', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('4'), height=2, width=7)
button4.grid(row=4, column=0)
calcapp.bind('<KP_4>', lambda event: addtoExpression('4'))
calcapp.bind('4', lambda event: addtoExpression('4'))

button5 = Button(calcapp, text='5', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('5'), height=2, width=7)
button5.grid(row=4, column=1)
calcapp.bind('<KP_5>', lambda event: addtoExpression('5'))
calcapp.bind('5', lambda event: addtoExpression('5'))

button6 = Button(calcapp, text='6', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('6'), height=2, width=7)
button6.grid(row=4, column=2)
calcapp.bind('<KP_6>', lambda event: addtoExpression('6'))
calcapp.bind('6', lambda event: addtoExpression('6'))

button7 = Button(calcapp, text='1', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('1'), height=2, width=7)
button7.grid(row=5, column=0)
calcapp.bind('<KP_1>', lambda event: addtoExpression('1'))
calcapp.bind('1', lambda event: addtoExpression('1'))

button8 = Button(calcapp, text='2', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('2'), height=2, width=7)
button8.grid(row=5, column=1)
calcapp.bind('<KP_2>', lambda event: addtoExpression('2'))
calcapp.bind('2', lambda event: addtoExpression('2'))

button9 = Button(calcapp, text='3', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('3'), height=2, width=7)
button9.grid(row=5, column=2)
calcapp.bind('<KP_3>', lambda event: addtoExpression('3'))
calcapp.bind('3', lambda event: addtoExpression('3'))

button0 = Button(calcapp, text='0', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('0'), height=2, width=7)
button0.grid(row=6, column=0)
calcapp.bind('<KP_0>', lambda event: addtoExpression('0'))
calcapp.bind('0', lambda event: addtoExpression('0'))

buttonpi = Button(calcapp, text='π', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('π'), height=2, width=7)
buttonpi.grid(row=6, column=2)
calcapp.bind('p', lambda event: addtoExpression('π'))

buttone = Button(calcapp, text='e', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('e'), height=2, width=7)
buttone.grid(row=7, column=2)
calcapp.bind('e', lambda event: addtoExpression('e'))

#operation buttons 
plus = Button(calcapp, text='+', fg='black', bg='#E95420',
command=lambda: addtoExpression('+'), height=2, width=7)
plus.grid(row=6, column=3, rowspan = 2, ipady = 24)
calcapp.bind('<KP_Add>', lambda event: addtoExpression('+'))
calcapp.bind('+', lambda event: addtoExpression('+'))

minus = Button(calcapp, text='-', fg='black', bg='#E95420',
command=lambda: addtoExpression('-'), height=2, width=7)
minus.grid(row=5, column=3)
calcapp.bind('<KP_Subtract>', lambda event: addtoExpression('-'))
calcapp.bind('-', lambda event: addtoExpression('-'))

multiply = Button(calcapp, text='×', fg='black', bg='#E95420',
command=lambda: addtoExpression('*'), height=2, width=7)
multiply.grid(row=4, column=3)
calcapp.bind('<KP_Multiply>', lambda event: addtoExpression('*'))
calcapp.bind('*', lambda event: addtoExpression('*'))

divide = Button(calcapp, text='÷', fg='black', bg='#E95420',
command=lambda: addtoExpression('/'), height=2, width=7)
divide.grid(row=3, column=3)
calcapp.bind('<KP_Divide>', lambda event: addtoExpression('/'))
calcapp.bind('/', lambda event: addtoExpression('/'))

equals = Button(calcapp, text='=', fg='black', bg='#E95420',
command=lambda: equal(), height=12, width=6)
equals.grid(row=3, column=4, rowspan=5, ipady=11)
calcapp.bind('<Return>', lambda event: equal())
calcapp.bind('<KP_Enter>', lambda event: equal())

clear = Button(calcapp, text='C', fg='black', bg='#AEA79F',
command=lambda: c(), height=2, width=7)
clear.grid(row=2, column=0)
calcapp.bind('<BackSpace>', lambda event: c())
calcapp.bind('<Delete>', lambda event: c()) 
    
decimal= Button(calcapp, text='.', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('.'), height=2, width=7)
decimal.grid(row=6, column=1)
calcapp.bind('<KP_Decimal>', lambda event: addtoExpression('.'))
calcapp.bind('.', lambda event: addtoExpression('.'))

modulo= Button(calcapp, text='mod', fg='black', bg='#E95420',
command=lambda: addtoExpression('%'), height=2, width=6)
modulo.grid(row=2, column=4)
calcapp.bind('%', lambda event: addtoExpression('%'))

power= Button(calcapp, text='^', fg='black', bg='#E95420',
command=lambda: addtoExpression('^'), height=2, width=7)
power.grid(row=2, column=1)
calcapp.bind('^', lambda event: addtoExpression('^'))

root= Button(calcapp, text='√', fg='black', bg='#E95420',
command=lambda: addtoExpression('^(1/'), height=2, width=7)
root.grid(row=2, column=2)

factorial= Button(calcapp, text='!', fg='black', bg='#E95420',
command=lambda: addtoExpression('!'), height=2, width=7)
factorial.grid(row=2, column=3)
calcapp.bind('!', lambda event: addtoExpression('!'))

#brackets
bracketR= Button(calcapp, text=')', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression(')'), height=2, width=7)
bracketR.grid(row=7, column=1)
calcapp.bind(')', lambda event: addtoExpression(')'))

bracketL= Button(calcapp, text='(', fg='#FFFFFF', bg='#333333',
command=lambda: addtoExpression('('), height=2, width=7)
bracketL.grid(row=7, column=0)
calcapp.bind('(', lambda event: addtoExpression('('))

#exit the app on esc press
calcapp.bind('<Escape>', lambda event: qt())
    
def main():
    calcapp.mainloop()

if __name__ == "__main__":
    main()
