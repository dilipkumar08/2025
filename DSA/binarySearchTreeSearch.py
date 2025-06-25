def binarySearchTree(node,val):
    if not node:
        return 
    elif node.data==val:
        return node
    elif node.data>val:
        return binarySearchTree(node.left,val)
    else:
        return binarySearchTree(node.right,val)
