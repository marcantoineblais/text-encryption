
DEFAULT = "Ta mère en short"


def characters_list_generator():
    characters_list = [chr(i) for i in range(32, 127)]
    for i in range(192, 382):
        characters_list.append(chr(i))
    characters_list.append("’")
    return characters_list


def show_user_commands():
    print('Write "-code" to encrypt your text.')
    print('Write "-decode" to decrypt your text.')
    print('Write "-exit" to end the program.')
    print('Write "-help" to view these commands again.')
    print('Write "-init" to show initial text.')
    print('Write "-keyword" to change the keyword.')
    print('Write "-noinit" to hide initial text.')
    print('Write "-reset" to restore the default parameters.')
    print('Write "-status" to view active parameters.')
    print("----------------------------------------------")
    return


def check_if_command_in_user_input(initial_text, command_list, i=0):
    if len(initial_text) == 0:
        print("Please write at least one character.")
        return ValueError

    command_list_order_of_execution = []
    while i in range(len(initial_text)):
        possible_command_list = []
        if initial_text[i] == " ":
            i += 1
        elif initial_text[i] == "-":
            while initial_text[i] != " ":
                possible_command_list.append(initial_text[i])
                i += 1
                if i == len(initial_text):
                    possible_command_str = "".join(possible_command_list)
                    if any([command in possible_command_str for command in command_list]):
                        for command in command_list:
                            if possible_command_str == command:
                                command_list_order_of_execution.append(command)
                                return command_list_order_of_execution
                    else:
                        print('Invalid command. Please write "-help" to see valid user commands.')
                        return []
            possible_command_str = "".join(possible_command_list)
            if any([command in possible_command_str for command in command_list]):
                for command in command_list:
                    if possible_command_str == command:
                        command_list_order_of_execution.append(command)
                        i += 1
                        break
            else:
                print('Invalid command. Please write "-help" to see the user commands.')
                return []
        else:
            if len(possible_command_list) > 0:
                print('Invalid command. Please write "-help" to see valid user commands.')
            return []
    return []


def show_status(keyword, show_initial_text, is_encryption):
    print(f"The current keyword is : '{keyword}'")
    if show_initial_text:
        print("Initial text will be shown.")
    else:
        print("Initial text will not be shown.")
    if is_encryption:
        print("Text will be encrypted.")
    else:
        print("Text will be decrypted.")
    return


def program_end(is_end):
    print("Exiting program.")
    return is_end


def program_reset(is_reset):
    print("Initial parameters restored.")
    return is_reset


def replace_keyword(keyword):
    print(f"The current keyword is : '{keyword}'")
    new_keyword = input("Please write your new keyword : ")
    if new_keyword == "":
        return keyword
    return new_keyword


def show_initial_text_toggle(show_initial_text):
    if show_initial_text:
        print("Initial text will be shown.")
        return
    print("Initial text will not be shown.")
    return


def encryption_toggle(is_encryption):
    if is_encryption:
        print("Text will be encrypted.")
        return is_encryption
    print("Text will be decrypted.")
    return is_encryption


def text_encryption(initial_text, keyword):
    characters_list = characters_list_generator()

    keyword_value_list = []
    for value in keyword:
        i = 0
        while i in range(len(characters_list)):
            if value == characters_list[i]:
                keyword_value_list.append(i)
            i += 1

    initial_text_value_list = []
    for value in initial_text:
        i = 0
        while i in range(len(characters_list)):
            if value == characters_list[i]:
                initial_text_value_list.append(i)
            i += 1

    encrypted_text_value_list = []
    i = 0
    last_value = 0
    for value in initial_text_value_list:
        encrypted_text_character_value = value + (keyword_value_list[i] + last_value)
        while encrypted_text_character_value >= len(characters_list):
            encrypted_text_character_value -= len(characters_list)
        encrypted_text_value_list.append(encrypted_text_character_value)
        last_value = keyword_value_list[i] + last_value
        while last_value >= len(characters_list):
            last_value -= len(characters_list)
        i += 1
        if i == len(keyword_value_list):
            i = 0

    encrypted_text_character_list = []
    for value in encrypted_text_value_list:
        for i in range(len(characters_list)):
            if i == value:
                encrypted_text_character_list.append(characters_list[i])
                break
    encrypted_text = "".join(encrypted_text_character_list)
    return encrypted_text


