from init_app import db
import sqlalchemy as sa


class BinaniTree(db.Model):
    __tablename__ = "binari_tree"
    
    id = sa.Column(sa.Integer, primary_key = True)
    value = sa.Column(sa.Integer, unique = True)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey('binari_tree.id'), nullable = True)
        
    def __init__(self, value:int, parent_id=None) -> None:
        self.value = value
        self.parent_id = parent_id

    @staticmethod
    def create_tree(nodes):
        for node in nodes:
            parent = BinaniTree.search_node( node["parent"])
            tree = BinaniTree(node["node"], parent.id)
            db.session.add(tree)
            db.session.commit()
            
    @staticmethod
    def search_node(value):
        return db.session.query(BinaniTree).filter_by(value = value).first()
    
    @staticmethod
    def search_node_id(value):
        return db.session.query(BinaniTree).filter_by(id = value).first()
    
    @staticmethod
    def get_nodes():
        return db.session.query(BinaniTree).all()
           
    @staticmethod 
    def ancestor(value1,value2):
        node1:BinaniTree = BinaniTree.search_node(value1)
        node2:BinaniTree = BinaniTree.search_node(value2)

        if node1 and node2:
            def search_parent(node:BinaniTree,values:list):
                if not node or not node.parent_id: return values
                values.append(node.parent_id)
                return search_parent(BinaniTree.search_node_id(node.parent_id),values)
            parent_n1 = search_parent(node1,[])
            parent_n2 = search_parent(node2,[])
            try:
                val:int = next(i for i in parent_n1 if i in parent_n2)
                return BinaniTree.search_node_id(val).value
            except StopIteration as _:
                return None
    
    