# python3

def read_input():
    inputType = input()

    if "I" in inputType:
        pattern = input()
        text = input()
    # input from a file
    elif "F" in inputType:
        try:
            with open("tests/06") as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
        except FileNotFoundError:
            print("file not found")
            return
    else:
        print("Invalid input source")
        return

    return (pattern, text)


B = 13
Q = 256


def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    global B, Q
    pattern_length = len(pattern)
    text_length = len(text)

    hash_patt = get_hash(pattern)
    hash_text = get_hash(text[0:pattern_length])

    b_power = pow(B, pattern_length - 1, Q)

    occurrences = []

    for i in range(text_length - pattern_length + 1):
        if hash_patt == hash_text and text[i:i + pattern_length] == pattern:
            occurrences.append(i)

        if i < text_length - pattern_length:
            hash_text = (hash_text - ord(text[i]) * b_power) % Q
            hash_text = (hash_text * B + ord(text[i + pattern_length])) % Q

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
