def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Empty dictionary for caching
    cache = {}
    # Loop thru each item in list of weights
    for i in range(length):
        # Find complement for each item weight with respect to limit
        target_weight = limit - weights[i]
        # Check if target_weight is in cache
        if target_weight in cache:
            # If yes, select the target_weight from cache
            s = cache[target_weight]
            # Create new list for each item and cached weight
            new_list = [i, s]
            # Sort the list in reverse ascending order
            new_list.sort(reverse = True)
            # Return the sorted list
            return new_list
        # If target_weight is not in cache
        else:
            # Save the weight in cache with value i
            cache[weights[i]] = i
    return None