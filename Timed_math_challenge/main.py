import random 
import time


MIN_OPERAND=3
MAX_OPERAND=12
OPERATORS=['+','-','*']
TOTAL_PROBLEMS=10


start=input("Press Enter to start")
start_time=time.time()
print("--------------------------------------")
question_count=1
mistakes=0

if start=="":
    for i in range(TOTAL_PROBLEMS):
        operand_1=random.randint(MIN_OPERAND,MAX_OPERAND)
        operand_2=random.randint(MIN_OPERAND,MAX_OPERAND)
        operator=random.choice(OPERATORS)

        expression_result=eval(f"{operand_1}{operator}{operand_2}")

        while question_count<=TOTAL_PROBLEMS:
            try:
                answer=int(input(f"#{question_count} : {operand_1} {operator} {operand_2} : "))
            
                if answer==expression_result:
                    print("Correct !.")
                    question_count+=1
                    break
                else:
                    print("Wrong!")
                    mistakes+=1
                    continue
            except ValueError:
                print("Invalid answer please try again !.")
                continue
else:
    print("Inavalid selection please try again by pressing Enter !..")

end_time=time.time()

if question_count>TOTAL_PROBLEMS:
    print(f"You have solved in {round(end_time-start_time,1)} seconds !. with {mistakes} mistakes")


