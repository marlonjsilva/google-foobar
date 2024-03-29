import unittest
import solution


class TestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 1, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 0, 0],
                    [1, 1, 1, 0],
                ]
            ),
            7,
        )

    def test_case_2(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0],
                ]
            ),
            11,
        )

    def test_case_3(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 0, 0, 1],
                    [1, 1, 1, 1],
                    [1, 1, 0, 1],
                    [1, 1, 0, 0],
                ]
            ),
            7,
        )

    def test_case_4(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 0, 0, 0],
                ]
            ),
            12,
        )

    def test_case_5(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 1],
                    [1, 1, 1, 0, 1],
                    [0, 0, 1, 0, 1],
                    [0, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0],
                ]
            ),
            17,
        )

    def test_case_6(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 1, 1, 0],
                    [0, 1, 1, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0],
                ]
            ),
            28,
        )

    def test_case_7(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 1, 1, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 1, 1, 0, 1],
                    [0, 1, 1, 0, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1, 1, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                ]
            ),
            16,
        )

    def test_case_8(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                ]
            ),
            151,
        )

    def test_case_0(self):
        self.assertEqual(
            solution.solution(
                [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]
            ),
            19,
        )


if __name__ == "__main__":
    unittest.main()
