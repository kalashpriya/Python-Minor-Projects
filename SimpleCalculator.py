#Simple calculator
import numpy as np
#Initializing a random variable to enter the loop to allow repeated operations.
rep=1 
while(rep==1):
    #Accepting operation input from user
    operation = input("Enter operation (+, -, *, /, %, **): ") 
    #Exponentiation operation
    if operation == '**': 
        b= int(input("Enter base value: ")) 
        e= int(input("Enter exponent value: ")) #Power value input
        print(f"Result: {b**e}")
    #Addition operation
    elif operation== '+': 
        #Number of values input if the user might want to add multiple numbers
        num= int(input("How many numbers do you want to add?: ")) 
        val=[]
        for i in range(num):
            n=float(input(f"Enter value {i+1}: "))
            val.append(n) #Storing values to a list
        print("Result: ", np.sum(val)) #Using numpy sum function to calculate sum
    #Subtraction operation
    #We are assuming here that subtraction is only between two numbers for simplicity
    elif operation== '-': 
        a= float(input("Enter A: "))
        b= float(input("Enter B: "))
        print("Result (A-B): ",a-b) #Calculating difference
    elif operation== '*':
        #Number of values input if the user might want to multiply multiple numbers
        num= int(input("How many numbers do you want to multiply?: ")) 
        val=[] #List to store input values
        for i in range(num):
            n=float(input(f"Enter value {i+1}: "))
            val.append(n)
        print("Result: ", np.prod(val)) #Using numpy product function
    #Division operation
    elif operation== '/': 
        a= float(input("Enter A: "))
        b= float(input("Enter B: "))
        if b==0: #Error handling for division by zero
            print("Error: Division by zero is not possible.")
        else:
            print("Result (A/B): ",a/b)
    #Modulus operation
    elif operation== '%': 
        a= float(input("Enter A: "))
        b= float(input("Enter B: "))
        if b==0: #Error handling for modulus by zero
            print("Error: Division by zero is not possible.")
        else:
            print("Result (A%B): ",a%b)
    #Invalid operation handling
    else: 
        print("Invalid input")
    #Taking input to continue or exit
    print("To perform another operation press 1 or press 0 to exit.")
    rep=int(input()) 
    if rep==0:
        print("Exiting the calculator. Thank you!")
        #If user inputs 0, the loop ends and program exits
        #If user inputs 1, the loop continues for another operation