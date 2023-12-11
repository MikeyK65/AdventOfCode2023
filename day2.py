MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

gamesPossible = 0

def extract_numbers_before_colour(array, colour):
    result = 0

    for element in array:
        #print (element)
        if colour == 'blue':
            if 'blue' in element:
                # Split the element and extract the number before "blue"
                parts = element.split('blue')
                #print (parts, len(parts))

                if len(parts) == 2:
                    number_before_colour = parts[0].strip()
                    #print (parts[0], number_before_blue)
                    result += (int(number_before_colour))
        elif colour == 'red':
            if 'red' in element:
                # Split the element and extract the number before "blue"
                parts = element.split('red')
                if len(parts) == 2:
                    number_before_colour = parts[0].strip()
                    result += (int(number_before_colour))
        elif colour == 'green':
            if 'green' in element:
                # Split the element and extract the number before "blue"
                parts = element.split('green')
                if len(parts) == 2:
                    number_before_colour = parts[0].strip()
                    result += (int(number_before_colour))

    return result

def extract_game_numbers(input_string):

    #total_counts = {
    #    'GameNumber': 'Total',
    #    'BlueCount': 0,
    #    'RedCount': 0,
    #    'GreenCount': 0
    #}

    game = input_string.split(':')
    game2 = game[0].split(' ')
    #print (game2[1])

    # Split the input string into games using the delimiter ';'
    games = game[1].split(';')
    #print (games)

    results = []

    for game_str in games:
        # Split each game into components using the delimiter ','
        components = game_str.split(',')
        #print (components)

        # Extract the game number and counts for red, blue, and green
        game_number = int(game2[1])
        blue_count = extract_numbers_before_colour(components, 'blue')
        red_count = extract_numbers_before_colour(components, 'red')
        green_count = extract_numbers_before_colour(components, 'green')

        #print (blue_count, red_count, green_count)

        #total_counts['BlueCount'] += blue_count
        #total_counts['RedCount'] += red_count
        #total_counts['GreenCount'] += green_count

        results.append({
            'GameNumber': game_number,
            'BlueCount': blue_count,
            'RedCount': red_count,
            'GreenCount': green_count
        })

    return results

for line in open("2023 day 2 input.txt", "r"):
    results = extract_game_numbers(line)
    #print (results)
    success = True
    for result in results:
        print (result, "MAX = ", MAX_BLUE, MAX_RED, MAX_GREEN)
        if (result["BlueCount"] > MAX_BLUE) or (result["BlueCount"] < 0) or (result["RedCount"] > MAX_RED) or (result["RedCount"] < 0) or (result["GreenCount"] > MAX_GREEN) or (result["GreenCount"] < 0):
            print (results[0]["GameNumber"], " failed")

            success = False
            break

    if success == True:        
        print (results[0]["GameNumber"])
        gamesPossible += results[0]["GameNumber"]


        

print (gamesPossible)
    #for GameNum, blue, red, green in results[0]:
    #    pass

