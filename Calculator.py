import re

print("Magical calculator")
print("type 'quit' to exit\n")

previous=0
run = True

def performMaths():
    global run
    global previous
    equation =""
    if previous == 0:
       equation=input("Enter equation:")
    else:
        equation=input(str(previous))

    if (equation == 'quit'):
        print("Goodbye,Buddy")
        run= False
    else:
        equation=re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous=eval(equation)
        else:
            previous = eval(str(previous)+equation)


while run:
    performMaths()