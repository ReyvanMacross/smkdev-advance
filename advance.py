import itertools

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def calculate_total_distance(route, cities):
    total_distance = 0
    for i in range(len(route)):
        city1 = cities[route[i] - 1]
        city2 = cities[route[(i + 1) % len(route)] - 1]
        total_distance += calculate_distance(city1[0], city1[1], city2[0], city2[1])
    return total_distance

def find_optimal_route(N, cities):
    initial_route = list(range(1, N + 1))
    optimal_route = []
    min_distance = float('inf')

    for permuted_route in itertools.permutations(initial_route):
        current_distance = calculate_total_distance(permuted_route, cities)
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_route = list(permuted_route)

    return optimal_route, min_distance

# Input dari pengguna
N = int(input("Masukkan jumlah kota : "))
cities = []
for i in range(N):
    x, y = map(int, input(f"Masukkan koordinat kota ke-{i + 1} (format: x y): ").split())
    cities.append((x, y))

# Temukan rute optimal
optimal_route, min_distance = find_optimal_route(N, cities)

# Output hasil
print("Output:")
print("Optimal Route:", " -> ".join(f"City {city}" for city in optimal_route), "-> City 1")
print("Total Distance:", f"{min_distance:.1f} Units")
