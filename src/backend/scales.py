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
            result = data['maj'][w][0][0:3]+data['maj'][w][0][4:6]
            print(result)
            print()
            return result

        elif w in data['min']:
            print(f" [{w.title()}] Minor Pentatonic // 1 - b3 - 4 - 5 - b7 ")
            result = data['min'][w][0][:1]+data['min'][w][0][2:5]+data['min'][w][0][-1:]
            print(result)
            print()
            return result


    def major_minor_scale(w):
        if w in data['maj']:
            print(f" [{w.title()}] Major Scale // 1 - 2 - 3 - 4 - 5 - 6- 7 ")
            result = data['maj'][w][0]
            print(result)
            print()
            return result

        elif w in data['min']:
            print(f" [{w.title()}] Natural Minor Scale // 1 - 2 - b3 - 4 - 5 - b6 - b7 ")
            result = data['min'][w][0]
            print(result)
            print()
            return result


    def melodic_minor_scale(w):
        if w in data['min']:
            print(f" [{w.title()}] Melodic Minor Scale // R - 2 - b3 - 4 - 5 - 6 - 7 ")
            result = data['min'][w][0][0:5]+data['min'][w][1][0:]
            print(result)
            print()
            return result


    def harmonic_minor_scale(w):
        if w in data['min']:
            print(f" [{w.title()}] Harmonic Minor Scale // R - 2 - b3 - 4 - 5 - b6- 7 ")
            result = data['min'][w][0][0:6]+data['min'][w][1][1:]
            print(result)
            print()
            return result


    def blues_scale(w):
        if w in data['min']:
            print(f" [{w.title()}] Blues Scale // R - b3 - 4 - b5 - 5 - b7 ")
            result = data['min'][w][0][:1]+data['min'][w][0][2:4]+data['min'][w][2]
            print(result)
            print()
            return result


    pentatonic(w)
    print()
    major_minor_scale(w)
    print()
    melodic_minor_scale(w)
    print()
    harmonic_minor_scale(w)
    print()
    blues_scale(w)
