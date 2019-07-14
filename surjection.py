from my_lib.person import Person
from my_lib.jection import surject

# There are 5 peoples. Pitcher have six boxes.
pitcher = Person("Pitcher", [[2], [3], [5], [7], [11], [13]])
first = Person("First", [[], [], [], [], []])
second = Person("Second", [[], [], [], []])
third = Person("Third", [[], [], []])
catcher = Person("Catcher", [[], []])


# Go!
print("radio> Starting line up.")
pitcher.show()
first.show()
second.show()
third.show()
catcher.show()

print("radio> The pitcher threw the ball towards first.")
first.clear_boxes()
surject(pitcher, first)
first.show()

print("radio> The first threw the ball towards second.")
second.clear_boxes()
surject(first, second)
second.show()

print("radio> The second threw the ball towards third.")
third.clear_boxes()
surject(second, third)
third.show()

print("radio> The third threw the ball towards catcher.")
catcher.clear_boxes()
surject(third, catcher)
catcher.show()

print("Info    : Finished")
