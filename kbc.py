import os
import time

# Creating a KBC game
print("Hello Contestant, Welcome to KBC")
name=input("Enter your Name: ")
print("Greetings,",name,"Let's start your quest to become a millionaire\n")

#Rules
print("Rules of the Game:")
print("1. There will be 5 question and four options for each question.")
print("2. You have to enter the answer as option A/B/C/D .")
print("3. Type E if you wish to end the game")
print("4. If you answer a question incorrectly you will get nothing")
print("5. Galat answer par gandi gaaliyan bhi di jayengi\n\n")

#Prompt for are you ready
st=input("Are you ready(Answer in y/n) :")
if(st.upper()=="N"):
    # print("The contest has ended. Go fuck yourself")
    exit("The contest has ended. Go fuck yourself")
os.system('cls')
print("The contest will start in 5 seconds")
time.sleep(5)
os.system('cls')

#The part for questions and answers
questions=("Which country invaded Ukraine recently?","What is ranking of India in World's largest countrty Area-Wise?","How many Union-Territories are there in India?","Who is the author of Harry Potter?","Since its inception, which category of the Nobel Prize has been awarded every single year?")
options=(("China","Russia","North-Korea","USA"),("Fourth","Fifth","Sixth","Seventh"),("6","7","8","9"),("Dan Brown","JK Rowling","Mark Twain","Tim Allen"),("Chemistry","Physics","Peace","Economics"))
answer=("B","D","C","B","D")
galli=("Bhag ja saale Muthbaaz","Ye lo saande ka tel isko laga k ulta let jao","Dhat.. teri maa ki chut ","Apko prize me lauda diya jayega","Bhosdike Madarchod Behen-ke-lode, Jhattu Maa ki chut teri, Tatto ke Saudagar")

prize=1000
for i,ques in enumerate(questions):
    print("For",prize,"rupees,")
    print("Question",i+1,"-",ques)
    print("A.",options[i][0])
    print("B.",options[i][1])
    print("C.",options[i][2])
    print("D.",options[i][3],"\n")
    ans=input("Enter your answer as A/B/C/D or E if you wish to end the game: ")
    print("\n")
    if(ans.upper()==answer[i]):
        if(i==4):
            print("Congratulation",name,"Aap ban gye h crorepati!")
            break
        print("Correct answer, you win",prize,"rupees.\n")
    elif(ans.upper()=="E"):
        if(i==0):
            print("You win Nothing, Game ends here for you son of a bitch")
            exit()
        else:
            print("Congratulations",name,"You win",prize,"rupees")
            print("Game ends here!!")
            exit()
    else:
        print("Got you bitch!! Wrong answer, You win nothing")
        print(galli[i])
        exit("Game ends here!!")
    if(i!=4):
        print("Next question will apear in 5 seconds..\n")
        time.sleep(5)
        os.system('cls')
    prize=prize*10

print("\nYOU ARE THE CHAMPION!!!")


