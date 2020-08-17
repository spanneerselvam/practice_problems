
s = "saigopinipanneerselvam"
def frequent_letters(s):
    d = {key: 0 for key in s}
    for i in s:
        d[i] += 1 
    repeated = []
    max_item = max(d.values())
    for key, values in d.items():
        if values == max_item:
            repeated.append(key)
    for item in repeated:
        print(item, ":", max_item)


def second_frequent_letters(s):
    d = {key: 0 for key in s}
    for i in s:
        d[i] += 1 
    repeated = list(sorted(set(d.values())))
    second_item = repeated[len(repeated)-2]
    repeated = list()
    for key, value in d.items():
        if value == second_item:
            repeated.append(key)
    for item in repeated:
        print(item, ":", second_item)

second_frequent_letters(s)
