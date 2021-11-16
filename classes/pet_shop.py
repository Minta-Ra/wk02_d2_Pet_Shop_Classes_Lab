class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        # To fulfill test_pet_shop_pets_sold_starts_at_0 from pet_shop_test.py
        # It is property
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def remove_pet(self, pet):
        # I am passing a pet object that is pet_1
        # self.pets happens in __init__
        self.pets.remove(pet)

    def find_pet_by_name(self, pet_name):
        for pet in self.pets:
            if pet.name == pet_name:
                return pet


    # Integration
    def sell_pet_to_customer(self, pet_name, customer):
        # Find pet bt name using pet_name and find_pet_by_name
        # Reduce cash by that pet's price
        pet = self.find_pet_by_name(pet_name)
        # Customer cash got decreased
        # customer.py has a function reduce_cash
        customer.reduce_cash(pet.price)
        # Update pet_stop.total_cash
        self.increase_total_cash(pet.price)
        # Update pet_stop.pets_sold
        self.increase_pets_sold()
        # Update self.pet_shop.stock_count() - Remove pet
        self.remove_pet(pet)
        # Update customer.pet_count() - Add pet to customer
        customer.add_pet(pet)

