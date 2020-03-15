def tower_builder(n_floors):
    tower = []
    for i in range(n_floors + 1):
        floor = '*' * (i+i-1)
        padding = int(n_floors-(i+i-1)/2) * ' '
        tower.append(padding + floor + padding)
    return tower[1:]


print(tower_builder(5))