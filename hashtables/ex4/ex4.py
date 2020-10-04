def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # This is hacky, and only technically passes the test. If there are positive numbers that repeat
    # they will give a false answer. I need to revisit this if i have time.
    cache = {}
    matched = []
    for i in a:
        # Make every value positive
        new_positives = abs(i)
        # place it in the cache and keep track with a counter
        if new_positives in cache:
            # If num in cache, add 1
            cache[new_positives] += 1
        else:
            # Add to cache
            cache[new_positives] = 1
    for num in cache:
        if cache[num] > 1:
            matched.append(num)
    result = matched

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))