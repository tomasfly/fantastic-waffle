# test_data/fibonacci_sequence_data.py

# Test data for Fibonacci Sequence implementation

# Test cases for generating Fibonacci sequence
fibonacci_test_cases = [
    # Test case 1: n = 0
    {
        'n': 0,
        'expected_sequence': []
    },
    # Test case 2: n = 1
    {
        'n': 1,
        'expected_sequence': [0]
    },
    # Test case 3: n = 5
    {
        'n': 5,
        'expected_sequence': [0, 1, 1, 2, 3]
    },
    # Test case 4: n = 10
    {
        'n': 10,
        'expected_sequence': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    },
    # Test case 5: n = 15
    {
        'n': 15,
        'expected_sequence': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    }
]