def math_operation():
    while True:
        try:
            # Ask the user to choose an operation
            print("Choose an operation (Addition, Subtraction, Multiplication, Division): ")
            operation = input().strip().lower()

            if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
                print("Invalid operation. Please choose one of the four math operations.")
                continue
