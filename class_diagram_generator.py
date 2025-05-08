"""
Class Diagram Generator - Creates draw.io diagrams from Python classes.

This module provides a simple way to generate class diagrams from Python modules.
It analyzes class inheritance and composition relationships and creates a visual
representation using the drawpyo library.
"""

import inspect
import importlib
import os
from typing import Dict, Type
import drawpyo
from drawpyo.diagram_types import TreeDiagram, NodeObject


class ClassDiagramGenerator:
    """Generates draw.io diagrams from Python classes."""
    
    def __init__(self, output_dir="."):
        """
        Initialize the diagram generator.
        
        Args:
            output_dir: Directory where the diagram will be saved
        """
        self.output_dir = output_dir
        self.inheritance = {}
        self.composition = {}
        self.all_classes = set()
    
    def generate_diagram(self, module_name, file_name=None, direction="down", link_style="orthogonal"):
        """
        Generate a class diagram for a module.
        
        Args:
            module_name: Name of the module to analyze
            file_name: Name of the output file (defaults to module_name + _diagram.drawio)
            direction: Direction of the tree (up, down, left, right)
            link_style: Style of links (orthogonal, straight, curved)
            
        Returns:
            Path to the generated diagram file
        """
        # Analyze the module
        self._analyze_module(module_name)
        
        # Set up the file name
        if file_name is None:
            file_name = f"{module_name.split('.')[-1]}_diagram.drawio"
        
        # Create the tree diagram
        tree = TreeDiagram(
            file_path=self.output_dir,
            file_name=file_name,
            direction=direction,
            link_style=link_style,
        )
        
        # Create node objects for each class
        nodes = {}
        for class_name in self.all_classes:
            nodes[class_name] = NodeObject(
                tree=tree,
                value=class_name,
                base_style="rounded rectangle"
            )
        
        # Add inheritance relationships
        for child, parents in self.inheritance.items():
            for parent in parents:
                if parent in nodes:  # Only if the parent is in our diagram
                    nodes[child].tree_parent = nodes[parent]
        
        # Add composition relationships as links
        for class_name, dependencies in self.composition.items():
            for dependency in dependencies:
                if dependency in nodes:  # Only if the dependency is in our diagram
                    # Add a link between the classes
                    link = drawpyo.diagram.Edge(
                        page=tree.page,
                        source=nodes[class_name],
                        target=nodes[dependency],
                        value="uses",
                    )
                    # Style the link differently from inheritance
                    link.apply_style_string("endArrow=open;dashed=1;")
        
        # Auto-layout the diagram
        tree.auto_layout()
        
        # Write the diagram to a file
        tree.write()
        
        return os.path.join(self.output_dir, file_name)
    
    def _analyze_module(self, module_name):
        """
        Analyze a module's classes and their relationships.
        
        Args:
            module_name: Name of the module to analyze
        """
        # Reset state
        self.inheritance = {}
        self.composition = {}
        self.all_classes = set()
        
        # Import the module
        module = importlib.import_module(module_name)
        
        # Get all classes from the module
        classes = self._get_classes_from_module(module)
        self.all_classes.update(classes.keys())
        
        # Analyze dependencies
        self._analyze_inheritance(classes)
        self._analyze_composition(classes)
    
    def _get_classes_from_module(self, module) -> Dict[str, Type]:
        """Extract all classes from a module."""
        classes = {}
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and obj.__module__ == module.__name__:
                classes[name] = obj
        return classes
    
    def _analyze_inheritance(self, classes):
        """Analyze inheritance relationships between classes."""
        for class_name, cls in classes.items():
            # Get base classes (excluding object)
            bases = [base.__name__ for base in cls.__bases__ if base.__name__ != 'object']
            if bases:
                self.inheritance[class_name] = bases
    
    def _analyze_composition(self, classes):
        """Analyze composition relationships between classes."""
        for class_name, cls in classes.items():
            self.composition[class_name] = []
            
            # Get the __init__ method
            init_method = cls.__init__
            
            # Skip if it's the default __init__
            if init_method.__module__ == '__builtin__':
                continue
            
            # Get the source code of the __init__ method
            try:
                source = inspect.getsource(init_method)
                
                # Look for attribute assignments with class instances
                for other_class_name in classes.keys():
                    # Skip self-references
                    if other_class_name == class_name:
                        continue
                    
                    # Check for patterns like self.attr = OtherClass()
                    if f"self.{other_class_name.lower()}" in source or \
                       f"self._{other_class_name.lower()}" in source or \
                       f" {other_class_name}(" in source:
                        self.composition[class_name].append(other_class_name)
            except (IOError, TypeError):
                # Can't get source code for some reason
                pass


def generate_class_diagram(module_name, output_dir=".", file_name=None, 
                          direction="down", link_style="orthogonal"):
    """
    Convenience function to generate a class diagram for a module.
    
    Args:
        module_name: Name of the module to analyze
        output_dir: Directory where the diagram will be saved
        file_name: Name of the output file (defaults to module_name + _diagram.drawio)
        direction: Direction of the tree (up, down, left, right)
        link_style: Style of links (orthogonal, straight, curved)
        
    Returns:
        Path to the generated diagram file
    """
    generator = ClassDiagramGenerator(output_dir)
    return generator.generate_diagram(
        module_name=module_name,
        file_name=file_name,
        direction=direction,
        link_style=link_style
    )


if __name__ == "__main__":
    # Example usage
    diagram_path = generate_class_diagram("model_classes")
    print(f"Diagram generated at: {diagram_path}")
