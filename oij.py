text = input()
result = 0
lastFound = 'j'
for character in text:
    if lastFound == 'j' and character == 'o':
        lastFound = character
    elif lastFound == 'o' and character == 'i':
        lastFound = character
    elif lastFound == 'i' and character == 'j':
        lastFound = character
        result += 1
if not result:
    print("NIE")
else:
    print(result)
