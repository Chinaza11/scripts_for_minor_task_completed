#! /usr/bin/env Python3

"""
Created on Thu Oct 19 16:02:12 2023

@author: Chinaza 

Password Generator
"""

import random, sys, os

#to check the current working directory
print(os.getcwd())

#to change the directory
os.chdir("G:/My Drive/school_and_programming/scripts_for_minor_task_completed")

print(os.getcwd())

#----------------------------------------------------------------------------------------------------

#creating a function that makes a password that comprises of random characters
def random_characters():
    
    while True:
    
        #creating variables for the alphabets, numbers, and symbols
        alphabets = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        symbols = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ":", ";", "<", ">", ",", ".", "?", "/", "~", "`")
        
        #creating empty variables that would be used later in the loop for storing random selection of possible passwords and the final password
        random_selection = ""
        password = ""
        
        try:
            character_set = int(input("What character set do you want for your password?\nEnter 1 for only alphanumeric and 2 for alphanumeric + symbols: "))
            
            #this if statement runs if the user decides that they want a password that comprises of alphanumeric only
            if character_set == 1:
                
                while True:
                    try:
                        password_range = int(input("How many characters do you want your password to be (password must be at least 3 characters long, however, to make a fairly strong password, it is advisable that it is at least 6 characters long)? "))
                        
                        if password_range >2: #making sure characters selected by the user is at least 3
                            
                            #loop creates a random selection of alphabets and numbers with length that is twice what the user entered
                            for i in range(password_range):
                                
                                #this randomly selects an alphabet
                                random_position1 = random.randint(0, len(alphabets)-1)
                                random_alphabet = alphabets[random_position1]
                                random_selection += random_alphabet
                                
                                #this randomly selects a number
                                random_position2 = random.randint(0, len(numbers)-1)
                                random_number = numbers[random_position2]
                                random_selection += random_number
                    
                            random_selection2 = list(random_selection) #making the selection a list so final password can be picked from it
                    
                            #loop makes selection from the previously randomly selected alphabets and numbers. this becomes the final password. Length is exactly what the user inputed.
                            for i in range(password_range):
                                password += random_selection2[random.randint(0, len(random_selection2)-1)]
                        
                            print(f"Your new password is: {password}")
                        
                        else:
                            print("Invalid entry: password must be at least 3 characters long")
                            continue
                        
                    except ValueError:
                        print("Invalid entry, try again. Entry must be an integer and password must be at least 3 characters long")
                        
                    else:
                        break
                
            
            #this if statement runs if the user decides that they want a password that comprises of alphanumeric and symbols
            elif character_set == 2:
                
                while True:
                    try:
                        password_range = int(input("How many characters do you want your password to be (password must be at least 3 characters long, however, to make a fairly strong password, it is advisable that it is at least 6 characters long)? "))
                        
                        if password_range > 2: #making sure characters selected by the user is at least 3
                            
                            #loop creates a random selection of alphabets, numbers and symmbols with length that is twice what the user entered
                            for i in range(password_range):
                        
                                #this randomly selects an alphabet
                                random_position1 = random.randint(0, len(alphabets)-1)
                                random_alphabet = alphabets[random_position1]
                                random_selection += random_alphabet
                                
                                #this randomly selects a number
                                random_position2 = random.randint(0, len(numbers)-1)
                                random_number = numbers[random_position2]
                                random_selection += random_number
                                
                                #this randomly selects a symbol
                                random_position3 = random.randint(0, len(symbols)-1)
                                random_symbol = symbols[random_position3]
                                random_selection += random_symbol
                    
                            random_selection2 = list(random_selection) #making the selection a list so final password can be picked from it
                            
                            #loop makes selection from the previously randomly selected alphabets, numbers and symbols, this becomes the final password. Length is exactly what the user inputed.
                            for i in range(password_range):
                                password += random_selection2[random.randint(0, len(random_selection2)-1)]
                                
                            print(f"Your new password is: {password}")
                        
                        else:
                            print("Invalid entry: password must be at least 3 characters long")
                            continue
                    
                    except ValueError:
                        print("Invalid entry, try again. Entry must be an integer and password must be at least 3 characters long")
                    
                    else:
                        break
                    
            elif character_set != 1 or 2:
                print("Invalid choice; You can only pick from 1 or 2")
                continue
                    
            while True:
                try:
                    user_decision = int(input("Do you want to save your password?\nEnter 1 for Yes and 2 for No: "))
                    
                    #block of code prompts the user to add a label to the password, saves it and append it to the saved_password.txt file
                    if user_decision == 1:
                        password_label = input("What label do you want to give your password? ")
                        to_be_saved = f"\n {password_label}: {password}"
                        print(to_be_saved)
                        print("\nYour new password and label has been saved successfully\n")
                        with open("result/saved_password.txt", "a") as fout: #this opens the file for appending and creates the file if it does not exist
                            fout.write(to_be_saved)
                            fout.close()
                            sys.exit() #to exit the function and end the program
                    
                    #if user decides to not save the password, this code sends the user back to the beginning of the function
                    elif user_decision == 2:
                        break
                        
                    elif user_decision != 1 or 2:
                        print("Invalid choice; You can only pick from 1 or 2")
                        continue
                    
                except ValueError:
                    print("Invalid entry, try again; You can only pick from 1 or 2")
                
                else:
                    break
            
        except ValueError:
            print("Invalid entry, try again; You can only pick from 1 or 2")
    

