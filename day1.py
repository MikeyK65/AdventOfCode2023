calibrationValue = 0
totalCalibrationValue = 0
a = -1
b = -1


letters = ["1","2","3","4","5","6","7","8","9","one", "two","three","four","five","six","seven","eight","nine"]
numbers = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
wordRepresentations = ["one", "two","three","four","five","six","seven","eight","nine"]


def find_indices_of_strings(text, strings_to_find):
    indices = []
    
    for word in strings_to_find:
        start_index = 0
        while True:
            index = text.find(word, start_index)
            if index == -1:
                break
            indices.append((word, index))
            start_index = index + 1
    
    return indices


for line in open("2023 day 1 input.txt", "r"):
    
    #numbers = [char for char in line if char.isdigit()]
    #print (numbers)
    #if numbers:
    #    a = int(numbers[0])
    #    b = int(numbers[-1])
    #    s = str(a) + str(b)
    #    calibrationValue = int(s)
    #    #print (line, a,b, s, calibrationValue)

    indices = find_indices_of_strings(line, letters)

    #print(f"Indices of occurrences: {indices}")     

    # Find the tuple with the lowest second element
    min_tuple = min(indices, key=lambda x: x[1])

    # Find the tuple with the highest second element
    max_tuple = max(indices, key=lambda x: x[1])   

    #print (min_tuple[0], max_tuple[0], type(min_tuple[0]), type(min_tuple[1]))
    if (min_tuple[0].isdigit()):
        a = int(min_tuple[0])
    else:
        a = wordRepresentations.index(min_tuple[0]) + 1

    if (max_tuple[0].isdigit()):
        b = int(max_tuple[0])
    else:
        b = wordRepresentations.index(max_tuple[0]) + 1

    #a = int(numbers[0])
    #b = int(numbers[-1])
    s = str(a) + str(b)
    calibrationValue = int(s)
    print (line, a,b, s)

        
    totalCalibrationValue += calibrationValue

print (totalCalibrationValue)

    


