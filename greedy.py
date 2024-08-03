#Coin Changing
# def indian_coin_change(amount, denominations):
#     # Sort the denominations in descending order
#     denominations.sort(reverse=True)
    
#     result = []
#     count = 0
    
#     for coin in denominations:
#         if amount == 0:
#             break
#         if coin <= amount:
#             num_coins = amount // coin
#             amount -= num_coins * coin
#             count += num_coins
#             result.extend([coin] * num_coins)
    
#     return count, result

# # Example usage
# amount = 93
# denominations = [1, 2, 5, 10, 20, 50, 100, 2000]

# count, coins_used = indian_coin_change(amount, denominations)
# print(f"Minimum number of coins needed: {count}")
# print(f"Coins used: {coins_used}")

#Activity Selection
# def activity_selection(start_times, end_times):
#     # Combine start and end times into a list of tuples and sort by end times
#     activities = sorted(zip(start_times, end_times), key=lambda x: x[1])
    
#     selected_activities = []
#     last_end_time = 0
    
#     for start, end in activities:
#         if start >= last_end_time:
#             selected_activities.append((start, end))
#             last_end_time = end
            
#     return selected_activities

# # Example usage
# start_times = [1, 3, 0, 5, 8, 5]
# end_times = [2, 4, 6, 7, 9, 9]

# selected_activities = activity_selection(start_times, end_times)
# print(f"Selected activities: {selected_activities}")

#Frac Knap
# def fractional_knapsack(capacity, values, weights):
#     # Calculate value per weight for each item
#     value_per_weight = [v / w for v, w in zip(values, weights)]
    
#     # Create a list of items with (value, weight, value_per_weight)
#     items = list(zip(values, weights, value_per_weight))
    
#     # Sort items by value per weight in descending order
#     items.sort(key=lambda item: item[2], reverse=True)
    
#     total_value = 0
    
#     for value, weight, vpw in items:
#         if capacity == 0:
#             break
        
#         # Determine how much of the item we can take
#         take_weight = min(weight, capacity)
#         total_value += take_weight * vpw
#         capacity -= take_weight
    
#     return total_value

# # Example usage
# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50

# max_value = fractional_knapsack(capacity, values, weights)
# print(f"Maximum value in Knapsack = {max_value}")

#Optimal pattern merge
# import heapq

# def optimal_pattern_merge(patterns):
#     # Create a min-heap from the patterns
#     heapq.heapify(patterns)
    
#     total_cost = 0
    
#     while len(patterns) > 1:
#         # Extract the two smallest patterns
#         first = heapq.heappop(patterns)
#         second = heapq.heappop(patterns)
        
#         # Merge them
#         merge_cost = first + second
#         total_cost += merge_cost
        
#         # Add the merged pattern back to the heap
#         heapq.heappush(patterns, merge_cost)
    
#     return total_cost

# # Example usage
# patterns = [4, 3, 2, 6]

# total_cost = optimal_pattern_merge(patterns)
# print(f"Total cost of merging patterns: {total_cost}")

#Maximum and Minimum Difference - Greedy Algorithm
# arr = [12, -3, 10, 0]
# arr.sort()
# max_diff, min_diff = 0, 0
# n = len(arr)
# for i in range(n//2):
#     max_diff += (arr[i+n//2] - arr[i])
#     min_diff += (arr[2*i+1] - arr[2*i])

# print(f"Maximum difference between sums: {max_diff}")
# print(f"Minimum difference between sums: {min_diff}")

#Expedition
# import heapq

# def min_stops_to_reach_town(fuel_stops, distances, initial_fuel):
#     n = len(fuel_stops)
#     max_heap = []
#     stops = 0
#     current_fuel = initial_fuel
#     current_position = 0
#     index = 0

#     while current_position < len(distances):
#         # While we haven't reached the next stop and we have fuel stops left to consider
#         while index < n and current_position < len(distances) and current_fuel < distances[current_position]:
#             # Add the fuel capacity at the current stop to the max heap
#             heapq.heappush(max_heap, -fuel_stops[index])
#             index += 1

#         # If we can't reach the next stop and there are no more fuel stops to consider
#         if current_fuel < distances[current_position] and not max_heap:
#             return -1

#         # Refuel at the stop with the maximum fuel capacity if needed
#         while current_position < len(distances) and current_fuel < distances[current_position] and max_heap:
#             current_fuel += -heapq.heappop(max_heap)
#             stops += 1
        
#         # Move to the next stop
#         if current_position < len(distances):
#             current_fuel -= distances[current_position]
#             current_position += 1

#     return stops

# # Example usage
# fuel_stops = [50, 30, 20, 40, 10]  # Fuel capacities at each stop
# distances = [30, 40, 50, 20]       # Distances between stops
# initial_fuel = 10                  # Initial fuel in the tank

# print("Minimum number of stops required:", min_stops_to_reach_town(fuel_stops, distances, initial_fuel))
