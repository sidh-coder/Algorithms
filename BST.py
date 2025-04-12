
class Node:
    def __init__(self,value,left=None,right=None):
        self.left = left
        self.right = right
        self.value = value

def insert(root,value):
    if root == None:
        return(Node(value))
    elif(value<root.value):
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return(root)

def postorder(root,result):
    if(root.left!=None):
        postorder(root.left,result)
    if(root.right!=None):
        postorder(root.right,result)
    result.append(root.value)

def preorder(root,result):
    result.append(root.value)
    if(root.left!=None):
        preorder(root.left,result)
    if(root.right!=None):
        preorder(root.right,result)

def inorder(root,result):
    if(root.left!=None):
        inorder(root.left,result)
    result.append(root.value)
    if(root.right!=None):
        inorder(root.right,result)
def find(value,root):
    if(value<root.value):
        node = find(value,root.left)
    elif(value>root.value):
        node = find(value,root.right)
    elif(value == root.value):
        return(root)
    return(node)
def find_min(root):
    if(root.left!=None):
        min = find_min(root.left)
    else:
        return(root)
    return(min)
def display(root):
    op = int(input("enter 1 for inorder 2 for preorder 3 for postorder: "))
    result = []
    match op:
        case 1:
            inorder(root,result)
            for i in result:
                print(i,end=',')
        case 2:
            preorder(root,result)
            for i in result:
                print(i,end=',')
        case 3:
            postorder(root,result)
            for i in result:
                print(i,end=',')
        case _:
            main()
    return
def delete(root,value):
    if(value<root.value):
        root.left = delete(root.left,value)
    elif(value>root.value):
        root.right = delete(root.right,value)
    elif(value==root.value):
        if(root.left == None and root.right ==None):
            root = None
            return(root)
        elif(root.left!=None and root.right == None):
            root = root.left
            return(root)
        elif(root.left==None and root.right!=None):
            root = root.right
            return(root)
        else:
            min = find_min(root.right)
            root.right=delete(root.right,min.value)
            root.value = min.value

            
    return(root)
def main():
    root = None  
    while True:
        option = int(input("enter 1 to insert 2 to display 3 to delete 4 to find: "))
        match option:
            case 1:
                while(True):
                    value = int(input("enter value of node(-1 to break): "))
                    if(value == -1):
                        break
                    root = insert(root,value)
            case 2:
                display(root)
            case 3:
                value = int(input("enter value to delete: "))
                root = delete(root,value)
            case 4:
                value = int(input("enter value to find: "))
                node = find(value,root)
                print(node.value)

main()