def text_decryption(initial_text, keyword):
    characters_list = characters_list_generator()

    keyword_value_list = []
    for character in keyword:
        i = 0
        while i in range(len(characters_list)):
            if character == characters_list[i]:
                keyword_value_list.append(len(characters_list) - i)
            i += 1

    initial_text_value_list = []
    for character in initial_text:
        i = 0
        while i in range(len(characters_list)):
            if character == characters_list[i]:
                initial_text_value_list.append(i)
            i += 1

    encrypted_text_value_list = []
    i = 0
    last_value = 0
    for value in initial_text_value_list:
        encrypted_text_character_value = value + (keyword_value_list[i] + last_value)
        while encrypted_text_character_value >= len(characters_list):
            encrypted_text_character_value -= len(characters_list)
        encrypted_text_value_list.append(encrypted_text_character_value)
        last_value = keyword_value_list[i] + last_value
        while last_value >= len(characters_list):
            last_value -= len(characters_list)
        i += 1
        if i == len(keyword_value_list):
            i = 0

    encrypted_text_character_list = []
    for value in encrypted_text_value_list:
        for i in range(len(characters_list)):
            if i == value:
                encrypted_text_character_list.append(characters_list[i])
                break
    encrypted_text = "".join(encrypted_text_character_list)
    return encrypted_text


def program_run(keyword=DEFAULT, show_initial_text=False, is_encryption=True, is_reset=False, is_end=False):
    initial_text = input("Please write or copy your text here : ")

    # Check for user command in text.
    cmd_list = {
        "-code": [is_encryption, encryption_toggle, [True]],
        "-decode": [is_encryption, encryption_toggle, [False]],
        "-exit": [is_end, program_end, [True]],
        "-reset": [is_reset, program_reset, [True]],
        "-keyword": [keyword, replace_keyword, [keyword]],
        "-init": [show_initial_text, show_initial_text_toggle, [True]],
        "-noinit": [show_initial_text, show_initial_text_toggle, [False]],
        "-help": [show_user_commands, []],
        "-status": [show_status, (keyword, show_initial_text, is_encryption)],
    }

    command_list_order_of_execution = check_if_command_in_user_input(initial_text, cmd_list)
    if command_list_order_of_execution == ValueError:
        print()
        return program_run(keyword, show_initial_text, is_encryption)
    if len(command_list_order_of_execution) > 0:
        for user_command in command_list_order_of_execution:
            if len(cmd_list[user_command]) < 3:
                cmd_list[user_command][0](*cmd_list[user_command][1])
            else:
                cmd_list[user_command][0] = cmd_list[user_command][1](*cmd_list[user_command][2])
            # if cmd_list["-exit"]:
            #     return
            # if cmd_list["-reset"]:
            #     return program_run()
        print()
        return program_run(
            keyword=cmd_list["-keyword"][0],
            show_initial_text=cmd_list["-init"][0],
            is_encryption=cmd_list["-code"][0]
        )

    # Program execution when text is detected.
    if is_encryption:
        computed_text = text_encryption(initial_text, keyword)
    else:
        computed_text = text_decryption(initial_text, keyword)
    print()
    print("MODIFIED TEXT : ")
    print(computed_text)
    if show_initial_text:
        print("----------------------------------------------")
        print("ORIGINAL TEXT : ")
        print(initial_text)
    print()
    return program_run(
            keyword=cmd_list["-keyword"][0],
            show_initial_text=cmd_list["-init"][0],
            is_encryption=cmd_list["-code"][0]
        )


# Comment next line to not show commands at program start.
show_user_commands()
print()

# Change "DEFAULT" value on line 3 to replace default keyword.
program_run()
