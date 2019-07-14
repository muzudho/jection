class Person(object):
    def __init__(self, name, boxes):
        self._name = name
        self._boxes = boxes
        return

    @property
    def name(self):
        return self._name

    @property
    def boxes(self):
        return self._boxes

    def clear_boxes(self):
        for box in self._boxes:
            box.clear()

    def show(self):
        print("{:<8}: ".format(self._name), end="")

        for box in self._boxes:
            print("[", end="")
            first = True
            for ball in box:
                if not first:
                    print(", ", end="")
                else:
                    first = False
                print("{:>2}".format(ball), end="")
            print("]", end="")
        print("")
