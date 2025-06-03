# pop in different
def push(value):
    top=-1
    if(top==4):
        return "stack is full"
    else:
        top=top+1
        return stack.append(value)
        
def pop():
    top=5
    if(top!=-1):
        return stack.pop()
    else:
        top-=1
        return "stack is empty"
top=-1
size=50
stack=[None]*size
push(20)
push(30)
push(40)
push(50)
push(60)
push(70)
push(80)
pop()
pop()
pop()
print(stack)
print(stack)