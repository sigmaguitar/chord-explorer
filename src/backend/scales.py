while True:
    import json
    with open('data/scales.json', 'r') as file:
        data = json.load(file)

    w = input("Choose the KEY you want to further explore ! - Type [quit] to Exit ")
    w = w.strip().lower()
    print()

    #print(data['major'])

    def pentatonic(w):
        if w in data['maj']:
            print(f" [{w.title()}] Major Pentatonic Scale // 1 - 2 - 3 - 5 - 6 ")
            result_1 = data['maj'][w][0][0:3]+data['maj'][w][0][4:6]
            print(result_1)
            print()
            return result_1

        elif w in data['min']:
            print(f" [{w.title()}] Minor Pentatonic // 1 - b3 - 4 - 5 - b7 ")
            result_1 = data['min'][w][0][:1]+data['min'][w][0][2:5]+data['min'][w][0][-1:]
            print(result_1)
            print()
            return result_1


    def major_minor_scale(w):
        if w in data['maj']:
            print(f" [{w.title()}] Major Scale // 1 - 2 - 3 - 4 - 5 - 6- 7 ")
            result = data['maj'][w][0]
            print(result)
            return result

        elif w in data['min']:
            print(f" [{w.title()}] Natural Minor Scale // 1 - 2 - b3 - 4 - 5 - b6 - b7 ")
            result_2 = data['min'][w][0]
            print(result_2)
            return result_2


    pentatonic(w)
    major_minor_scale(w)
    print()