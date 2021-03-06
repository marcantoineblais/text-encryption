
DEFAULT = "This is an encryption key"
previous_input = []


def characters_list_generator():
    characters = [chr(i) for i in range(32, 127)]
    for i in range(192, 382):
        characters.append(chr(i))
    characters.append("’")
    return characters


def show_help(cmd):
    if cmd == "-help":
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
    return


def check_if_command_in_user_input(initial_text, i=0):
    cmd_list = ("-code", "-decode", "-exit", "-reset", "-keyword", "-init", "-noinit", "-help", "-status")

    if len(initial_text) == 0:
        print("Please write at least one character.")
        return ValueError

    user_cmd = []
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
                    if any([command in possible_command_str for command in cmd_list]):
                        for command in cmd_list:
                            if possible_command_str == command:
                                user_cmd.append(command)
                                return user_cmd
                    else:
                        print('Invalid command. Please write "-help" to see valid user commands.')
                        return []
            possible_command_str = "".join(possible_command_list)
            if any([command in possible_command_str for command in cmd_list]):
                for command in cmd_list:
                    if possible_command_str == command:
                        user_cmd.append(command)
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


def show_status(cmd, keyword, show_initial_text, is_encryption):
    if cmd == "-status":
        print(f"The current keyword is : '{keyword}'")
        if show_initial_text:
            print("Initial text will be shown.")
        else:
            print("Initial text will not be shown.")
        if is_encryption:
            print("Text will be encrypted.")
        else:
            print("Text will be decrypted.")
        print()
    return


def program_end(cmd):
    if cmd == "-exit":
        print("Exiting program.")
        print()
        return True
    return False


def program_reset(cmd):
    if cmd == "-reset":
        print("Initial parameters restored.")
        print()
        return True
    return False


def replace_keyword(cmd, keyword):
    if cmd == "-keyword":
        print(f"The current keyword is : '{keyword}'")
        new_keyword = input("Please write your new keyword : ")
        print()
        if new_keyword == "":
            return keyword
        return new_keyword
    return keyword


def show_initial_text_toggle(cmd, show_initial_text):
    if cmd == "-init":
        print("Initial text will be shown.")
        print()
        return True
    if cmd == "-noinit":
        print("Initial text will not be shown.")
        print()
        return False
    return show_initial_text


def encryption_toggle(cmd, is_encryption):
    if cmd == "-code":
        print("Text will be encrypted.")
        print()
        return True
    if cmd == "-decode":
        print("Text will be decrypted.")
        print()
        return False
    return is_encryption


def value_calc(text):
    value_list = []
    for value in text:
        i = 0
        while i in range(len(characters_list)):
            if value == characters_list[i]:
                value_list.append(i)
                break
            i += 1
    return value_list


def reverse_value_calc(text):
    value_list = []
    for value in text:
        i = 0
        while i in range(len(characters_list)):
            if value == characters_list[i]:
                value_list.append(len(characters_list) - i)
                break
            i += 1
    return value_list


def text_value_gen(keyword_value_list, initial_text_value_list, first_value):
    text_value_list = []
    i = 0
    last_value = first_value
    for value in initial_text_value_list:
        text_character_value = (value + (keyword_value_list[i] + last_value)) % len(characters_list)
        text_value_list.append(text_character_value)
        last_value = (keyword_value_list[i] + last_value) % len(characters_list)
        i += 1
        if i == len(keyword_value_list):
            i = 0
    return text_value_list


def text_gen(value_list):
    character_list = []
    for value in value_list:
        for i in range(len(characters_list)):
            if i == value:
                character_list.append(characters_list[i])
                break
    encrypted_text = "".join(character_list)
    return encrypted_text


def text_encryption(initial_text, keyword):
    keyword_value_list = value_calc(keyword)
    initial_text_value_list = value_calc(initial_text)
    calc_value = sum(keyword_value_list) % len(characters_list)
    encrypted_text_value_list = text_value_gen(keyword_value_list, initial_text_value_list, calc_value)
    encrypted_text = text_gen(encrypted_text_value_list)
    return encrypted_text


def text_decryption(initial_text, keyword):
    keyword_value_list = reverse_value_calc(keyword)
    initial_text_value_list = value_calc(initial_text)
    calc_value = len(characters_list) - (sum([len(characters_list) - value for value in keyword_value_list]))
    decrypted_text_value_list = text_value_gen(keyword_value_list, initial_text_value_list, calc_value)
    decrypted_text = text_gen(decrypted_text_value_list)
    return decrypted_text


def run_text_encryption(is_encryption, initial_text, keyword, show_initial_text):
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
    return


def program_run(keyword=DEFAULT, show_initial_text=False, is_encryption=True):
    initial_text = input("Please write or copy your text here : ")

    # Check for user command in text.
    user_cmd = check_if_command_in_user_input(initial_text)
    if user_cmd == ValueError:
        print()
        return program_run(keyword, show_initial_text, is_encryption)

    # execute user cmd in order of apparition
    if len(user_cmd) > 0:
        for cmd in user_cmd:
            if program_end(cmd):
                return
            if program_reset(cmd):
                return program_run()
            show_help(cmd)
            show_status(cmd, keyword, show_initial_text, is_encryption)
            is_encryption = encryption_toggle(cmd, is_encryption)
            show_initial_text = show_initial_text_toggle(cmd, show_initial_text)
            keyword = replace_keyword(cmd, keyword)
        return program_run(keyword, show_initial_text, is_encryption)

    # Program execution when text is detected.
    run_text_encryption(is_encryption, initial_text, keyword, show_initial_text)
    return program_run(keyword, show_initial_text, is_encryption)


# Comment next line to not show commands at program start.
show_help("-help")

# Generate characters' list
characters_list = characters_list_generator()

# Change "DEFAULT" value on line 3 to replace default keyword.
program_run()
