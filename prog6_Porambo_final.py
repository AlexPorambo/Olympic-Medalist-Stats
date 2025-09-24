import csv

##################################################################
## Author: Alex Porambo                                         ##
## Major: Computer Science                                      ##
## Creation Date: December 1st, 2024                            ##
## Due Date: December 6th, 2024                                 ##
## Course: CS115-01                                             ##
## Professor Name: Professor Shimkanon                          ##
## Assignment: #6                                               ##
## Filename: prog6_Porambo_olympics.py                          ##
## Purpose: This program takes in the athletes.csv and          ##
## medalists.csv dataset and sorts it based on the user's       ##
## request. The user can short by atheletes from a certain      ##                 
## country, male to female ratio for each country, and male to  ##
## female medalist ratio for each country                       ##
##################################################################

###############################################################
## Function Name:     Fix_Athlete_List                       ##
## Description:       This function returns a list of        ##
##                    only Athlete names, gender, and Country##
## Parameters:        list: athletes                         ##
## Return Value:      list: SortedAthletes                   ##
###############################################################

def Fix_Athlete_List(athletes):
    
    SortedAthletes = []
    for i in range(len(athletes)):
        if athletes[i][1] == "True": # Removes False and irrelevant data 
            line = []
            line.append(athletes[i][4]) # Athlete's name
            line.append(athletes[i][5]) # Athlete's gender
            line.append(athletes[i][8]) # Athlete's country
            SortedAthletes.append(line)
        else:
            continue
    SortedAthletes = sorted(SortedAthletes, key=lambda x: x[2]) # Sorts list on country
    
    return SortedAthletes

###################################################################
## Function Name:     Fix_Medalists_List                         ##
## Description:       This function returns a list of the        ##
##                    Medalist's medal won, gender, and Country  ##
## Parameters:        list: medalists                            ##
## Return Value:      list: SortedMedalists                      ##
###################################################################

def Fix_Medalists_List(medalists):
    
    SortedMedalists = []
    for i in range(len(medalists)):
        if medalists[i][20] == "True": # Removes False and irrelevant data
            line = []
            line.append(medalists[i][2]) # Medal type
            line.append(medalists[i][4]) # Gender of Medalist
            line.append(medalists[i][6]) # country of medalist
            SortedMedalists.append(line)
        else:
            continue
        
    SortedMedalists = sorted(SortedMedalists, key=lambda x: x[2]) # Sorts list on country
    
    return SortedMedalists
    

###############################################################
## Function Name:     Find_Athletes_By_Country               ##
## Description:       This function returns a list of        ##
##                    only Athlete names from a Country that ##
##                    the user has inputed                   ##
## Parameters:        list: Athletes                         ##
##                    str: user_country                      ##
## Return Value:      list: country_grouped                  ##
###############################################################

def Find_Athletes_By_Country(Athletes, user_country):
    country_grouped = [] 
    
    for entry in Athletes:
        country = entry[2]  # Extract the country name from the entry
        if country == user_country: 
            country_grouped.append(entry[0]) # Adds Athlete name to list if they are from the requested country
            
    country_grouped = sorted(country_grouped, key=lambda x: x[0]) # Sorts first name in Alphabetical order for easier read
    
    return country_grouped

##################################################################
## Function Name:     M_to_F_ratio                              ##
## Description:       This function returns a dictionary of     ##
##                    of the males and females as well as the   ##
##                    male-to-female ratio for each country.    ##
##                    the user has inputed                      ##
## Parameters:        list: Athletes                            ##
## Return Value:      Dict: M_to_F_ratio (males, females, ratio)##
##################################################################

def M_to_F_ratio(Athletes):
    country_groups = {}
    
    for entry in Athletes: # counts the number of males and females to a country
        country = entry[2] 
        gender = entry[1]
        
        if country not in country_groups: # If country is not found in dictionary a new key is defined in dict
            country_groups[country] = {'Male': 0, 'Female': 0}  # Initialize counts
        
        # Increment gender count
        # Add a count for Male or Female in dictionary under the country
        if gender == 'Male': 
            country_groups[country]['Male'] += 1
        elif gender == 'Female':
            country_groups[country]['Female'] += 1

    # Calculate Male-to-Female ratio for each country
    M_to_F_ratio = {}
    for country, counts in country_groups.items():
        males = counts['Male']
        females = counts['Female']
        
        if females > 0 and males > 0: # Avoid division by zero and other unproportional ratios
            ratio = males / females
            
        else:
            ratio = "not possible"  # Catches division by zero would otherwise occur and unproportional ratios like (0:5)
          
        M_to_F_ratio[country] = (males, females, ratio)
        
    return M_to_F_ratio

##################################################################
## Function Name:     medal_ratio                               ##
## Description:       This function returns a dictionary of     ##
##                    of the males and females as well as the   ##
##                    male-to-female ratio for each country     ##
##                    for the specific medal the user inputed   ##
## Parameters:        list: Medalists                           ##
## Return Value:      Dict: M_to_F_ratio (males, females, ratio)##
##################################################################


