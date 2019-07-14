from my_lib.person import Person
from my_lib.jection import inject

# There are 5 peoples. Pitcher have six boxes.
pitcher = Person("Pitcher", [[2], [3], [5], [7], [11], [13]])
first = Person("First", [[], [], [], [], [], [], []])
second = Person("Second", [[], [], [], [], [], [], [], []])
third = Person("Third", [[], [], [], [], [], [], [], [], []])
catcher = Person("Catcher", [[], [], [], [], [], [], [], [], [], []])

# Go!
print("radio> Starting line up.")
pitcher.show()
first.show()
second.show()
third.show()
catcher.show()

print("radio> The pitcher threw the ball towards first.")
first.clear_boxes()
inject(pitcher, first)
first.show()

print("radio> First returned the ball to the pitcher.")
pitcher.clear_boxes()
inject(first, pitcher)
pitcher.show()

print("radio> The pitcher threw the ball towards second.")
second.clear_boxes()
inject(pitcher, second)
second.show()

print("radio> Second returned the ball to the pitcher.")
pitcher.clear_boxes()
inject(second, pitcher)
pitcher.show()

print("radio> The pitcher threw the ball towards third.")
third.clear_boxes()
inject(pitcher, third)
third.show()

print("radio> Third returned the ball to the pitcher.")
pitcher.clear_boxes()
inject(third, pitcher)
pitcher.show()

print("radio> The pitcher threw the ball towards catcher.")
catcher.clear_boxes()
inject(pitcher, catcher)
catcher.show()

print("radio> Catcher returned the ball to the pitcher.")
pitcher.clear_boxes()
inject(catcher, pitcher)
pitcher.show()

print("Info    : Finished")
