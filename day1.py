calibrationValue = 0
totalCalibrationValue = 0
a = -1
b = -1

stage = 2

letters = ["one", "two","three","four","five","six","seven","eight","nine"]
numbers = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

def extract_word_representations(input_string):
    current_word = ''
    words = []

    for char in input_string:
        if char.isalpha():
            current_word += char
        else:
            if current_word and current_word.isdigit():
                words.append(current_word)
                current_word = ''
                
    if current_word and current_word.isdigit():
        words.append(current_word)

    word_representations = [word for word in words if word.isdigit() and 0 <= int(word) <= 9]
    print (input_string, word_representations)
    return word_representations

def find_word_representations(input_string):
    words = [word for word in input_string.split() if word.isalpha() and word.isdigit()]
    print (input_string, words)
    return words

def find_substring_index(main_string, substring):
    index = main_string.find(substring)
    return index

for line in open("2023 day 1 input.txt", "r"):
    if stage == 1:
        numbers = [char for char in line if char.isdigit()]

        if numbers:
            a = int(numbers[0])
            b = int(numbers[-1])
            s = str(a) + str(b)
            calibrationValue = int(s)
            #print (line, a,b, s, calibrationValue)

    elif stage == 2:
        numbers = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        digitNumbers = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

        digitNumbers = [index for index, char in enumerate(line) if char.isdigit()]
        digitActualNumber = [line[index] for index in digitNumbers]

        for i in range(len(letters)):
            numbers[i] = find_substring_index(line, letters[i])

        # Get index
        non_negative_numbers = [num for num in numbers if num >= 0]

        if non_negative_numbers:
            #lowest = min(non_negative_numbers)
            #highest = max(non_negative_numbers)

            a = min(numbers.index(min(filter(lambda x: x >= 0, non_negative_numbers))), *digitNumbers)
            b = max(numbers.index(max(filter(lambda x: x >= 0, non_negative_numbers))), *digitNumbers)

            s = str(line[a]) + str(line[b])
            calibrationValue = int(s)
            print (line, numbers, digitNumbers, digitActualNumber, a, b, s)
        

        
    totalCalibrationValue += calibrationValue

print (totalCalibrationValue)

    


