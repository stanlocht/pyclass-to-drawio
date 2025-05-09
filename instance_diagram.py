"""
Script to create a diagram of instances and their relationships.

This script demonstrates how to create a diagram showing relationships
between instances of classes from the model_classes module.
"""

import os
import drawpyo
from drawpyo.diagram_types import TreeDiagram, NodeObject
from model_classes import Animal, Dog, Cat, Owner, Veterinarian, PetShop


def create_instance_diagram(output_dir=None, file_name="pet_instances_diagram.drawio"):
    """
    Create a diagram showing relationships between instances.

    Args:
        output_dir: Directory where the diagram will be saved
        file_name: Name of the output file

    Returns:
        Path to the generated diagram file
    """
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    # Create instances
    fido = Dog("Fido", 3, "Golden Retriever")
    whiskers = Cat("Whiskers", 2, "Tabby")
    mittens = Cat("Mittens", 4, "Calico")

    john = Owner("John")
    john.add_pet(fido)

    sarah = Owner("Sarah")
    sarah.add_pet(whiskers)
    sarah.add_pet(mittens)

    dr_smith = Veterinarian("Smith", "General")
    dr_smith.treat(fido)
    dr_smith.treat(whiskers)

    pet_palace = PetShop("Pet Palace")
    pet_palace.hire_veterinarian(dr_smith)

    # Create the diagram
    tree = TreeDiagram(
        file_path=output_dir,
        file_name=file_name,
        direction="down",
        link_style="orthogonal",
    )

    # Create nodes for each instance
    nodes = {}

    # Pet nodes
    nodes["fido"] = NodeObject(tree=tree, value="Fido (Dog)", base_style="rounded rectangle")
    nodes["fido"].apply_style_string("fillColor=#d5e8d4;strokeColor=#82b366;")  # Green

    nodes["whiskers"] = NodeObject(
        tree=tree, value="Whiskers (Cat)", base_style="rounded rectangle"
    )
    nodes["whiskers"].apply_style_string("fillColor=#d5e8d4;strokeColor=#82b366;")  # Green

    nodes["mittens"] = NodeObject(tree=tree, value="Mittens (Cat)", base_style="rounded rectangle")
    nodes["mittens"].apply_style_string("fillColor=#d5e8d4;strokeColor=#82b366;")  # Green

    # Owner nodes
    nodes["john"] = NodeObject(tree=tree, value="John (Owner)", base_style="rounded rectangle")
    nodes["john"].apply_style_string("fillColor=#dae8fc;strokeColor=#6c8ebf;")  # Blue

    nodes["sarah"] = NodeObject(tree=tree, value="Sarah (Owner)", base_style="rounded rectangle")
    nodes["sarah"].apply_style_string("fillColor=#dae8fc;strokeColor=#6c8ebf;")  # Blue

    # Vet node
    nodes["dr_smith"] = NodeObject(
        tree=tree, value="Dr. Smith (Vet)", base_style="rounded rectangle"
    )
    nodes["dr_smith"].apply_style_string("fillColor=#fff2cc;strokeColor=#d6b656;")  # Yellow

    # Pet shop node
    nodes["pet_palace"] = NodeObject(
        tree=tree, value="Pet Palace (Shop)", base_style="rounded rectangle"
    )
    nodes["pet_palace"].apply_style_string("fillColor=#f8cecc;strokeColor=#b85450;")  # Red

    # Add ownership relationships
    nodes["fido"].tree_parent = nodes["john"]
    nodes["whiskers"].tree_parent = nodes["sarah"]
    nodes["mittens"].tree_parent = nodes["sarah"]

    # Add vet-patient relationships
    add_relationship(tree, nodes["dr_smith"], nodes["fido"], "treats")
    add_relationship(tree, nodes["dr_smith"], nodes["whiskers"], "treats")

    # Add pet shop relationship
    nodes["dr_smith"].tree_parent = nodes["pet_palace"]

    # Auto-layout the diagram
    tree.auto_layout()

    # Write the diagram to a file
    tree.write()

    return os.path.join(output_dir, file_name)


def add_relationship(tree, source, target, label=None):
    """
    Add a relationship between two nodes.

    Args:
        tree: The TreeDiagram
        source: Source node
        target: Target node
        label: Optional label for the relationship
    """
    link = drawpyo.diagram.Edge(
        page=tree.page,
        source=source,
        target=target,
        value=label,
    )
    link.apply_style_string("endArrow=open;dashed=1;strokeWidth=1.5;")
    return link


if __name__ == "__main__":
    # Create the instance diagram
    diagram_path = create_instance_diagram()

    print(f"Instance diagram generated at: {diagram_path}")
    print("You can open this file with draw.io or the draw.io VS Code extension.")
