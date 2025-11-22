# mindmap_leaf.py

class MindMapLeaf:
    def __init__(self, name, shape):
        """Leaf node for the mind map (no children)."""
        self.name = name
        self.shape = shape

    def __str__(self):
        """Return the name formatted with the shape."""
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def display(self, indent=0):
        """Print this leaf with indentation."""
        spaces = " " * indent
        print(spaces + str(self))

    def get_shape_representation(self):
        """Return the shape template string."""
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}((",
        }
        # default is just the text with no shape
        return shapes.get(self.shape, "{}")
