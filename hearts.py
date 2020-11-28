hearts = int(input())
heart = """\
 @@@   @@@
@   @ @   @
@    @    @
@         @
 @       @
  @     @
   @   @
    @ @
     @\
"""
for i in range(hearts-1):
    print(heart)
print(heart, end='')
