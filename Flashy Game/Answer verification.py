
#DECLARE AnsVerify: BOOLEAN
#DECLARE User_Ans: STRING
#DECLARE Answer: STRING #insert answer from file (FINN)

Answer = "A compiler is a type of translator " #This will be answer from file
Ans_Verify = False
Count = 0
print(Answer)

User_ans = str(input("Please enter YES if you achieved the correct answer and please enter NO if you achieved the incorrect answer:"))
while User_ans != "NO" and User_ans != "YES":
    print("Please type in either YES or NO")
    User_ans = str(input("Please enter YES if you achieved the correct answer and please enter NO if you achieved the incorrect answer:"))

if User_ans == "YES":
    Ans_Verify = True
    Count = Count + 1
    print("Well done you have 1 more point")
elif User_ans == "NO" or User_ans == "no" or User_ans == "No":
    Ans_Verify = False
    print("Don't worry just try again.")

Grade