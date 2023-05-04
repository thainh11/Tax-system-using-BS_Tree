class BStree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self, node):
        if self.isEmpty():
            self.root = node
        else:
            cur = self.root
            while cur:
                if node.data.code < cur.data.code:
                    if cur.left == None:
                        cur.left = node
                    cur = cur.left
                elif node.data.code > cur.data.code:
                    if cur.right == None:
                        cur.right = node
                    cur = cur.right
                elif node.data.code == cur.data.code:
                    return f"code {node.data.code} has existed"

    def in_Order(self, node):
        if self.isEmpty():
            print("Nothing in the list")            
            return None        
        if node == None:
            return
        else:
            self.in_Order(node.left)
            print(node.data)
            self.in_Order(node.right)
    
    def pre_Order(self, node):
        if self.isEmpty():
            print("Nothing in the list")            
            return None
        if node == None:
            return
        else:
            print(node.data)
            self.pre_Order(node.left)
            self.pre_Order(node.right)   

    def breadth_First(self):    
        if self.isEmpty():
            return None
        queue = []
        queue.append(self.root) #append thêm phần tử vào cuối - enqueue
        while queue != []:
            node = queue[0]
            queue = queue[1:] #dequeue
            #pop() lấy phần tử cuối, không phải ptu đầu => khác dequeue
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
 
    def findNode(self, code):
        if self.isEmpty():
            print("Nothing in the list")            
            return None
        node = self.root
        while node:
            if code > node.data.code:
                node = node.right
            elif code < node.data.code:
                node = node.left
            else:
                return node.data
        return "Not in tree"

    def delete_by_copy(self, root, code): #Copying Left
        if not root: return None
        if root.data.code == code:
            if not root.right and not root.left: return None
            if not root.right and root.left: return root.left
            if root.right and not root.left: return root.right
            else:
                temp = root.left
                while temp.right:  temp = temp.right
                root.data = temp.data
                temp = None
        elif root.data.code > code:
            root.left = self.delete_by_copy(root.left, code)
        else:
            root.right = self.delete_by_copy(root.right, code)
        return root 
 
    def storeNode(self, root, nodes):
        if not root:
            return
        self.storeNode(root.left, nodes)
        nodes.append(root)
        self.storeNode(root.right, nodes)
 
    def buildTree(self, nodes, start, end):
        if start > end:
            return None
        mid = (start+end) // 2
        node = nodes[mid]
    
        node.left = self.buildTree(nodes, start, mid-1)
        node.right = self.buildTree(nodes, mid+1, end)
        return node
    
    def balance_Tree(self, root):
        nodes = []
        self.storeNode(root, nodes)
        n = len(nodes)
        self.root = self.buildTree(nodes, 0, n-1)
    
    global nodeList
    nodeList = []
    def in_OrderNode(self, node):
        if self.isEmpty():   
            return None        
        if node == None:
            return
        else:
            self.in_OrderNode(node.left)
            nodeList.append(node)
            self.in_OrderNode(node.right)
            return nodeList

    def turnLeft(self, nodeList): 
        if self.isEmpty():
            print("Nothing in the list")
            return
        nodeList = nodeList[::-1]
        i = 0
        for node in nodeList:
            node.left = None
            node.right = None
        for node in nodeList:
            if i == 0:
                self.root = node
            else:
                self.insert(node)
            i += 1

    global list1
    list1 = []
    def count(self, node):
        if self.isEmpty():
            return 0      
        if node == None:
            return
        else:
            self.count(node.left)
            self.count(node.right)
            list1.append(node)
        if node == self.root:
            return len(list1)