#random_characters()
#----------------------------------------------------------------------------------------------------

#creating a function that makes a password that comprises of random words
def random_words():

    while True:
        
        #assigning a compilation of words to the words variable
        words = ("Apple", "Banana", "Cherry", "Date", "Eggplant", "Fruit", "Grape", "Honey", "Ice", "Jam", "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Pear", "Quince", "Raspberry", "Strawberry", "Tangerine", "Umbrella", "Vegetable", "Watermelon", "Xylophone", "Yogurt", "Zucchini", "Cucumber", "Lettuce", "Potato", "Pineapple", "Broccoli", "Cauliflower", "Carrot", "Radish", "Spinach", "Cabbage", "Pepper", "Onion", "Tomato", "Celery", "Avocado", "Peach", "Plum", "Blueberry", "Ginger", "Papaya", "Coconut", "Book", "Chair", "Desk", "Lamp", "Computer", "Keyboard", "Mouse", "Monitor", "Printer", "Pen", "Pencil", "Notebook", "Backpack", "Clock", "Couch", "Television", "Remote", "Table", "Plate", "Spoon", "Fork", "Knife", "Cup", "Glass", "Mirror", "Picture", "Painting", "Easel", "Canvas", "Window", "Curtain", "Shoe", "Socks", "Shirt", "Pants", "Hat", "Gloves", "Scarf", "Coat", "Jacket", "Umbrella", "Bag", "Wallet", "Bracelet", "Necklace", "Ring", "Watch", "Sunglasses")
    
        word_password = "" #creating an empty variable that would be used later in the loop for storing the password
        
        try:
            password_range = int(input("How many words do you want to make up your password? "))
            
            if password_range > 0: #making sure the word selected by the user is at least 1
            
                #for loop randomly selects word from the word collection. The number of words selected depends on the user input
                for i in range(password_range):
                    word_password += words[random.randint(0, len(words)-1)]
                    
                print(f"Your new password is: {word_password}")
                
                while True:
                    try:
                        user_decision = int(input("Do you want to save your password?\nEnter 1 for Yes and 2 for No: "))
                        
                        #block of code prompts the user to add a label to the password, saves it and append it to the saved_password.txt file
                        if user_decision == 1:
                            password_label = input("What label do you want to give your password? ")
                            to_be_saved = f"\n {password_label}: {word_password}"
                            print(to_be_saved)
                            print("\nYour new password and label has been saved successfully\n")
                            with open("result/saved_password.txt", "a") as fout:
                                fout.write(to_be_saved)
                                fout.close()
                                sys.exit() #to exit the function and end the program
                        
                        #if user decides to not save the password, this code sends the user back to the beginning of the function
                        elif user_decision == 2:
                            break
                        
                        elif user_decision != 1 or 2:
                            print("Invalid entry; You can only pick from 1 or 2")
                            continue
                            
                    except ValueError:
                        print("Invalid entry, try again; You can only pick from 1 or 2")
                    
                    else:
                        break
                    
            else:
                print("Invalid entry: word selection must be at least 1")
                
        except ValueError:
            print("Invalid choice, try again; entry can only be integers.")



#main function for welcoming user and controlling script execution
def main():
    
    print("\nWelcome User! This script will enable you generate a password\n")
    
    while True:
        try:
            choice = int(input("Do you want to make a new password or review previously saved password?\nEnter 1 to review previously saved password, 2 to make a new password and 3 to exit program: "))
            
            #if statement opens file containing previously saved password
            if choice == 1:
                previous_password = open("result/saved_password.txt")
                for i in previous_password:
                    print(i)
            
            #elif statement prompts user to select from two options and make a password
            elif choice == 2:
                
                while True:
                    try:
                        password_type =  int(input("What type of password would you like?\nEnter 1 for random characters and 2 for random words: "))
                        
                        #this if statement calls the random_characters() function
                        if password_type == 1:
                            random_characters()
                            
                        #this elif statement calls the random_words() function
                        elif password_type == 2:
                            random_words()
                            
                        else:
                            print("Invalid entry, try again; You can only pick from 1 or 2")
                            continue
                            
                    except ValueError:
                        print("Invalid entry, try again; You can only pick from 1 or 2")
                        
                    else:
                        break
            
            #this elif statement ends the program
            elif choice == 3:
                sys.exit()
                
            else:
                print("Invalid entry, try again; You can only pick from 1, 2 or 3")
        
        except ValueError:
            print("Invalid entry, try again; You can only pick from 1, 2 or 3")
            
if __name__ == '__main__':
    main()
    