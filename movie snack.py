# cook your dish here
X, Y, Z = map(int, input().split())
cost_individual = (2 * X) + (3 * Y)  
cost_combo = (2 * Z) + Y            
min_cost = min(cost_individual, cost_combo)
print(min_cost)
