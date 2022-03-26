
DEFAULT = "Ta mère en short"


def characters_list_generator():
    characters_list = [chr(i) for i in range(32, 127)]
    for i in range(192, 382):
        characters_list.append(chr(i))
    characters_list.append("’")
    return characters_list


def show_user_commands(initial_text):
    if "-help" in initial_text.lower():
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
        print()
        return True
    return False


def check_if_command_in_user_input(initial_text, this_is_a_user_command=False, i=0):
    command_list = ["-code", "-decode", "-exit", "-reset", "-keyword", "-init", "noinit", "-help", "-status"]

    if len(initial_text) == 0:
        print("Please write at least one character.")
        return ValueError

    while i in range(len(initial_text)):
        possible_command_list = []
        command_list_order_of_execution = []
        if initial_text[i] == " ":
            i += 1
        elif initial_text[i] == "-":
            while initial_text[i] != " ":
                possible_command_list.append(initial_text[i])
                i += 1
                if i == len(initial_text):
                    possible_command_str = "".join(possible_command_list)
                    if any([command in possible_command_str for command in command_list]):
                        this_is_a_user_command = True
                        return this_is_a_user_command
                    else:
                        this_is_a_user_command = False
                        print('Invalid command. Please write "-help" to see valid user commands.')
                        return this_is_a_user_command
            possible_command_str = "".join(possible_command_list)
            if any([command in possible_command_str for command in command_list]):
                this_is_a_user_command = True
                i += 1
            else:
                this_is_a_user_command = False
                print('Invalid command. Please write "-help" to see the user commands.')
                return this_is_a_user_command
        else:
            this_is_a_user_command = False
            if len(possible_command_list) > 0:
                print('Invalid command. Please write "-help" to see valid user commands.')
            return this_is_a_user_command
    return this_is_a_user_command


def show_status(initial_text, keyword, show_initial_text, is_encryption):
    if "-status" in initial_text.lower():
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


def program_end(initial_text):
    if "-exit" in initial_text.lower():
        print("Exiting program.")
        return True
    return False


def program_reset(initial_text):
    if "-reset" in initial_text.lower():
        print("Initial parameters restored.")
        return True
    return False


def replace_keyword(initial_text, keyword):
    if "-keyword" in initial_text.lower():
        print(f"The current keyword is : '{keyword}'")
        new_keyword = input("Please write your new keyword : ")
        if new_keyword == "":
            return keyword
        return new_keyword
    return keyword


def show_initial_text_toggle(initial_text, show_initial_text):
    if "-noinit" in initial_text.lower():
        show_initial_text = False
        print("Initial text will not be shown.")
        return show_initial_text
    if "-init" in initial_text.lower():
        show_initial_text = True
        print("Initial text will be shown.")
        return show_initial_text
    return show_initial_text


def encryption_toggle(initial_text, is_encryption):
    if "-code" in initial_text.lower():
        is_encryption = True
        print("Text will be encrypted.")
        return is_encryption
    if "-decode" in initial_text.lower():
        is_encryption = False
        print("Text will be decrypted.")
        return is_encryption
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


def program_run(keyword=DEFAULT, show_initial_text=False, is_encryption=True,):
    initial_text = input("Please write or copy your text here : ")

    # Check for user command in text.
    is_user_command = check_if_command_in_user_input(initial_text)
    if is_user_command == ValueError:
        print()
        return program_run(keyword, show_initial_text, is_encryption)
    elif is_user_command:
        show_user_commands(initial_text)
        show_status(initial_text, keyword, show_initial_text, is_encryption)
        if program_end(initial_text):
            return
        if program_reset(initial_text):
            print()
            return program_run()
        keyword = replace_keyword(initial_text, keyword)
        show_initial_text = show_initial_text_toggle(initial_text, show_initial_text)
        is_encryption = encryption_toggle(initial_text, is_encryption)
        print()
        return program_run(keyword, show_initial_text, is_encryption)

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
    return program_run(keyword, show_initial_text, is_encryption)


# Comment next line to not show commands at program start.
show_user_commands("-help")

# Change "DEFAULT" value on line 3 to replace default keyword.
program_run()
