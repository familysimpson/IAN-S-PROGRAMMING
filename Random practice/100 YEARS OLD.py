"""Create a program that asks the user their name and their age.
Print out a message addressed to them that tell them how many years that they will turn 100 years old """

#DECLARE name: STRING
#DECLARE age: INTEGER
#DECLARE future_age: INTEGER

name = str(input("Please enter your name"))
age = int(input("Please enter your age"))

future_years = 100 - age
print(name,"you will be 100 in",future_years, "years")