# mindmap_composite.py

class MindMapComposite:
    def __init__(self, name, shape):
        """Composite node for the mind map (can have children)."""
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        """Add a child node (leaf or composite)."""
        self.children.append(child)

    def remove(self, child):
        """Remove a child node."""
        self.children.remove(child)

    def __str__(self):
        """Return the composite name formatted with the shape."""
        shape_representation = self.get_shape_representation()
        return shape_representation.format(self.name)

    def display(self, indent=0):
        """Print this node and then all children with indentation."""
        spaces = " " * indent
        print(spaces + str(self))
        for child in self.children:
            child.display(indent + 2)

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
