# Wczytujemy napis
text = input()

# Pierwsza metoda
# Definujemy napis, który będziemy tworzyć
result = ""
# Dla każdej litery w napisie na wejściu sprawdzamy czy musimy ją zamienić.
for char in text:
    if char == 'a':
        result += str(4)
    elif char == 'e':
        result += str(3)
    elif char == 'i':
        result += str(1)
    elif char == 'o':
        result += str(0)
    elif char == 's':
        result += str(5)
    else:
        result += char

# # Druga metoda
# code = (('a', 4), ('e', 3), ('i', 1), ('o', 0), ('s', 5))
# for i in code:
#     text = text.replace(i[0], str(i[1]))
# print(text)

# Trzecia metoda
dcode = {
    'a': 4,
    'e': 3,
    'i': 1,
    'o': 0,
    's': 5
}
# for i in dcode:
#     text = text.replace(i, str(dcode[i]))

for char, encode in dcode.items():
    text = text.replace(char, str(encode))

print(text)
