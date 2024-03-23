def create_pyramid(total_words):
    # Calculate the number of levels in the pyramid based on the total number of words
    n = int((-1 + (1 + 8 * total_words) ** 0.5) / 2)

    pyramid = [[None] * i for i in range(1, n + 1)]

    current_number = 1

    # Fill the pyramid structure with numbers
    for i in range(n):
        for j in range(i + 1):
            pyramid[i][j] = current_number
            current_number += 1

    return pyramid


def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    number_word_dict = {}
    
    for line in lines:
        if line:
            number, word = line.split()
            number_word_dict[int(number)] = word
            
    n = len(lines)

    pyramid = create_pyramid(n)



    # Extract the message words based on the pyramid structure
    message_words = [number_word_dict[row[-1]] for row in pyramid]

    # Join the message words to form the decoded message
    decoded_message = ' '.join(message_words)

    return decoded_message


# Example usage:
message_file = 'coding_qual_input.txt'  # Change this to the actual file name
decoded_message = decode(message_file)
print(decoded_message)


