def print_message(message):
    print(f"=> {message}")


def get_value(prompt, _type, _min=None, _max=None):
    while True:
        user_input = input("=> " + prompt)
        if _type is not None:
            try:
                user_input = _type(user_input)
            except ValueError:
                print_message(f"Please enter number of type {_type.__name__}")
                continue
        if _min is not None and user_input < _min:
            print_message(f"Please enter a value greater than {_min}")
        elif _max is not None and user_input > _max:
            print_message(f"Please enter a value less than {_max}")
        else:
            return user_input


while True:
    loan_amount = get_value("Please enter the loan amount: ", float, 1)
    monlthy_apr = (
        get_value("Please enter the APR in % (2.5 for 2.5%): ", float, 0) / 100 / 12
    )

    while True:
        loan_duration_years = get_value(
            "Please enter the duration of the loan in years: ", int, 0
        )
        loan_duration_months = get_value(
            "Please enter the duration of the loan in months: ", int, 0
        )
        loan_duration = (loan_duration_years * 12) + loan_duration_months
        if loan_duration:
            break
        print_message("Loan duration must be greater than 0.")

    if monlthy_apr > 0:
        montly_payment = loan_amount * (
            monlthy_apr / (1 - (1 + monlthy_apr) ** (-loan_duration))
        )
    else:
        montly_payment = loan_amount / loan_duration

    print_message(f"Your monthly payment is: {montly_payment:.2f}")

    while True:
        exit_calc = get_value("Would you like to exit? (y/n): ", str)
        if exit_calc != "y" and exit_calc != "n":
            print_message("Please enter 'y' or 'n'")
        else:
            break

    if exit_calc[0] == "y":
        break
