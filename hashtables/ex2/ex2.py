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
    # Empty dictionary for caching
    cache = {}
    # Loop thru tickets in list of tickets
    for ticket in tickets:
        # Save ticket destinations to cache, using ticket source as index
        cache[ticket.source] = ticket.destination
    # Create an empty list to store routes
    route = []
    # Final destination has no next destination, so "NONE" is end of trip
    route.append(cache["NONE"])
    # Loop thru tickets in list of tickets again
    for ticket in tickets:
        # Set next_location to be the final route item 
        next_location = route[-1]
        # Append the next_location from cache
        route.append(cache[next_location])
        # If the final route item is "NONE"
        if route[-1] == "NONE":
            # The trip is over, so return the whole route list
            return route