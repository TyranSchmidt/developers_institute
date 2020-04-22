keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

for item in zip(keys, values):
	print(item)

# exercise 2

store = {
	"name": "Zara",
	"creation_date": 1975,
	"creator_name": "Amancio Ortega Gaona",
	"type_of_clothes": ["men", "women", "children", "home"],
	"international_competitors": ["Gap", "H&M", "Benetton"], 
	"number_stores": 7000, 
	"major_color":{
	"France": "blue",
	"Spain": "red",
	"US":"pink and green", 
	}
}


store["number_stores"] = 2

print("Zara's clients are everyone")
store["country_creation"] = "Spain"
if "international_competitors" in store:
	store["international_competitors"].append("Desigual")
	print(store)

del store["creation_date"]

print(store["international_competitors"][-1])

print("The major colors of the US are {US}".format(**store["major_color"]))

print(len(store))
print(store.keys())

more_on_store = {
	"creation_date": 1975,
	"number_stores": 10000,
}

for stuff in more_on_store:
		store[stuff] = more_on_store[stuff]

print(store["number_stores"])