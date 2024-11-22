from collections import deque

numbers = input()
nmb=numbers.split()
stack = deque()

for i in nmb:
    a=int(i)
    stack.append(a)

print("stack1", stack)

for i in range(len(stack)):
    number = stack.pop()
    print(int(number)** 2)
