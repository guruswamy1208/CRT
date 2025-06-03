# Enter your code here stack
def push(value):
    top=-1
    if(top==4):
        return "stack is full"
    else:
        top=top+1
        return stack.append(value)
stack=[10]        # size as 5
push(20)
push(30)
push(40)
push(50)
push(60)
push(70)
push(80)
print(stack)