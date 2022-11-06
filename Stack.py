#importing collections.deque
from collections import deque

stack = deque()

# append() function to push the element in the stack
stack.append('Ahmed')
stack.append('111')
stack.append('12 years old')
print('Initial stack:')
print(stack)

# pop() function to pop the elements from the stack

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped all:')
print(stack)



