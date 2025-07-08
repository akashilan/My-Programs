def find(cities, visited, source, destination):
	if destination in cities[source]:
		return True
	else:
		for city in cities[source]:
			if city not in visited:
				visited.append(city)
				is_found = find(cities, visited, city, destination)
				return True if is_found == True else False

def is_reachable(cities, source, destination):
	if source not in cities or destination not in cities:
		return False
	if source in cities:
		visited = [source]
	if source == destination:
		return True
	return find(cities, visited, source, destination)

cities = {'a': ['b', 'c', 'd'], 'b':['a'], 'c':['a', 'f'], 'd': ['a'], 'f': ['c', 'e'], 'e': ['f']}
print(is_reachable(cities, 'b', 'e'))
