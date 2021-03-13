# text to be entered by user
text = input('Enter text:')


def backward(string):
    """
    This function backwards words longer
    than 3 signs in a string
    :param string: string entered by user
    :return: string with reversed words unless
    shorter then 3 signs
    """
    string = string.split()
    words = []
    for word in string:
        if len(word) > 3:
            words.append(word[::-1])
        else:
            words.append(word)

    words = ' '.join(words)
    return words


if __name__ == '__main__':
    result = backward(text)
    print(result)
