def pentatonic(key, data):
    if key in data['maj']:
        # print(f" [{key.title()}] Major Pentatonic Scale // 1 - 2 - 3 - 5 - 6 ")
        result = data['maj'][key][0][0:3]+data['maj'][key][0][4:6]
        return result

    elif key in data['min']:
        #print(f" [{key.title()}] Minor Pentatonic // 1 - b3 - 4 - 5 - b7 ")
        result = data['min'][key][0][:1]+data['min'][key][0][2:5]+data['min'][key][0][-1:]
        return result


def major_minor_scale(key, data):
    if key in data['maj']:
       #print(f" [{key.title()}] Major Scale // 1 - 2 - 3 - 4 - 5 - 6- 7 ")
        result = data['maj'][key][0]
        return result

    elif key in data['min']:
       #print(f" [{key.title()}] Natural Minor Scale // 1 - 2 - b3 - 4 - 5 - b6 - b7 ")
        result = data['min'][key][0]
        return result


def melodic_minor_scale(key, data):
    if key in data['min']:
        #print(f" [{key.title()}] Melodic Minor Scale // R - 2 - b3 - 4 - 5 - 6 - 7 ")
        result = data['min'][key][0][0:5]+data['min'][key][1][0:]
        return result


def harmonic_minor_scale(key, data):
    if key in data['min']:
        #print(f" [{key.title()}] Harmonic Minor Scale // R - 2 - b3 - 4 - 5 - b6- 7 ")
        result = data['min'][key][0][0:6]+data['min'][key][1][1:]
        return result


def blues_scale(key, data):
    if key in data['min']:
        #print(f" [{key.title()}] Blues Scale // R - b3 - 4 - b5 - 5 - b7 ")
        result = data['min'][key][0][:1]+data['min'][key][0][2:4]+data['min'][key][2]
        return result
