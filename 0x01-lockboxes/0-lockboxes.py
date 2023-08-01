#!/usr/bin/python3
"""Lockboxes module."""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    args:
        boxes(list): list containing lists representing a box

    Returns:
        True if all boxes can be opened, false otherwise

    """
    if len(boxes) == 1:
        return True
    if not all(isinstance(box, list) for box in boxes):
        return False
    is_open = []
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            for k in range(1, len(boxes)):
                if i == k:
                    continue
                else:
                    if boxes[i][j] == k:
                        is_open.append("{} is_opened".format(k))
    unique_list = []
    [unique_list.append(item) for item in is_open if item not in unique_list]
    return True if len(unique_list) == (len(boxes) - 1) else False
