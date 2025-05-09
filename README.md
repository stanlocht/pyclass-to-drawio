# Python Class and Instance Diagram Generator

This project demonstrates how to generate draw.io diagrams from Python classes and instances. It provides a simple way to visualize class relationships and instance dependencies.

## Overview

The repository contains:

1. **Simple model classes** - A set of related classes (Animal, Dog, Cat, Owner, etc.)
2. **Class diagram generator** - Creates diagrams showing class inheritance and composition
3. **Instance diagram generator** - Creates diagrams showing relationships between instances

## Example Diagrams

### Class Diagram

When you run `generate_diagram.py`, it analyzes the classes in `model_classes.py` and generates a diagram like this:

```
                  ┌─────────┐
                  │ Animal  │
                  └────┬────┘
                       │
          ┌────────────┴────────────┐
          │                         │
    ┌─────┴─────┐             ┌─────┴─────┐
    │    Dog    │             │    Cat    │
    └───────────┘             └───────────┘
                                    ▲
                                    │ uses
                                    │
┌──────────┐  uses  ┌──────────┐   │
│  Owner   │◀───────│ PetShop  │   │
└──────────┘        └──────────┘   │
      ▲                  │         │
      │                  │ uses    │
      │                  ▼         │
      │ uses      ┌──────────────┐ │
      └───────────│ Veterinarian │◀┘
                  └──────────────┘
```

### Instance Diagram

When you run `instance_diagram.py`, it creates instances of these classes and generates a diagram showing their relationships:

```
                ┌───────────────┐
                │ Pet Palace    │
                │ (Shop)        │
                └───────┬───────┘
                        │
                        │
                ┌───────▼───────┐
                │ Dr. Smith     │
                │ (Vet)         │
                └─┬─────────┬───┘
                  │         │
          treats  │         │  treats
                  │         │
        ┌─────────▼─┐     ┌─▼──────────┐
        │ Fido      │     │ Whiskers   │
        │ (Dog)     │     │ (Cat)      │
        └─────────▲─┘     └────────────┘
                  │              ▲
                  │              │
          ┌───────┴───┐   ┌──────┴─────┐
          │ John      │   │ Sarah      │◀─────┐
          │ (Owner)   │   │ (Owner)    │      │
          └───────────┘   └────────────┘      │
                                              │
                                      ┌───────┴────┐
                                      │ Mittens    │
                                      │ (Cat)      │
                                      └────────────┘
```

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

### Model Classes

Here's a simplified view of the classes in `model_classes.py`:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

class Veterinarian:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients = []

    def treat(self, animal):
        self.patients.append(animal)

class PetShop:
    def __init__(self, name):
        self.name = name
        self.animals_for_sale = []
        self.veterinarian = None

    def hire_veterinarian(self, vet):
        self.veterinarian = vet
```

### Instance Creation

Here's how instances are created in `instance_diagram.py`:

```python
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
```

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

## Viewing and Converting Diagrams

The generated `.drawio` files can be opened with:
- [draw.io](https://app.diagrams.net/) website
- draw.io desktop application
- VS Code with the draw.io extension

### Converting to SVG

To convert the `.drawio` files to SVG for embedding in documentation:

1. Open the `.drawio` file in VS Code with the draw.io extension
2. Use the "Draw.io: Convert To..." command
3. Select "SVG" as the target format
4. The resulting `.drawio.svg` file can be directly viewed in GitHub and other SVG-compatible viewers

### Class Diagram
![Class Diagram](pet_classes_diagram.drawio.svg)

### Instance Diagram
![Instance Diagram](pet_instances_diagram.drawio.svg)

Note: The actual appearance may vary slightly depending on the draw.io version and layout algorithm. The ASCII diagrams above are simplified representations of what you'll see in the diagrams.

## License

This project is open source and available under the MIT License.
