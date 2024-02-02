import random

def hill_climbing(f, x0):
	x = x0 # initial solution
	while True:
		neighbors = generate_neighbors(x) # generate neighbors of x
		# find the neighbor with the highest function value
		best_neighbor = max(neighbors, key=f)
		if f(best_neighbor) <= f(x): # if the best neighbor is not better than x, stop
			return x
		x = best_neighbor # otherwise, continue with the best neighbor


def generate_neighbors(x):
    # generate 100 neighbors of x by adding or subtracting 0.001 to each dimension
    neighbors = []
    for i in range(100):
        neighbor = []
        for xi in x:
            neighbor.append(xi + random.uniform(-0.001, 0.001))
        neighbors.append(neighbor)
    return neighbors


def f(x):
    return sum(xi**2 for xi in x)


if __name__ == '__main__':
    x0 = [random.uniform(-1, 1) for i in range(10)]
    x = hill_climbing(f, x0)
    print(x, f(x))