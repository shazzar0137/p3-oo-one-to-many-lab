class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = [] 

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  
        if owner:
            self.set_owner(owner) 
        Pet.all.append(self) 

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self.owner = owner
        owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name 
        self._pets = [] 

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        pet.owner = self 
        self._pets.append(pet) 


    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)