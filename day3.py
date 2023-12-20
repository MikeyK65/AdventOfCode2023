import re

def extract_whole_numbers(input_string):
    pattern = r'\b\d+\b'
    whole_numbers = [int(match) for match in re.findall(pattern, input_string)]
    return whole_numbers

schematicArray = []

for line in open("2023 day 3 input.txt", "r"):
    schematicArray.append (line)

i = 0
index = 0
partsSum = 0
while index < len(schematicArray):
    # Get all numbers out
    wholeNumbers = extract_whole_numbers(schematicArray[index])
    startIndex = endIndex = 0

    # For each number check to see if there is an adjacent symbol
    # Need to get index of each number and length
    # Then check on current line startIndex - 1, endIndex + 1
    # Check previous line same indexes as the number
    # Check following line as above
    for num in wholeNumbers:
        startIndex = schematicArray[index].find(str(num))
        endIndex = startIndex + len(str(num))
        #print (wholeNumbers, startIndex, endIndex)

    index += 1
