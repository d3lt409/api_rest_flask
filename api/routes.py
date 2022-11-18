from flask import current_app as app, request, jsonify
from models import BinaniTree, db

@app.route("/api/create/tree",methods=['POST'])
def create_tree():
    data = request.get_json()
    if request.method == "POST":
        root = BinaniTree(int(data["root"]))
        db.session.add(root)
        db.session.commit()
        BinaniTree.create_tree(data["tree"])
        return jsonify({"created":"successfully"}), 200
    
@app.route("/api/tree/ancester", methods= ["GET"])
def get_ancester():
    node1 = int(request.args.get("node1"))
    node2 = int(request.args.get("node2"))
    value = BinaniTree.ancestor(node1,node2)
    if value:
        return jsonify({"node1": node1, "node2":node2, "ancestor": value}),200
    else: 
        return jsonify({"node1": node1, "node2":node2, "ancestor": None}),404