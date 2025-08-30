from geopy import distance
from geopy.geocoders import get_geocoder_for_service
import json

query_cities = ["london", "minsk", "moscow", "warsaw"]
cities_cache = {}
fr = open("distances_cache.JSON", "r")
json_parsed = json.loads(fr.read())
print(json_parsed)


def check_cache():
    counter = 0
    already_cached_index = []

    for city in query_cities:
        if city in json_parsed:
            already_cached_index.append(query_cities.index(city)-counter)
            counter += 1
            print(f"{city} present")
    return already_cached_index


already_cached_index = check_cache()
for index in already_cached_index:
    del query_cities[index]


def geocode(geocoder, config, query):
    cls = get_geocoder_for_service(geocoder)
    geolocator = cls(**config)
    location = geolocator.geocode(query)
    return (location.latitude, location.longitude)


for city in query_cities:
    cities_cache.update(
            {f"{city}": geocode("nominatim",
                                dict(user_agent="Mozilla/5.0 (X11; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0"),
                                city)
             }
            )

json_parsed.update(cities_cache)
print(json_parsed)
# If there is nothing in distances_cache.JSON initialize
fw = open("distances_cache.JSON", "w")
fw.write(json.dumps(json_parsed))

distances = {}

for city in json_parsed.keys():
    for target in json_parsed.keys():
        if city != target:
            distances.update({f"{city}>{target}": round(distance.distance(json_parsed[city], json_parsed[target]).miles, 1)})

print(distances)
