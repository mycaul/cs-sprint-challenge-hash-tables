#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    #create fixed length for route
    route = [None] * length

    for i in range(length):
        current = tickets[i]
        cache[current.source] = current.destination
    route[0] = cache["NONE"]
    route[1] = cache[route[0]]

    for i in range(2, length):
        route[i] = cache[route[i - 1]]

    return route
    