def triad(key, data):
    if key in data['aug']:
        scale = data['aug'][key]
    elif key in data['maj']:
        scale = data['maj'][key][0]
    elif key in data['min']:
        scale = data['min'][key][0]
    elif key in data['dim']:
        scale = data['dim'][key]
    else:
        return None, None, None

    # root_pos = [scale[0],scale[2],scale[4]]
    root_pos = f" {scale[0]} - {scale[2]} - {scale[4]}  "

    # first_inv = [scale[2], scale[4], scale[0]]
    first_inv = f" {scale[2]} - {scale[4]} - {scale[0]}  "

    # second_inv = [scale[4], scale[0], scale[2]]
    second_inv = f" {scale[4]} - {scale[0]} - {scale[2]} "

    return root_pos, first_inv, second_inv


# if w in aug:
#     print(f"TRIAD              {w.capitalize()}          ")
#     result_1 = aug[w][0] + "-" + aug[w][2] + "-" + aug[w][4]
#     print("Root  // 1-3-#5 //", result_1, " // DO - MI - SO")
#     result_2 = aug[w][2] + "-" + aug[w][4] + "-" + aug[w][0]
#     print("1st  // 3-#5-1 //", result_2, " //  MI - SO - DO")
#     result_3 = aug[w][4] + "-" + aug[w][0] + "-" + aug[w][2]
#     print("2nd // #5-1-3 //", result_3, " //   SO - DO - MI")
#
# elif w in maj:
#     print(f"TRIAD              {w.capitalize()}major         ")
#     result_1 = maj[w][0][0] + "-" + maj[w][0][2] + "-" + maj[w][0][4]
#     print("Root  // 1-3-5 //", result_1, " // DO - MI - SO")
#     result_2 = maj[w][0][2] + "-" + maj[w][0][4] + "-" + maj[w][0][0]
#     print("1st  // 3-5-1 //", result_2, " //  MI - SO - DO")
#     result_3 = maj[w][0][4] + "-" + maj[w][0][0] + "-" + maj[w][0][2]
#     print("2nd // 5-1-3 //", result_3, " //   SO - DO - MI")
#
# elif w in min:
#     print(f"TRIAD                {w.capitalize()}inor          ")
#     result_1 = min[w][0][0] + "-" + min[w][0][2] + "-" + min[w][0][4]
#     print("Root  // 1-b3-5 // ", result_1, " // DO - MI - SO")
#     result_2 = min[w][0][2] + "-" + min[w][0][4] + "-" + min[w][0][0]
#     print("1st  // b3-5-1 // ", result_2, " //  MI - SO - DO")
#     result_3 = min[w][0][4] + "-" + min[w][0][0] + "-" + min[w][0][2]
#     print("2nd // 5-1-b3 // ", result_3, " //   SO - DO - MI")
#
# elif w in dim:
#     print(f"TRIAD                {w.capitalize()}      ")
#     result_1 = dim[w][0] + "-" + dim[w][2] + "-" + dim[w][4]
#     print(f"Root  // 1-b3-b5 // ", result_1, " // DO - MI - SO")
#     result_2 = dim[w][2] + "-" + dim[w][4] + "-" + dim[w][0]
#     print("1st  // b3-b5-1 // ", result_2, " //  MI - SO - DO")
#     result_3 = dim[w][4] + "-" + dim[w][0] + "-" + dim[w][2]
#     print("2nd // b5-1-b3 // ", result_3, " //   SO - DO - MI")