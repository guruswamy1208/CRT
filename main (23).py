# stack all program
stack=[]
top= -1
def push(value):
    global top
    stack.append(value)
    top +=1

def pop():
    global top
    if top== -1:
        print("stack is empty. nothing to pop")
        return 
    else:
        stack.pop()
        top -= 1
def peek():
    if top == -1:
        return "stack is empty. no top element"
    else:
        return f"top element ={stack[top]}"
        
def display():
    if(top==-1):
        print("empty")
    else:
        for i in range(top,-1,-1):
            print(stack[i])
push(10)     #top=0
push(30)    #top=11
push(50)    #top=2
push(70)    #top=3
pop()
pop()
print(peek())
display()