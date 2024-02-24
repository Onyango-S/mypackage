def top_n(items, n):
    """
    Returns the top N items from the provided list in the descending order.

    Args:
        items (list): The input list.
        n (int): The number of top items to return.

    Returns:
        list: The top N items from the input list in the descending order.
    Example:
        >>> my_list = [10, 5, 8, 20, 3, 15]
        >>> top_items = top_n(my_list, 3)
        >>> print(top_items)
        [20, 15, 10]
    """
    # Sort the list in descending order
    sorted_items = sorted(items, reverse=True)

    # Return the top N items
    return sorted_items[:n]

# Example usage:
my_list = [10, 5, 8, 20, 3, 15]
top_items = top_n(my_list, 3)
print("Top 3 items:", top_items)
