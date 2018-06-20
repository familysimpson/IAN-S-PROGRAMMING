
#DECLARE AnsVerify: BOOLEAN
#DECLARE User_Ans: STRING
#DECLARE Answer: STRING #insert answer from file (FINN)
Question = "Is a compiler a type of translator?"
Answer = "A compiler is a type of translator " #This will be answer from file
Ans_Verify = False
Count = 0
print(Question)
print(Answer)

User_ans = str(input("Please enter 'y' if you achieved the correct answer and please enter 'n' if you achieved the incorrect answer:"))
while User_ans != "n" and User_ans != "y":
    print("Please type in either 'y' or 'n'")
    User_ans = str(input("Please enter 'y' if you achieved the correct answer and please enter 'n' if you achieved the incorrect answer:"))

if User_ans == "y":
    Ans_Verify = True
    Count = Count + 1
    print("Well done you have 1 more point")
elif User_ans == "n":
    Ans_Verify = False
    print("Don't worry just try again.")

