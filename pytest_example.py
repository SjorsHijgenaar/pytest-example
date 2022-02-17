from pytest import approx
from pytest import raises

def add(a, b):
    return a+b

def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError('received negative input')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_word_occurrence_in_file(file_name, word):
    """
    Counts how often word appears in file file_name.
    Example: if file contains "one two one two three four"
             and word is "one", then this function returns 2
    """
    count = 0
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            count += words.count(str(word))
    return count

def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
    def go_for_a_walk(self):  # <-- how would you test this function?
        self.hunger += 1

def test_add():
    assert add(1, 2) == 3
    assert add("1", "2") == "12"
    assert add(0.1, 0.2) == approx(0.3)

def test_factorial():
    with raises(Exception):
        factorial(-1)
    with raises(Exception):
        factorial(0.1)
    assert factorial(3) == 6
    assert factorial(10) == 3628800
    assert factorial(20) == 2432902008176640000
    assert factorial(5) == 5*4*3*2*1
    assert factorial(5) == 120

def test_count_word_occurrence_in_file():
    assert count_word_occurrence_in_file('test.txt', 'hello') == 6
    assert count_word_occurrence_in_file('test.txt', 'hi') == 0
    # actually we believe the test is correct but the function itself is incorrect
    # the function doesn't force a str type input parameter
    # but doesn't work for any other input
    assert count_word_occurrence_in_file('test.txt', 5) == 0    
    assert count_word_occurrence_in_file('test.txt', 0.6) == 1
    assert count_word_occurrence_in_file('test.txt', 6) == 1

def test_count_word_occurrence_in_string():
    assert count_word_occurrence_in_string('one two one two three four', 'one') == 2