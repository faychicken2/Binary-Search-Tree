class BinarySearchTree:
    def __init__(self, val=None):
        self.left = None    
        self.right = None   
        self.val = val      

    # pushing data into the tree 
    def push(self, val):
        # checking if val is null
        # if it is then we assign it a value
        if not self.val:
            self.val = val
            return

        # cheching if the value we are pushing is already in it
        # if it is then we do nothing
        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.push(val)
                return
            self.left = BinarySearchTree(val)
            return

        if self.right:
            self.right.push(val)
            return
        self.right = BinarySearchTree(val)

    # delete a node from the tree
    def delete(self, val):
        # checking if the node in empty
        if self == None:
            return self
        # checking if val and self.val are the same
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        # finding were to look for the node
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val) 
            return self
        # checking if the right branch is null 
        if self.right == None:
            return self.left
        # checking if the left branch is null
        if self.left == None:
            return self.right
        min_larger_node = self.right
        # looping through the right branch
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)

    # Traversing the tree in order
    def Traverse(self, vals):
        if self.left is not None:
            self.left.Traverse(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.Traverse(vals)
        return vals

    # getting the min value in the tree
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    # getting the max value in the tree
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

        return self

def main():
    import random

    tree = BinarySearchTree()   # initializing the class

    numbersToPush = []  # list of numbers to be pushed to the tree
    # adding radom numbers to the tree
    for x in range(20):
        numbersToPush.append(int(random.uniform(0, 99)))

    print("pushing to tree " + str(numbersToPush))
    # pushing the numbers to the tree
    for num in numbersToPush:
        tree.push(num)

    print()
    print("Traverse the tree in order: ", tree.Traverse([])) # Traverse the tree in order
    print()


    numbersToDel = []   # list of random numbers to be deleted
    for x in range(10):
        numbersToDel.append(int(random.uniform(0, 99)))
        
    print("deleting from tree " + str(numbersToDel))
    # deleting the numbers from the tree
    for num in numbersToDel:
        tree.delete(num)

    print()
    print("Traverse the tree in order: ", tree.Traverse([])) # Traverse the tree in order
    print()

    # getting the min and max values in the tree
    print("The Max value in the tree is ", tree.get_max())
    print("The Min value in the tree is ", tree.get_min())




if __name__ == '__main__':
    main()
