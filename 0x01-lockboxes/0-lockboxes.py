def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])  # set of unlocked boxes
    keys = boxes[0]  # keys in the first box
    while keys:
        key = keys.pop()  # take a key from the list
        if key in unlocked:
            # the key opens a box that is already unlocked
            continue
        if key >= n:
            # the key is invalid (there is no box with that number)
            continue
        # unlock the box and add its keys to the list
        unlocked.add(key)
        keys.extend(boxes[key])
    # check if all boxes are unlocked
    return len(unlocked) == n
