print("welcome  to my computer quizz!")

playing=input("do you want to play?")
score=0

if playing.lower() !="yes":
    quit()
    
print("okay,lets play")   

answer=input("what does cpu stands for ?")
if answer.lower() =="central proccessing unit":
    print("correct")
    score == 1
else:
    print("incorrect")    

answer=input("what does gpu stands for ?")
if answer.lower() =="graphics proccessing unit":
    print("correct")
    score == 1
else:
    print("incorrect")    

answer=input("what does RAM stands for ?")
if answer.lower() =="random access memory":
    print("correct")
    score == 1
else:
    print("incorrect")

answer=input("what does psu stands for ?")
if answer.lower() =="power supply":
    print("correct")
    score == 1
else:
    print("incorrect")  

print("you got"+str(score)+"questions  correct")   
print("you got"+str(score/4)*100+"%")   