def medal_ratio(Medalists, medal_code):
    medalist_groups = {}

    # Group medalists by country and gender
    for entry in Medalists:
        
            
        # Extract relevant fields
        medal_type = entry[0]  # Medal code (1.0, 2.0, 3.0)
        gender = entry[1]  # Gender of the athlete
        country = entry[2]  # Country name
    
        # Check if entry matches the medal code and is valid
        if medal_type == medal_code:
            if country not in medalist_groups: # If country is not found in dictionary a new key is defined in dict
                medalist_groups[country] = {'Male': 0, 'Female': 0}  # Initialize counts
    
            # Increment gender count
            if gender == 'Male':
                medalist_groups[country]['Male'] += 1
            elif gender == 'Female':
                medalist_groups[country]['Female'] += 1

    # Calculate Male-to-Female ratios
    M_to_F_ratio = {}
    for country, counts in medalist_groups.items():
        males = counts['Male']
        females = counts['Female']
    
        # Calculate ratio or assign infinity
        if females > 0 and males > 0: # Avoid division by zero
            ratio = males / females
            
        else:
            ratio = "not possible" # Catches division by zero would otherwise occur and unproportional ratios like (0:5)
                               
            
        M_to_F_ratio[country] = (males, females, ratio)
    
    return M_to_F_ratio

###############################################################
## Function Name:     main                                   ##
## Description:       Main function                          ##
## Parameters:        None                                   ##
## Return Value:      None                                   ##
###############################################################

if __name__ == '__main__':
    
    # -- READS CSV FILES -- #
    athletes = []
    with open('athletes.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for line in csvFile:
            athletes.append(line)
            
    medalists = []        
    with open('medallists.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for line in csvFile:
            medalists.append(line)
            
    # -- READS CSV FILES -- #
    
    print("Paris 2024 Olympics sorting Machine")
    user_opt = input("Please enter the number of one of the following:\n1: Athletes for a Country \n2: Male to Female ratio for each Country \n3: Male to Female medal ratio for each country \n4: Exit \n")
    
    while user_opt != "4": # Program will continuoly run until user enters 4
    
        # Remove unnecessary and false data before anything else
        Athletes = Fix_Athlete_List(athletes) 
        Medalists = Fix_Medalists_List(medalists)
        
        # Find Athletes from a country
        if user_opt == "1":
            user_country = input("Enter a Valid Country or enter BACK:\n")
            while user_country != "BACK":
                
                country_data = Find_Athletes_By_Country(Athletes, user_country)
                
                print(f"{user_country}:")
                for entry in country_data:
                    print(f"{entry}")
            
                user_country = input("Enter a Valid Country or enter 'BACK':\n")  
      
        # Find Male to Female ratio for all Countries
        elif user_opt == "2":
            Ratio = M_to_F_ratio(Athletes)
            
            for country, stats in Ratio.items():
                males, females, ratio = stats
                print(f"---{country}---")
                print(f"Males - {males}")
                print(f"Females - {females}")
                
                # Check if the ratio is a valid number or not possible
                if ratio != "not possible":
                    print(f"Ratio - {ratio:.3f}\n")
                else:
                    print("Ratio - Not possible\n")
          
        # # Find Male to Female medalist ratio for all Countries     
        elif user_opt == "3":
            user_medal_option = input("Medal Option Please Enter: \n1: Gold \n2: Silver \n3: Bronze \n4: Back \n")
            
            
            while user_medal_option != "4":
                
                # Gold medal option
                if user_medal_option == "1":
                    medal_code = "1.0" 
                    
                    Ratio = medal_ratio(Medalists, medal_code)
                    
                    for country, stats in Ratio.items():
                        males, females, ratio = stats
                        print(f"---{country}---")
                        print(f"Males - {males}")
                        print(f"Females - {females}")
                        
                        # Check if the ratio is a valid number or not possible
                        if ratio != "not possible":
                            print(f"Ratio - {ratio:.3f}\n")
                        else:
                            print("Ratio - Not possible\n")
                            
                    break # Returns user to main menu after one interation
                  
                # Silver Medal option    
                elif user_medal_option == "2":
                    medal_code = "2.0"
                    
                    Ratio = medal_ratio(Medalists, medal_code)
                    
                    for country, stats in Ratio.items():
                        males, females, ratio = stats
                        print(f"---{country}---")
                        print(f"Males - {males}")
                        print(f"Females - {females}")
                        
                        # Check if the ratio is a valid number or not possible
                        if ratio != "not possible":
                            print(f"Ratio - {ratio:.3f}\n")
                        else:
                            print("Ratio - Not possible\n")
                            
                    break # Returns user to main menu after one interation
                 
                # Bronze Medal option    
                elif user_medal_option == "3":
                    medal_code = "3.0"
                    
                    Ratio = medal_ratio(Medalists, medal_code)
                    
                    for country, stats in Ratio.items():
                        males, females, ratio = stats
                        print(f"---{country}---")
                        print(f"Males - {males}")
                        print(f"Females - {females}")
                        
                        # Check if the ratio is a valid number or not possible
                        if ratio != "not possible":
                            print(f"Ratio - {ratio:.3f}\n")
                        else:
                            print("Ratio - Not possible\n")
                    
                    break # Returns user to main menu after one interation
        
                else:
                    user_medal_option = input("Please enter a number 1-4\n") # Catches input that is not valid 
                    
                    
             
                
            
                        
                    
        user_opt = input("Please enter the number of one of the following:\n1: Athletes for a Country \n2: Male to Female ratio for each Country \n3: Male to Female medal ratio for each country \n4: Exit \n")
            