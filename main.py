# This is a program that runs DFA on an input string
# Created by Wilber Rosales and Anya Hossaini

# Open and read DFA file
# File simDFA = {w | w contains sets of all string that start with '0'} with the alphabet Î£ = { 0, 1 }

alphabet = []
initial_state = []
number = []
next_state = []

def valid_input(input_str, alphabet):
    for i in input_str:
        if i not in alphabet:
            return False

    return True


with open("simDFA.txt", "r") as file:
    print('File read successfully.')
    alphabet = file.readline()
    lines = file.readlines()
    desired_lines = lines[3:9]

    for i in desired_lines:
        as_list = i.split(" ")
        initial_state.append(as_list[0])
        number.append(as_list[1])
        next_state.append(as_list[2].replace("\n", ""))

while True:
    # User inputs string
    print('Please enter an input string:')
    input_string = input()
    bad_input = True

    while bad_input:
        if not valid_input(input_string, alphabet):
            print("please enter a valid string")
            input_string = input()
            continue
        bad_input = False

    # if string is empty, should be rejected
    if len(input_string) == 0:
        print('Input is rejected.')
        print(initial_state[0])
    # if the first char in input is equal to the first rule from file, should be accepted
    elif input_string[0] == number[0]:
        accepted_path = []
        print('Input is accepted. Path:')
        accepted_path.append(initial_state[0])
        accepted_path.append(next_state[0])
        for i in range(1, len(input_string)):
            if input_string[i] == number[4]:
                accepted_path.append(next_state[4])
            elif input_string[i] == number[5]:
                accepted_path.append(next_state[5])
        print(' '.join(accepted_path))
    # if the first char in input is equal to the second rule from file, should be rejected
    elif input_string[0] == number[1]:
        rejected_path = []
        print('Input is rejected. Path:')
        rejected_path.append(initial_state[1])
        rejected_path.append(next_state[1])

        for i in range(1, len(input_string)):
            if input_string[i] == number[2]:
                rejected_path.append(next_state[2])
            elif input_string[i] == number[3]:
                rejected_path.append(next_state[3])
        print(' '.join(rejected_path))

file.close()