length = int(input())
for i in range(1, length+1):
    if not i % 7 and not i % 11:
        print("Wiwat!")
    elif not i % 7:
        print("Hurra!")
    elif not i % 11:
        print("Super!")
    else:
        print(i)
