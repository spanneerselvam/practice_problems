s = "sairam "
def reverse_string(s):
    w = ""
    for i in range(len(s)-1, -1, -1):
        w+=str(s[i])
    return w 

print(reverse_string(s))
