print("Enter the grade POINTS acc to your grades")
def cal_CGP(grades, credits):
        total_gradP=0
        total_credits=0

        for grade, credit in zip(grades, credits):
            total_gradP += grade*credit 
            total_credits += credit
            print(total_gradP)
            print(total_credits)
        if total_credits==0:
              return 0
        
        cgp= total_gradP / total_credits
        return cgp

def result():
        total_courses= int(input("enter the total number of subject: "))
        grades=[]
        credits=[]

        for i in range(total_courses):
            grade=float(input(f"Enter the grade of the subject {i+1}: "))
            credit=float(input(f"Enter the credit of the subject{i+1}: "))
            grades.append(grade)
            credits.append(credit)    
        cgp= cal_CGP(grades, credits)    
        print("your CGP is:",cgp)
        print(grades) 
        print(credits) 

result()
  
    



