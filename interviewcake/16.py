

def max_duffel_bag_value(cake_tuples, capacity):
    """ takes a list of cake type tuples and a weight capacity, and
    returns the maximum monetary value the duffle bag can hold."""
    max_values_at_capacities = [0] * (capacity + 1)

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

print(max_duffel_bag_value(cake_tuples, capacity))

