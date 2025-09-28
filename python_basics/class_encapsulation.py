class Student:
    def __init__(self, name, grade):
        self.name = name  # Public attribute
        self._grade = grade  # Protected attribute (by convention)
        self.__scholarship = False  # Private attribute (name mangling)

    # Public method
    def display_info(self):
        print(f"Name: {self.name}, Grade: {self._grade}")

    # Protected method (just a convention)
    def _is_passing(self):
        return self._grade >= 75

    # Private method
    def __check_scholarship(self):
        if self._grade > 90:
            self.__scholarship = True

    # Public method to safely access private details
    def check_eligibility(self):
        self.__check_scholarship()
        return self.__scholarship


# ---------------------------
# Usage
student = Student("Alice", 92)

# ✅ Public: freely accessible
print(student.name)  # Alice
student.display_info()  # Name: Alice, Grade: 92

# ⚠️ Protected: should not be accessed directly, but possible
print(student._grade)  # 92
print(student._is_passing())  # True

# ❌ Private: not directly accessible
# print(student.__scholarship)       # AttributeError
# print(student.__check_scholarship())  # AttributeError

# ✅ Correct way: use a public method to access private data
print(student.check_eligibility())  # True
