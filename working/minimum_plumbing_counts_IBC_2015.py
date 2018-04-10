#imports
import math

#Start of program, initial display text
print("IBC-2015 | 'Minimum Plumbing Facilities Calculator' |")
print("Program running...")
print("______________________________________")

#Here the user inputs building classification. Once a valid classification is entered, the while loop will break and ask for the building occupancy.
while True:
    classification = input("|Assembly, Business, Educational, Factory and Industrial, Institutional, Mercantile, Residential, Storage|\nEnter building classification: ")
    classification = classification.lower()
    #Education
    if classification == "educational":
        print("You entered", classification.title(), "as your building classification.")
        print("______________________________________")
        break
    #Business
    elif classification == "business":
                print("You selected Business")
                break
    #Invalid classification input, else statment will instruct user to try again.
    else:
        print("______________________________________")
        print("Please enter a valid building classification.")
        print("______________________________________")
  
#Here, depending on the building classification, the user is asked to input the correct occupancy.        
while True:
    #Education
    if classification == "educational":
        while classification == "educational":
            occupancy = input("Educational occupancy options |E|\nEnter building occupancy: ")
            occupancy = occupancy.upper()
            #Education, E
            if occupancy == "E":
                print("You entered,", occupancy.upper() + ", as your building occupancy.")
                print("______________________________________")
                
                #Here the user inputs the population of their building.                
                population = input("Enter the population of your building: ")
                population = int(math.ceil(int(population)))
                populationMale = int(math.ceil(population / 2))
                populationFemale = int(math.ceil(population / 2))
                
                #Urinals can replace no more than 0.67% of total male toilets.
                toiletTotalMale = int(populationMale / 50)
                urinalMale = int(math.floor(toiletTotalMale * 0.67))
                toiletMale = int(toiletTotalMale - urinalMale)
                toiletFemale = int(populationFemale / 50)
                
                lavatoryMale = int(populationMale / 100)
                lavatoryFemale = int(populationFemale / 100)
                
                drinkingFountain = int(population / 100)
                
                #The program spits out the correct restroom calcs here based off of the population that the user entered.       
                print("______________________________________________________________________________")
                print("According to IBC 2015 | Chapter 29 | Section 2902 'Minimum Plumbing Facilities'")
                print("The minimum plumbing counts for your building are as follows...")
                print("______________________")
                print("Classification:", classification.title())
                print("Occupancy:", occupancy.upper())
                print("______________________")
                print("Population:", population)
                print("Males:", populationMale)
                print("Females:", populationFemale)
                print("______________________")
                print("Male Toilets:", toiletMale)
                print("Male Urinals:", urinalMale)
                print("Female Toilets:", toiletFemale)
                print()
                print("Male Lavatories:", lavatoryMale)
                print("Female Lavatories:", lavatoryFemale)
                print()
                print("Drinking Fountains:", drinkingFountain)
                print()
                print("Service Sinks: 1")
                print("______________________")
                
                break
            #If the user inputs an invalid occupancy, this else statement will redirect them to try again.
            else:
                print("Sorry, that is not a valid occupancy for this building classification")
                print("______________________________________")
    #Business
    elif classification == "business":
        while classification == "business":
            occupancy = input("Business occupancy options |B|\nEnter building occupancy: ")
            occupancy = occupancy.upper()
        #Business, 
            if occupancy == "B":
                print("You entered,", occupancy.upper() + ", as your building occupancy.")
                
                #Here the user inputs the population of their building.                
                population = input("Enter the population of your building: ")
                population = int(math.ceil(int(population)))
                populationMale = int(math.ceil(population / 2))
                populationFemale = int(math.ceil(population / 2))
                
                #Urinals can replace no more than 0.67% of total male toilets.
                toiletTotalMale = int(populationMale / 50)
                urinalMale = int(math.floor(toiletTotalMale * 0.67))
                toiletMale = int(toiletTotalMale - urinalMale)
                toiletFemale = int(populationFemale / 50)
                
                lavatoryMale = int(populationMale / 100)
                lavatoryFemale = int(populationFemale / 100)
                
                drinkingFountain = int(population / 100)
            
                #The program spits out the correct restroom calcs here based off of the population that the user entered.       
                print("______________________________________________________________________")
                print("According to IBC 2015 | Chapter 29 | Section 2902 'Minimum Plumbing Facilities'")
                print("The minimum plumbing counts for your building are as follows...")
                print("______________________")
                print("Classification:", classification.title())
                print("Occupancy:", occupancy.upper())
                print("______________________")
                print("Population:", population)
                print("Males:", populationMale)
                print("Females:", populationFemale)
                print("______________________")
                print("Male Toilets:", toiletMale)
                print("Female Toilets:", toiletFemale)
                print("______________________")
                print("Male Lavatories:", lavatoryMale)
                print("Female Lavatories:", lavatoryFemale)
                print("______________________")
                print("Drinking Fountains:", drinkingFountain)
                print("______________________")
                print("Service Sinks: 1")
                
                break
             #If the user inputs an invalid occupancy, this else statement will redirect them to try again.
            else:
                print("Sorry, that is not a valid occupancy for this building classification")
                print("______________________________________")
    #End Program
    break
