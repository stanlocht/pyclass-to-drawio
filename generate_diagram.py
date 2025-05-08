"""
Script to generate a class diagram from the model_classes module.

This script demonstrates how to use the ClassDiagramGenerator to create
a diagram of the classes in the model_classes module.
"""

import os
from class_diagram_generator import generate_class_diagram

if __name__ == "__main__":
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Generate the diagram
    diagram_path = generate_class_diagram(
        module_name="model_classes",
        output_dir=current_dir,
        file_name="pet_classes_diagram.drawio",
        direction="down",
        link_style="orthogonal",
    )

    print(f"Diagram generated at: {diagram_path}")
    print("You can open this file with draw.io or the draw.io VS Code extension.")
