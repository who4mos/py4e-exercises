def count(string, letter):
    occurr = 0

    for char in string:
        if char == letter:
            occurr += 1

    return occurr
