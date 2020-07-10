def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Create empty lists to store positive and negative values separately
    pos = []
    neg = []
    # Likewise create a list of lists to manipulate the values in one object
    arrays = [pos, neg]
    # Finally, create an empty dictionary for caching counts
    cache = {}
    # Loop thru each item in the input array a
    for i in a:
        # If the item is positive
        if i > 0:
            # Append the item to the pos list
            pos.append(i)
        # If the item is negative
        elif i < 0:
            # Append the item's absolute value to the neg list
            neg.append(abs(i))
    # Loop thru each array in arrays (pos and neg)
    for a in arrays:
        # Loop thru each item in the array
        for i in a:
            # If the item is in the cache, add 1 to the count
            if i in cache:
                cache[i] += 1
            # Otherwise, the item is not yet cached
            else:
                # So set its value to 1
                cache[i] = 1
    # Use a list comprehension to get cache items with counts equal to 2 (positive and negative)
    result = [i for i in cache if cache[i]==len(arrays)]
    # Return list of items with positive and negative values in a
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
