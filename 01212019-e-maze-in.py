# Hint 1. To get the input as string, use the following code:
S = input()

# Hint 2. You can define x and y variable, and set to (0, 0)
x, y = 0, 0

# Hint 3. Change x or y based on a direction in a for-loop.
for c in S:
    if c == 'L':
        # do something
    elif c == 'R':
        # do something
...















# My solution:
S = input()
x, y = 0, 0
for c in S:
    if c == 'L':
        x -= 1
    elif c == 'R':
        x += 1
    elif c == 'D':
        y -= 1
    elif c == 'U':
        y += 1
print('{} {}'.format(x, y))
