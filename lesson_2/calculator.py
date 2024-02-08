import json

# en / es / fr
LANGUAGE = 'en'

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(key):
    message = messages(key)
    print(f"=> {message}")

def messages(message):
    return MESSAGES[LANGUAGE][message]

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    except TypeError:
        return True

    return False

def get_value(key):
    value_str = None

    if key == 'operation':
        while value_str not in ["1", "2", "3", "4"]:
            if value_str:
                prompt("wrong_choice")
            prompt(key)
            value_str = input()
    else:
        while invalid_number(value_str):
            if value_str:
                prompt("invalid_number")
            prompt(key)
            value_str = input()

    return value_str

prompt("welcome")

while True:

    number1 = get_value("first_number")
    number2 = get_value("second_number")
    operation = get_value("operation")

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)

    print("=> " + messages("result").format(output=output))

    prompt("go_again")
    answer = input()
    if answer and answer[0].lower() != 'y':
        break
