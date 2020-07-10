def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Empty dictionary for caching
    cache = {}
    # Loop thru each array in arrays
    for a in arrays:
        # Loop thru each item in the array
        for i in a:
            # Check if each item is in the cache
            if i in cache:
                # If the item is already in the cache, add 1 to the counter for that item
                cache[i] += 1
            else:
                # Otherwise, set the counter to 1 for that item
                cache[i] = 1
    # Use a list comprehension to get items whose count equals the number of arrays input to the function
    results = [i for i in cache if cache[i]==len(arrays)]
    # Return intersecting items
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
