# As I'm learning the python i'll make changes each by each 

while True:
    try:
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
            result = num_1 / num_2
            print("Your result is: ", result)
        elif opr == '*':
            result = num_1 * num_2
            print("Your result is: ", result)
        else:
            print("Invalid operator")
            continue
        print("Result:", result)

    except ZeroDivisionError:
        print("Not divisible bye zero")

    except ValueError:
        print("Enter the valid input")

    usr_choice = input("Want to do another calculation: ")

    if usr_choice.lower() != 'y':
        print("Calculator Closed")
        break
