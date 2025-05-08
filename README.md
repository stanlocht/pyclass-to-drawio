# Python Class and Instance Diagram Generator

This project demonstrates how to generate draw.io diagrams from Python classes and instances. It provides a simple way to visualize class relationships and instance dependencies.

## Overview

The repository contains:

1. **Simple model classes** - A set of related classes (Animal, Dog, Cat, Owner, etc.)
2. **Class diagram generator** - Creates diagrams showing class inheritance and composition
3. **Instance diagram generator** - Creates diagrams showing relationships between instances

## Requirements

- Python 3.8+
- drawpyo library

## Installation

1. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install drawpyo
   ```

## Usage

### Generating Class Diagrams

To generate a diagram showing class relationships:

```python
from class_diagram_generator import generate_class_diagram

# Generate a diagram for a module
diagram_path = generate_class_diagram(
    module_name="your_module_name",
    output_dir="output_directory",  # Optional
    file_name="diagram_name.drawio",  # Optional
    direction="down",  # Optional: "up", "down", "left", "right"
    link_style="orthogonal"  # Optional: "orthogonal", "straight", "curved"
)
```

Or simply run:

```
python generate_diagram.py
```

This will create a diagram of the classes in `model_classes.py`.

### Generating Instance Diagrams

To generate a diagram showing relationships between instances:

```python
from instance_diagram import create_instance_diagram

# Create an instance diagram
diagram_path = create_instance_diagram(
    output_dir="output_directory",  # Optional
    file_name="instances_diagram.drawio"  # Optional
)
```

Or simply run:

```
python instance_diagram.py
```

## Example Files

- `model_classes.py` - Contains simple classes with inheritance and composition relationships
- `class_diagram_generator.py` - Contains the code to analyze classes and generate diagrams
- `generate_diagram.py` - Script to generate a class diagram
- `instance_diagram.py` - Script to generate an instance diagram

## How It Works

1. **Class Diagram Generation**:
   - Uses Python's `inspect` module to analyze class relationships
   - Detects inheritance by examining class bases
   - Detects composition by analyzing `__init__` methods
   - Creates a diagram using drawpyo's TreeDiagram

2. **Instance Diagram Generation**:
   - Manually creates instances and establishes relationships
   - Creates nodes for each instance
   - Adds relationships between instances
   - Applies styling to differentiate types of instances

## Viewing Diagrams

The generated `.drawio` files can be opened with:
- [draw.io](https://app.diagrams.net/) website
- draw.io desktop application
- VS Code with the draw.io extension

## License

This project is open source and available under the MIT License.
