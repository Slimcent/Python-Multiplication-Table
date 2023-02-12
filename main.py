def validate_input(number):
    while True:
        try:
            input_number = int(input(number))
        except ValueError:
            print("number is invalid")
            continue
        else:
            if input_number == 0:
                print("0 is not allowed")
            else:
                return input_number
                break


def multiplication(max_range, multiplication_value):
    for current_range_number in range(1, max_range):
        answer = current_range_number * multiplication_value
        print(str(multiplication_value) + " times " + str(current_range_number) + " = " + str(answer))


multiplicationValue = validate_input("Enter multiplication number")
multiplicationRange = validate_input("Enter multiplication range")

multiplication(multiplicationRange, multiplicationValue)
