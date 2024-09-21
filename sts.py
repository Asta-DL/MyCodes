import random
score_comp=0
score_user=0
def check(user, comp):
    if (user==comp):
        return 0
    if (user==0 and comp==1):
        return -1
    if user==1 and comp==0:
        return 1
    if user==1 and comp==2:
        return -1
    if user==2 and comp==1:
        return 1
    if user==0 and comp==1:
        return 1
    if user==1 and comp==0:
        return -1
user=int(input("enter 0 for stone,1 for paper and 2 for scissor :"))
comp=random.randint(0,2)
print(comp)
score=check(user,comp)
if score==0:
    print("Its a draw")
elif score==1:
    score_user+=1
    print(score_user)
    print("you got a point")
    score_user=5
    print("You won the game")
else:
    score_comp+=1
    print(score_comp)
    print("Computer got a point")    
    score_comp=5
    print("You lose the game")    





    




           
    
