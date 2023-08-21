import sys
print(sys.platform)
print(2 ** 100)
x = 'Spam!'
print(x * 8)
# Load a library module
# Raise 2 to a power
# String repetition
def get_user(username):
    print(f'Hello,{username.title()} !')
get_user('charya')

def describe_pet(animal_type, pet_name):
#"""Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')