import onnx
from collections import defaultdict

def list_op_names_with_count(model_path):
    # Load the ONNX model
    model = onnx.load(model_path)

    # Initialize a dictionary to count operator usage
    op_count = defaultdict(int)

    # Iterate through all nodes in the graph and count the usage of each operator
    for node in model.graph.node:
        op_count[node.op_type] += 1

    return dict(op_count)

# Example usage:
model_path = "model.onnx"
ops = list_op_names_with_count(model_path)
for op, count in ops.items():
    print(f"{op}: {count}")
