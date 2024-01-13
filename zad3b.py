import unittest

# Kod sortowania bąbelkowego
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.N = 10
        self.numbers = [4, 2, 7, 1, 9, 3, 5, 8, 6, 10]
        self.sorted_numbers = sorted(self.numbers)
        self.sorted_numbers[2], self.sorted_numbers[5] = self.sorted_numbers[5], self.sorted_numbers[2]
        self.numbers_bubble_sort = self.numbers.copy()

    def test_bubble_sort_sorted(self):
        bubble_sort(self.numbers_bubble_sort)
        self.assertEqual(self.numbers_bubble_sort, self.sorted_numbers)

    def test_bubble_sort_empty(self):
        empty_list = []
        bubble_sort(empty_list)
        self.assertEqual(empty_list, [])

    def test_bubble_sort_single_element(self):
        single_element_list = [42]
        bubble_sort(single_element_list)
        self.assertEqual(single_element_list, [42])


if __name__ == '__main__':
    unittest.main()
