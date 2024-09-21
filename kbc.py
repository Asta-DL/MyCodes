print("Lets begin our Junior KBC show")
name=input("Enter your name: ")
print(f"welcome {name}")
questions = [
    [
        "How many legs a elephant have ?",4,5,3,2,1
    ],
    [
        "Which city is known as Pink city: ", "Jalandhar", "Patiala", "Jaipur","Goa",3
    ],
    [
        "Clossest planet to the sun ?", "mars","mercury","earth","venus",2
    ],
    [
        "How many teeths a mosquito have ?",42,78,"none",47,4
    ],
    [
        "Which among these is not a language ?", "Python","Java","Microsoft","C++",3
    ],
    [
        "In which year India won the one day world cup",2011,2007,1998,2024,1
    ],
    [
        "Capital of India is: ","Pathankot","Ludhiana","Jammu","Delhi",4
    ],
    [
        "Which is the trending number one anime presently?","Naruto","One peice","Black clover","Slime",2
    ]
]
reward=[1000,2000,5000,10000,25000,75000,150000,300000,500000]
money = 0

for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs.{reward[i]}")
    print(question[0])
    print(f"a. {question[1]}\tb. {question[2]}\nc. {question[3]}\td. {question[4]}")
    answer=int(input("Enter your answer: "))
    if (answer == question[-1]):
        print(f"Your answer is correct\nyou have won Rs.{reward[i]}")
        if i==2:
            money=reward[2]
        elif i==5:
            money=reward[5]
        elif i==8:
            money=reward[8]        
    else:
        print("Wrong answer")
        print(f"{name},Your current total money is {money}")
        break
print(f"{name} have won Rs.{money} as his total")
print("Meri asha h ke aap apni iss dhanrashi ka istemal achhe kaam mein kre")
