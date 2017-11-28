# declare
number1 = 8
number2 = 16
result = number1 + number2
print("What is",number1,"+",number2,"?")
answer = int(input())
while answer != result:
    print("Incorrect - retry")
    answer = int(input())
print("Correct!")