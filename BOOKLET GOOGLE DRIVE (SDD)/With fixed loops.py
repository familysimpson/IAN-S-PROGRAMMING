"""QUESTION 5 (PAGE 12)
A computer program is used to store a patient’s heart rate each day for a week.
The seven readings are stored in an array of real numbers called “bpm”.
Using Pseudocode or a programming language of your choice,
write a short program to calculate the average heart rate of the patient over the seven days.
"""

#DECLARE bpm: REAL
#DECLARE days: INTEGER
bpm = [float,float,float,float,float,float,float]
days = 7
bpm_total = 0.0
for counter in range (0,7):
    bpm[counter] = float(input(("Enter heart rate ")))

    bpm_total = bpm_total+ bpm[counter]
bpm_avg = bpm_total / days
print(bpm_avg)

