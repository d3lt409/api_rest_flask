class Node():

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        
    def __str__(self) -> str:
        return f"<Node {self.value}>"
    
    def _get_nodes(self):
        return [self.right,self.left]

        
    def get_children(self):
        def iter_children(nodes,parent=None, resl:dict={}):
            for nod in nodes:
                if not nod:
                    return resl[parent.value]
                resl[parent.value] = resl.get(parent.value,[])+[nod.value]
                return iter_children(nod._get_nodes(), nod, resl)
                
    
        return iter_children(self._get_nodes(), self)
    
    
    def add_node(self,node):
        if not self.right: self.right = node
        elif  not self.left: self.left = node
        else:
            raise IndexError("No se puede agregar el nodo")
        
    
    def print_node(self):
      if self.left:
         self.left.print_node()
      print(self.value)
      if self.right:
         self.right.print_node()
        

class Tree:
    
    def __init__(self, root:int) -> None:
        self.root = Node(root)
        self.nodes = [self.root]
        
    def add_branch(self,nodes):
        for i in range(len(nodes)):
            if nodes[i] not in self._get_nodes_values():
                parent_node = self.get_node_value(nodes[i-1])
                child = Node(nodes[i])
                parent_node.add_node(child)
                child.parent = parent_node
                self.nodes.append(child)
    
    def _get_nodes_values(self):
        return [node.value  for node in self.nodes]
    
    def get_node_value(self,value):
        for node in self.nodes:
            if node.value == value: return node  
        return None
    

    def ancestor(self,node1,node2):
        node1 = self.get_node_value(node1)
        node2 = self.get_node_value(node2)

        if node1 and node2:
            def search_parent(node,values):
                if not node.parent: return values
                values.append(node.parent.value)
                return search_parent(node.parent,values)
            parent_n1 = search_parent(node1,[])
            parent_n2 = search_parent(node2,[])
            val = next(i for i in parent_n1 if i in parent_n2)
            return val
        
        return None
            
    
    def print_tree(self):
        self.root.print_node()
    
    
        


in1 = (70,84,85)
int2 = (70,84,78,80)
int3 = (70,84,78,76)
int4 = (70,49,54,51)
int5 = (70,49,37,40)
int6 = (70,49,37,22)

t = Tree(in1[0])
t.add_branch(in1)
t.add_branch(int2)
t.add_branch(int3)
t.add_branch(int4)
t.add_branch(int5)
t.add_branch(int6)

print("\n")
print(t.ancestor(40,78))
print(t.ancestor(51,37))
print(t.ancestor(76,85))
print ('%.2f' % 1714.666) 