#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

#Set the initial lowest GWA value to 5.0
lowest_GWA = 5.0
#Create an empty list to hold the name(s) of the student(s) with the highest GWA
highest_student = []
#Open the txt file in read mode
with open("studentsGWA.txt", "r") as raw_files:
    #Loop through each line in the file
    for line in raw_files:
        #Split the line into student name and GWA, then convert the GWA to float
        #Check if the current GWA is lower than the current lowest GWA
    #Print the Outcome