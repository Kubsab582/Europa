from geopy import distance
cities = {
    "london": (51.510311052239075, -0.12822038593055046),
    "minsk": (53.924508796618085, 27.60176254136057)
}

distances = {}

for city in cities.keys():
    for target in cities.keys():
        distances.update({f"{city}>{target}": round(distance.distance(cities[city], cities[target]).miles, 1)})


if __name__ == "__main__":
    print(distances)
