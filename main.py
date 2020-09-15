def open_file(file_directory):
    file = open(file_directory, 'r')
    data = []
    for i in file:
        data.append(i)
    return data


def get_character_map():
    character_map = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                     'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                     'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                     'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R',
                     'T', 'Z', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F',
                     'G', 'H', 'J', 'K', 'L', 'Y', 'X', 'C', 'V', 'B',
                     'N', 'M', '/', '(', '!', ')', '?', '_', '-', '‚',
                     ':', 'â', '¬', '.', '+', ',']
    return character_map


def get_randomized_character_map():
    randomized_character_map = ['S', 'L', 'A', '.', 'R', 'm', 'g', 'b', 'V', 'u',
                                '!', 'Z', 'i', '4', 'Y', 'd', ',', '_', '(', '2',
                                'I', 'N', 'q', 'n', 'J', 'o', 'h', 'T', 'a', 'y',
                                '5', 'p', 'F', '6', '8', ',', '-', 'l', '¬', '9',
                                '+', 'H', '1', ':', 't', 'ß', 'z', 'w', 'X', 'r',
                                'O', '?', 'B', 'Q', 'M', 'v', 'P', 'D', 'k', '3',
                                'f', 'C', 'U', 'E', 'c', 'K', ')', '0', '/', 'G',
                                '7', 'x', 's', 'j', 'W', 'e']
    return randomized_character_map


def obfuscate_character(character):
    if character == '\n':
        return '\n'
    elif character == ' ':
        return ' '
    else:
        return get_randomized_character_map()[get_character_map().index(character)]


def obfuscate_data(data):
    result_data = []
    for i in range(0, len(data)):
        obfuscated_word = ''
        for x in data[i]:
            obfuscated_word += obfuscate_character(x)
        result_data.append(obfuscated_word)
    return result_data


def deobfuscate_character(character):
    if character == '\n':
        return '\n'
    elif character == ' ':
        return ' '
    else:
        return get_character_map()[get_randomized_character_map().index(character)]


def deobfuscate_data(data):
    result_data = []
    for i in range(0, len(data)):
        deobfuscated_word = ''
        for x in data[i]:
            deobfuscated_word += deobfuscate_character(x)
        result_data.append(deobfuscated_word)
    return result_data


def print_data(data):
    for i in range(0, len(data)):
        print(data[i])


def main():
    path = input('Enter a file path: ')
    print('1. Obfuscate')
    print('2. Deobfuscate')
    print('3. Quit')
    process = input('Choose a process above: ')

    if process == '1':
        print_data(obfuscate_data(open_file(path)))
        main()
    elif process == '2':
        print_data(deobfuscate_data(open_file(path)))
        main()
    elif process == '3':
        return
    else:
        print('Invalid process')
        return


if __name__ == '__main__':
    main()
