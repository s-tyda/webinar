hearts = int(input())
heart = [
    " @@@   @@@ ",
    "@   @ @   @",
    "@    @    @",
    "@         @",
    " @       @ ",
    "  @     @  ",
    "   @   @   ",
    "    @ @    ",
    "     @     "]

for line in heart:
    for i in range(hearts):
        if i > 0:
            print(line, end=' ')
        else:
            print(line, end='')
    print()
