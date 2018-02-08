"""QUESTION 5 (PAGE 12)
A computer program is used to store a patient’s heart rate each day for a week.
The seven readings are stored in an array of real numbers called “bpm”.
Using Pseudocode or a programming language of your choice,
write a short program to calculate the average heart rate of the patient over the seven days.
"""

#DECLARE bpm: ARRAY[0:7] OF REAL
#DECLARE days: INTEGER
bpm = [float,float,float,float,float,float,float]

days = 7

bpm [0] = 80.1
bpm [1] = 80.1
bpm [2] = 80.1
bpm [3] = 80.1
bpm [4] = 80.1
bpm [5] = 80.1
bpm [6] = 80.1

sum = sum(bpm[0:7])
avg_hrt_rate = sum / days
print(avg_hrt_rate)

