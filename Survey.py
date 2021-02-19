f = open("SurveyResult.txt", "a+")

surinput = input("Are you ready for the survey: ")


def questions():
    Name = input("Ok to start with, what is your name: ")
    AgeQ = input("How old are you: ")
    print("Please say if you have heard of it before or played it")
    Q_Onee = input("Ok now the real questions, have you ever played or heard of Minecraft(Yes or No): ")
    Q_Twoo = input("Have you ever played or heard of Dark souls(Yes or No): ")
    Q_Threee = input("Have you ever played or heard of Super Smash Bros(Yes or No): ")
    Q_Fourr = input("Have you ever played or heard of Skate 3(Yes or No): ")
    f.write(Name + "\n")
    f.write(AgeQ + "\n")
    f.write(Q_Onee  + "\n")
    f.write(Q_Twoo + "\n")
    f.write(Q_Threee + "\n")
    f.write(Q_Fourr + "\n")

def results():
    f = open("SurveyResult.txt", "r")
    print(f.read())
    
    

if surinput == "Results":
    results()
if surinput == "Yes":
    questions()
if surinput == "No":
    pass

f.close()