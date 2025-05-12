def chords(key, data):
    MAJOR = ["", "m", "m", "", "", "m", "dim"]
    MAJOR7 = ["maj7", "min7", "min7", "maj7", "7", "m7", "m7b5"]
    MINOR = ["m", "dim", "", "m", "m", "", ""]
    MINOR7 = ["min7", "m7b5", "maj7", "min7", "min7", "maj7", "7"]
    NUM_MIN = ["i.", "iidim.", "III.", "iv.", "v.", "VI.", "VII."]
    NUM_MAJ = ["I.", "ii.", "iii.", "IV.", "V.", "vi.", "vii."]


#ToDo Namenänderung -

    if key in data['maj']:
        scale = data['maj'][key][0]
        major_scale =[]
        major7_scale = []
        for i in range(7):
            major_scale.append(scale[i] + MAJOR[i])
            major7_scale.append(scale[i] + MAJOR7[i])
            # major7_scale.append(NUM_MAJ[i] + scale[i] + MAJOR7[i])

        # print()
        # print(f"                Chords of [{key.title()}]")
        # print("  I.   II.  III.  IV.   V.   VI.   VII.")
        # print(major_scale_comb)
        # print()
        # print(major_scale_full_comb)
        # print()
        return major_scale, major7_scale

    if key in data['min']:
        scale = data['min'][key][0]
        minor_scale =[]
        minor7_scale = []
        for i in range(7):
            minor_scale.append(scale[i] + MINOR[i])
            minor7_scale.append(scale[i] + MINOR7[i])
            # minor7_scale.append(NUM_MIN[i] + scale[i] + MINOR7[i])

        # print("   I.    II.   III.  IV.    V.   VI. VII.")
        # print(natural_minor_comb)
        # print()
        # print(natural_minor_full_comb)
        # print()
        return minor_scale, minor7_scale

# test
# import json
#
# with open('data/scales.json', 'r') as file:
#     data = json.load(file)
#
# print(chords("cm", data))
