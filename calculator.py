while True:
    num_1 = int(input("Enter the first num: "))
    num_2 = int(input("Enter the second num: "))
    opr = input("Enter the operation: ")

    if opr == '+':
        result = num_1 + num_2
        print("Your result is: ", result)
    elif opr == '-':
        result = num_1 - num_2
        print("Your result is: ", result)
    elif opr == '/':
        if num_2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            result = num_1 / num_2
            print("Your result is: ", result)
    elif opr == '*':
        result = num_1 * num_2
        print("Your result is: ", result)
    else:
        print("Invalid operator")

    usr_choice = input("Want to do another calculation: ")

    if usr_choice != 'y':
        print("Calculator Closed")
    break

