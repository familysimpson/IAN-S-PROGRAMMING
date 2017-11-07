#train tickets
#declare seatNo : INTEGER
#declare numberOfSeats : INTEGER
#declare carriage : CHAR
carriage = input("Enter the train carriage letter:")
numberOfSeats = int(input("Enter total number of seats:"))
for seatNo in range(1,numberOfSeats+1):
    print(carriage,seatNo)