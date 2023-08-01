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
    if not any(isinstance(box, list) for box in boxes):
        return False
    if len(boxes) == 1:
        return True
    opened_boxes = [0]
    available_keys = boxes[0].copy()
    while available_keys:
        key = available_keys.pop()
        if key in opened_boxes:
            continue
        if key < len(boxes):
            opened_boxes.append(key)
            available_keys.extend(boxes[key])
    return len(opened_boxes) == len(boxes)
