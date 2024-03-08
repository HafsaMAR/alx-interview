#!/usr/bin/python3


def pascal_triangle(n):
    # expect error value
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of rows must be a positive integer")
    # use recursion to solve the triangle
    if n == 1:
        return [[1]]
    else:
        prev_triangle = pascal_triangle(n - 1)
        prev_row = prev_triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1]
                         for i in range(len(prev_row) - 1)] + [1]
        return prev_triangle + [new_row]


# class Testpascal_triangle(unittest.TestCase):
#     def test_boundary_cases(self):
#         self.assertEqual(pascal_triangle(1), [[1]])

#     def test_valid_inputs(self):
#         self.assertEqual(pascal_triangle(5), [
#             [1],
#             [1, 1],
#             [1, 2, 1],
#             [1, 3, 3, 1],
#             [1, 4, 6, 4, 1]
#         ])


#     def test_invalid_inputs_raised_errors(self):
#         with self.assertRaises(ValueError) as context:
#             pascal_triangle(-5)
        # self.assertEqual(str(context.exception),
        #                  "Number of rows must be a positive integer")


# if __name__ == '__main__':
#     unittest.main()
