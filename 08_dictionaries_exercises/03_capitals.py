countries, capitals = input().split(", "), input().split(", ")
capitals_dictionary = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in capitals_dictionary.items():
    print(f"{country} -> {capital}")
