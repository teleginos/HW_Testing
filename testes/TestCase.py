import unittest
from HumanMoveTest.main import Student


class TestStudent(unittest.TestCase):
    def test_walk_distance(self):
        student = Student('Student1')
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, f"Дистанции не равны {student.distance} != 500")

    def test_run_distance(self):
        student = Student('Student1')
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, f"Дистанции не равны {student.distance} != 1000")

    def test_competition(self):
        student1 = Student('Student_runer')
        student2 = Student('Student_walker')

        for _ in range(10):
            student1.run()
            student2.walk()
        self.assertLess(student1.distance, student2.distance, f"{student1} должен преодолеть дистанцию "
                                                              f"больше, чем {student2}")


if __name__ == "__main__":
    unittest.main()
