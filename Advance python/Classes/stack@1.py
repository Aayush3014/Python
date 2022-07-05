# WAP to implemenet different stack operations.

class node:
    def empty(stk):
        
        if stk == []:
            return True
        
        else:
            return False

    def push(stk, item):
        stk.append(item)
        top = len(stk) - 1

    def pop(stk):
        
        if node.empty(stk):
            return "underflow"
        
        else:
            item = stk.pop()
            
            if len(stk) == 0:
                return None
            
            else:
                top = len(stk) - 1

    def peek(stk):
        
        if node.empty(stk):
            return "underflow"
        
        else:
            top = len(stk)
            return stk[top-1]

    def display(stk):
        
        if node.empty(stk):
            print("Empty Stack")
        
        else:
            top = len(stk)
            for i in range(top):
                print(stk[i],end=" ")
            print()

stack = []
top = None

while True:
    print("""
Enter the stack operation which you want to implement ------->
1.Push
2.Pop 
3.Peek
4.Display
5.Exit""")
    
    operation = int(input("Enter the option value : "))
    
    if operation == 1:
        item = int(input("Enter the item you want to push : "))
        node.push(stack, item)

    elif operation == 2:
         if node.pop(stack):
            print("Stack is empty.")
         else:
            print(f"Deleted  item is {item}")

    elif operation == 3:
        item = node.peek(stack)
        if item == "underflow":

            print("No item available.")
        else:
            print(f"Item at the top of stack is {item}")

    elif operation == 4:
        node.display(stack)
    
    else:
        exit()