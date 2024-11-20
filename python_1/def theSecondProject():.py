def theSecondProject():
    print("Heyyyy you guys")
    print("Manvi")
    print("Manvi") 

# Call the function
theSecondProject()
theSecondProject()

# Function to display the menu
def displayMenu():
    print("Welcome to my calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Function to add two numbers
def addNumbers(firstNumber, secondNumber):
    sum = firstNumber + secondNumber
    print(f"The sum of {firstNumber} and {secondNumber} is {sum}")
            
# Function to subtract two numbers
def subtractNumbers(firstNumber, secondNumber):
    difference = firstNumber - secondNumber
    print(f"The difference of {firstNumber} and {secondNumber} is {difference}")

# Function to multiply two numbers
def multiplyNumbers(firstNumber, secondNumber):
    product = firstNumber * secondNumber
    print(f"The product of {firstNumber} and {secondNumber} is {product}")

# Function to divide two numbers
def divideNumbers(firstNumber, secondNumber):
    if secondNumber != 0:
        quotient = firstNumber / secondNumber
        print(f"The quotient of {firstNumber} and {secondNumber} is {quotient}")
    else:
        print("Error: Cannot divide by zero.")

# Main function
def main():
    # Display the menu
    displayMenu()
    def main(): This is the main program
    allFeatures = ["Adding", "Subtratction", "Division", "Multiplication", "Module"]
    
   #Start loop 
   for currentFeature in allFeatures:
      print(currentFeature)
   #Advanced loop
   
    # Get user input for the operation
    userOption = int(input("Please select an option: "))
    
    # Get user input for numbers
    userFirstNumber = float(input("Enter the first number: "))
    userSecondNumber = float(input("Enter the second number: "))
    
    # Execute based on user option
    if userOption == 1:
        addNumbers(userFirstNumber, userSecondNumber)
    elif userOption == 2:
        subtractNumbers(userFirstNumber, userSecondNumber)
    elif userOption == 3:
        multiplyNumbers(userFirstNumber, userSecondNumber)
    elif userOption == 4:
        divideNumbers(userFirstNumber, userSecondNumber)
    else:
        print("Invalid option selected.")

# Call the main function to start the program
main()
