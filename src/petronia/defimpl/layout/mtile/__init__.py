
"""
Default tiler for Petronia.

This implements the `layout.tile` api by providing a tree-like hierarchy of
containers and tiles, where the leaf nodes of the tree are the actual tiles.

The root of the tree is a virtual node that represents all the displays.
Each display container splits its children vertically, then each child under
that splits in the opposite direction of its parent.
"""
