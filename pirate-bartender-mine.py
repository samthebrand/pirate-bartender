import random

questions = {
    "strong": "Do ye like yer drinks mega mucho strong?",
    "salty": "Do ye like it with a super duper salty tang?",
    "bitter": "Are ye a lubber who likes it bitey bitter ouchie wowie?",
    "sweet": "Would ye like a bit of drippy droopy sweetness with yer poison?",
    "fruity": "Are ye one for a fruity tootie fresh and bootylicious finish?"
}
 
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def get_choices():
	choices = {}
	for flavor, question in questions.iteritems():
		print question
		choices[flavor] = raw_input().lower() in ["y","yes"]
		print ""
	return choices

def serve_drink(choices):
	drink = []
	for ingredient_type, liked in choices.iteritems():
		if not liked:
			continue

		drink.append(random.choice(ingredients[ingredient_type]))
	return drink

def main():
	choices = get_choices()
	drink = serve_drink(choices)
	print "Here's your drink buddy boy!"
	print "This is the recipe:"
	for ingredient in drink:
		print "A {}".format(ingredient)

if __name__ == "__main__":
	main()