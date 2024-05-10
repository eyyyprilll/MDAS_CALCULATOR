def math_operation():
    while True:
        try:
            # Ask the user to choose an operation
            print("Choose an operation (Addition, Subtraction, Multiplication, Division): ")
            operation = input().strip().lower()

            if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
                print("Invalid operation. Please choose one of the four math operations.")
                continue

            # Ask the user for two numbers
            print("Enter the first number: ")
            num1 = float(input())
            print("Enter the second number: ")
            num2 = float(input())

            # Perform the chosen operation
            if operation == 'addition':
                result = num1 + num2
            elif operation == 'subtraction':
                result = num1 - num2
            elif operation == 'multiplication':
                result = num1 * num2
            elif operation == 'division':
                if num2 == 0:
                    print("Cannot divide by zero. Please try again.")
                    continue
                result = num1 / num2

            # Display the result
            print("The result is: ", result)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Ask if the user wants to try again
        while True:
            print("Do you want to try again? (yes/no): ")
            try_again = input().strip().lower()
            if try_again == "yes":
                break
            elif try_again == "no":
                print("Exiting the calculator.")
                return
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

   # Call the function to start the program
math_operation()