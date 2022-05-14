from calculator import read_commands_input

if __name__ == '__main__':
    while True:
        print('::::: BASIC CALCULATOR ::::: \n(all inputs must be separated by space || E for Exit program)')
        commands = input(" line of ipunts: ")
        if not commands == 'E':
            print(f"Result: {read_commands_input(commands)} \n\n")
        else:
            exit()