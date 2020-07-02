def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    if len(items) == 0 or capacity == 0:
        return 0
    
    value_without = knapsack(items[1:], capacity)

    if capacity < items[0][1]:
        return value_without
    
    value_with = items[0][2] + knapsack(items[1:], capacity - items[0][1])
    
    return max(value_with, value_without)
  
if __name__ == "__main__":
    items = [ ('boots', 10, 60), ('tent', 20, 100), ('water', 30, 120), ('first aid', 15, 70) ]
    capacity = 50
    print(knapsack(items, capacity))