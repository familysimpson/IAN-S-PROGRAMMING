"""Snow day problem
There are 10 schools in the borough of barnet
Each school has a student capacity and a measurement for the depth of snow
1)Each school enters the capacity(%) and enter the depth of snow (cm)
2)Calculate which schools should stay open
3)List each school by number to say whether the school is open or closed"""

School_Array = ["","","","","","","","","",""]

School_Array[0] = "Queen Eliazbeth Girls School"
School_Array[1] = "Queen Elizabeth Boys School"
School_Array[2] = "St Michaels Girls School"
School_Array[3] = "Ashmole academy"
School_Array[4] = "Wren academy"
School_Array[5] = "Frien Barnet School"
School_Array[6] = "Finchley Catholic high school"
School_Array[7] = "East Barnet High School"
School_Array[8] = "Henrietta Barnet"
School_Array[9] = "Dame Alice Owen"

school_capacity = [float,float,float,float,float,float,float,float,float,float]
measurement_snow= [float,float,float,float,float,float,float,float,float,float]

for counter in range(0,10):
    print(School_Array[counter])
    school_capacity = float(input("What is the capacity of students today(%)"))
    measurement_snow = float(input("What is the measurement of snow at your school"))

    if school_capacity > 25.0:
        Gates_open = "CLOSE YOUR SCHOOL!"
        print(Gates_open)
        if measurement_snow >= 2.5:
            Gates_open = "CLOSE YOUR SCHOOL!"
            print(Gates_open)
        else:
            Gates_open = "OPEN YOUR SCHOOL!"
            print(Gates_open)