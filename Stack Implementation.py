#Stack Implementation

#Creating a Stack
def create_stack():
    stack = []
    return stack

#Creating stack is empty
def check_empty(stack):
    return len(stack) == 0

#Adding items into the Stack
def push(stack,item):
    stack.append(item)
    print("Pushed Item:",item)
    print("Stack Items",str(stack))

#Removing an item from the Stack
def pop(stack):
    if(check_empty(stack)):
        return "Stack is Empty"
    return stack.pop()

#find Peek
def peek(stack):
    peekItem = 0
    if(check_empty(stack)):
        return "stack is Empty"
    else:
        for i in stack:
            peekItem = i
    print("Peek of the Stack:",peekItem)


stack = create_stack()
#check_empty(stack)
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
check_empty(stack)
peek(stack)
print("Popped Item:",pop(stack))
print("Popped Item:",pop(stack))
print("Popped Item:",pop(stack))
print("Popped Item:",pop(stack))
peek(stack)
print("Stack after Popping the Item",str(stack))
