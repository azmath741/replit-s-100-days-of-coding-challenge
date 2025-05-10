# let's come up with a recipe generator to build us an amazing dish for today's evening meal!
# You will need to:
# 1.Create these as a variable:
#   A type of food
#   A type of plant
#   A method of cooking
#   A word to describe burned food
#   A household item
# 2. Output a nice looking Recipe page that *concatenates* a dish in this format:
# cooking food with burned plant on a bed of item
food_type=input("Enter food type: ")
plant_name=input("type of plant:")
method=input("A method of cooking:")
describe=input("describe the food:")
item=input("item:")
print("I love! ",food_type," It is a ",describe," dish that contains ","item.")
print("The key to a perfect", food_type," is", method)
