morse_dict = {
    'A': ' .- ', 'B': ' -... ', 'C': ' -.-. ',
    'D': ' -.. ', 'E': ' . ', 'F': ' ..-. ',
    'G': ' --. ', 'H': ' .... ', 'I': ' .. ',
    'J': ' .--- ', 'K': ' -.- ', 'L': ' .-.. ',
    'M': ' -- ', 'N': ' -. ', 'O': ' --- ',
    'P': ' .--. ', 'Q': ' --.- ', 'R': ' .-. ',
    'S': ' ... ', 'T': ' - ', 'U': ' ..- ',
    'V': ' ...- ', 'W': ' .-- ', 'X': ' -..- ',
    'Y': ' -.-- ', 'Z': ' --.. '
}

# text to be entered by user
text_to_decode = input('Enter Morse code to be decoded:')


def morsecheck(morse):
    """
    This function checks if in a morse code
    there are any alphanumeric values
    :param morse: Morse code provided by user
    :return: if Morse code is invalid returns
    a string with information, if it's valid return
    encryption function
    """
    if not any(substr.isalnum() for substr in morse):
        return decoder(morse)
    else:
        raise ValueError('This is an invalid Morse Code')


def decoder(morse):
    """
    This function encodes a Morse code string into
    latin alphabet text
    :param morse: Morse code string entered by user
    :return: encoded alphabetic text
    """
    morse = morse.replace('   ', ' space ')
    wordlist = morse.split()
    wordlist = [x.center(len(x) + 2) for x in wordlist]

    for letter, sign in morse_dict.items():
        wordlist = [x.replace(sign, letter) for x in wordlist]

    wordlist = [x.replace(' space ', ' ') for x in wordlist]
    encoded = ''.join(wordlist)
    return encoded


if __name__ == '__main__':
    result = morsecheck(text_to_decode)
    print(result)
