#Vargas, Ruben A.
#BSCPE 1-4
#Object-Oriented Programming

import pyfiglet

#Designs
print("\033[35m•\033[0m" * 58)
print("~" + "\033[;96;1;3mCodeperman\033[0m \033[;1;3mis on duty!\033[0m".center(81) + "~")
print("\033[35m•\033[0m" * 58)

#User's name
user_name = input(f"\n\033[;33;1;3mWhat is your name? \033[0m")
print(f"\n\033[;1;3mHey there, \033[;34;1;3m" + user_name + "\033[;1;3m!\033[0m")
print("\033[;33;1;3mHere's the student who got the highest GWA.\033[0m")
print("")

print("\033[35m•\033[0m" * 77)
print(pyfiglet.figlet_format("Congratulations!"))

#Set the initial lowest GWA value to 5.0
lowest_GWA = 5.0

#Create an empty list to hold the name(s) of the student(s) with the highest GWA
highest_student = []

#Open the txt file in read mode
with open("studentsGWA.txt", "r") as raw_file:

    #Loop through each line in the file
    for line in raw_file:

        #Split the line into student name and GWA, then convert the GWA to float
        student, gwa = line.strip().split(",")
        gwa = float(gwa)    
        
        #Check if the current GWA is lower than the current lowest GWA
        if gwa < lowest_GWA:
            #If so, update the variables
            lowest_GWA = gwa
            highest_student = student

    #Print the Outcome
    if lowest_GWA:
        print(f"\n\033[;33;1;3mThe student with the highest GWA is\033[0m \033[;96;1;3m{highest_student}\033[0m \033[;33;1;3mwith a GWA of\033[0m \033[;96;1;3m{lowest_GWA}\033[0m")
        print("")
        print("\033[35m•\033[0m" * 77)
    else:
        print("There were no student records in the provided file.")

print("")
print("\033[;33;1;3mThanks for your visit!\033[0m")
print("")
print("\033[35m•\033[0m" * 58)