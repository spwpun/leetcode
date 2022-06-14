import string

line = input()
key_dict = {"abc":"2", "def":"3","ghi":"4", "jkl":"5","mno":"6","pqrs":"7","tuv":"8","wxyz":"9"}
en = ""
for ch in line:
    if ch in string.ascii_uppercase:
        if ch == "Z":
            ch = 'a'
        else:
            ch = chr(ord(ch.lower()) + 1)
    elif ch in string.ascii_lowercase:
        for key in key_dict.keys():
            if ch in key:
                ch = key_dict[key]
    else:
        pass
    en += ch
print(en)