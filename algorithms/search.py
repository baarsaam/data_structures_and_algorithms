def binary_search(array, query) -> int:
    """
    This function implements the binary search algorithm given a sorted container of values. The values must be numbers
    (i.e., int or float).
    :param array: The array of values to be searched.
    :param query: The value to be queried from the array.
    :return: An integer value indicating the index of the query in the array. Return -1 if not found.
    """

    # Detecting the order of the array.
    descending = True if array[-1] < array[0] else False

    # Holding the end and start index of the array
    start_interval = 0
    end_interval = len(array)

    # If the aray is in descending order
    if descending:
        # Search
        while True:
            # Finding the middle index. If middle index is a float, 1 unit is added to it
            mid_point = int((start_interval + end_interval) / 2) + ((start_interval + end_interval) % 2)

            # If the middle point is equal to query
            if array[mid_point] == query:
                # Counting back from the found index to find the first instance of the query
                while array[mid_point - 1] == query:
                    mid_point -= 1
                return mid_point
            # If the middle point is greater than the query (query to the right of middle point), update the start.
            elif array[mid_point] > query:
                start_interval = mid_point
            # If the middle point is less than the query (query to the left of middle point), update the end.
            else:
                end_interval = mid_point
    else:
        pass
