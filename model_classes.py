"""
Simple model classes with dependencies for diagram generation.
This module demonstrates how to create class diagrams from related instances.
"""


class Animal:
    """Base class for all animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        """Make a generic animal sound."""
        return "..."

    def describe(self):
        """Return a description of the animal."""
        return f"{self.name}, {self.age} years old"


class Dog(Animal):
    """A dog is a type of animal."""

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        """Dogs bark."""
        return "Woof!"

    def fetch(self, item):
        """Dogs can fetch items."""
        return f"{self.name} fetched the {item}!"


class Cat(Animal):
    """A cat is a type of animal."""

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        """Cats meow."""
        return "Meow!"

    def purr(self):
        """Cats can purr."""
        return f"{self.name} is purring..."


class Owner:
    """A person who owns pets."""

    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        """Add a pet to the owner's collection."""
        self.pets.append(pet)
        return f"{self.name} now owns {pet.name}"

    def list_pets(self):
        """List all pets owned by this person."""
        if not self.pets:
            return f"{self.name} has no pets"

        pet_names = [pet.name for pet in self.pets]
        return f"{self.name} owns: {', '.join(pet_names)}"


class Veterinarian:
    """A doctor who treats animals."""

    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.patients = []

    def treat(self, animal):
        """Treat an animal patient."""
        if animal not in self.patients:
            self.patients.append(animal)
        return f"Dr. {self.name} treated {animal.name}"

    def get_patient_count(self):
        """Get the number of patients."""
        return len(self.patients)


class PetShop:
    """A shop that sells pets and supplies."""

    def __init__(self, name):
        self.name = name
        self.animals_for_sale = []
        self.veterinarian = None

    def add_animal(self, animal):
        """Add an animal to the shop's inventory."""
        self.animals_for_sale.append(animal)

    def hire_veterinarian(self, vet):
        """Hire a veterinarian for the pet shop."""
        self.veterinarian = vet
        return f"{vet.name} now works at {self.name}"

    def sell_pet(self, animal, owner):
        """Sell a pet to an owner."""
        if animal in self.animals_for_sale:
            self.animals_for_sale.remove(animal)
            owner.add_pet(animal)
            return f"{owner.name} bought {animal.name} from {self.name}"
        return f"{animal.name} is not available for sale"
