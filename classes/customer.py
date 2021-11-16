class Customer:
    def __init__(self, name, cash):
        # Instance variables / properties
        self.name = name
        self.cash = cash
        # Add list of pets to the customer
        self.pets = []

    def reduce_cash(self, amount):
        self.cash -= amount

    def pet_count(self):
        # Return the length of the list
        return len(self.pets)

    def add_pet(self, pet):
        self.pets.append(pet)

    def get_total_value_of_pets(self):
        total = 0
        # loop through the list
        for pet in self.pets:
            # We get pet price from Pet class self.price
            # .price is a property on the pet
            total += pet.price
        return total