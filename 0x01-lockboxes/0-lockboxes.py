#!/usr/bin/python3
""" model for Lockboxes """


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): list of lists
            representing boxes and keys.

    Returns:
        bool: True if all boxes can be opened,
            False otherwise.
    """
    # Create a set to keep track of visited boxes
    visited = set()

    # Initialize a stack with the keys from the first box
    stack = boxes[0][:]

    # Mark the first box as visited
    visited.add(0)

    # Perform depth-first search (DFS)
    while stack:
        key = stack.pop()
        # If the key opens a new box and that box has not
        # been visited yet
        if key < len(boxes) and key not in visited:
            # Mark the box as visited
            visited.add(key)
            # Add the keys from the newly opened box to
            # the stack
            stack.extend(boxes[key])

    # If all boxes have been visited, return True
    return len(visited) == len(boxes)
