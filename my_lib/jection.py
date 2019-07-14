import random


def inject(person1, person2):
    """
    len(person1.boxes) <= len(person2.boxes)
    """

    # Delete an empty box.
    boxes1 = [x for x in person1.boxes if x]

    if len(person2.boxes) < len(boxes1):
        print("Fail    : Person1 {}, Person2 {}.".format(
            len(boxes1), len(person2.boxes)))
        return

    destinations = list(range(len(person2.boxes)))
    random.shuffle(destinations)

    for i in range(0, len(boxes1)):
        person2.boxes[destinations[i]].extend(boxes1[i])


def surject(person1, person2):
    """
    len(person1.boxes) >= len(person2.boxes)
    """

    if len(person1.boxes) < len(person2.boxes):
        print("Fail    : I can not be satisfied. Src {}, Dst {}.".format(
            len(person1.boxes), len(person2.boxes)))
        return

    destinations = []
    for i in range(0, len(person1.boxes)):
        destinations.append(i % len(person2.boxes))

    random.shuffle(destinations)

    for i in range(0, len(person1.boxes)):
        person2.boxes[destinations[i]].extend(person1.boxes[i])

    return
