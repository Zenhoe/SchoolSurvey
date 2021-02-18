f = open("SurveyResult.txt", "w+")
Names = [f.readline([20])]
Age = [f.readline([20])]
Q_One = [f.readline([20])]
Q_Two = [f.readline([20])]
Q_Three = [f.readline([20])]
Q_Four = [f.readline([20])]
surinput = input("Are you ready for the survey")


def questions():
    Name = input("Ok to start with, what is your name: ")
    Names.append(Name)
    AgeQ = input("How old are you: ")
    Age.append(AgeQ)
    print("Please say if you have heard of it before or played it")
    Q_Onee = input("Ok now the real questions, have you ever played or heard of Minecraft(Yes or No): ")
    Q_One.append(Q_Onee)
    Q_Twoo = input("Have you ever played or heard of Dark souls(Yes or No): ")
    Q_Two.append(Q_Twoo)
    Q_Threee = input("Have you ever played or heard of Super Smash Bros(Yes or No): ")
    Q_Three.append(Q_Threee)
    Q_Fourr = input("Have you ever played or heard of Skate 3(Yes or No): ")
    Q_Four.append(Q_Fourr)
    f.writellines(Names)
    f.writelines(Age)
    f.writelines(Q_One)
    f.writelines(Q_Two)
    f.writelines(Q_Three)
    f.writelines(Q_Four)

def results():
    f.read()

if surinput == "Results":
    results()
if surinput == "Yes":
    questions()
if surinput == "No":
    pass

f.close()