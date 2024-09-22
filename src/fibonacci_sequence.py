# fibonacci_sequence.py

def generate_fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to the given number of terms.
    
    Args:
        n (int): The number of terms in the Fibonacci sequence.
    
    Returns:
        list: The Fibonacci sequence as a list.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence