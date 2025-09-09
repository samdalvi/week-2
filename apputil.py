import numpy as np

# update/add code below ...

def ways(n):
    """
    Calculate the number of ways to make change for n cents 
    using nickels (5 cents) and pennies (1 cent).
    Returns the number of ways as (num_nickels, num_pennies) combinations.
    """
    count = 0
    for num_nickels in range(n // 5 + 1):
        num_pennies = n - (num_nickels * 5)
        if num_pennies >= 0:
            count += 1
    return count


def lowest_score(names, scores):
    """
    Return the name of the student with the lowest score.
    Uses NumPy's argmin function to find the index of the minimum score.
    """
    names = np.array(names)
    scores = np.array(scores)
    
    min_index = np.argmin(scores)
    return names[min_index]


def sort_names(names, scores):
    """
    Return a list of student names sorted by their scores in descending order
    (highest to lowest).
    """
    names = np.array(names)
    scores = np.array(scores)
    
    # argsort gives ascending order, so we reverse with [::-1]
    sorted_indices = np.argsort(scores)[::-1]
    # Return the names in that order
    return names[sorted_indices]


# Test code 
if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 1 - Making Change with Nickels and Pennies")
    print("=" * 60)
    
    # Test cases for Exercise 1
    test_values = [12, 20, 3, 0]
    expected_results = [3, 5, 1, 1]
    
    for val, expected in zip(test_values, expected_results):
        result = ways(val)
        print(f"ways({val}) = {result} (expected: {expected})")
        
        # actual combinations
        print(f"  Combinations for {val} cents:")
        for nickels in range(val // 5 + 1):
            pennies = val - (nickels * 5)
            if pennies >= 0:
                print(f"    {nickels} nickels + {pennies} pennies = {nickels*5 + pennies*1} cents")
        print()
    
    print("=" * 60)
    print("EXERCISE 2 - Student Scores Analysis")
    print("=" * 60)
    
    # Test data for Exercise 2
    names = np.array(['Hannah', 'Astrid', 'Abdul', 'Mauve', 'Jung'])
    scores = np.array([99, 71, 85, 62, 91])
    
    print("Student Data:")
    print("-" * 30)
    for name, score in zip(names, scores):
        print(f"  {name:10s}: {score} points")
    print()
    
    # Test Exercise 2, Part 1
    print("Part 1: Student with Lowest Score")
    print("-" * 30)
    lowest = lowest_score(names, scores)
    lowest_score_value = scores[np.argmin(scores)]
    print(f"  Result: {lowest} (score: {lowest_score_value})")
    print(f"  Expected: Mauve (score: 62)")
    print()
    
    # Test Exercise 2, Part 2
    print("Part 2: Students Sorted by Score (Descending)")
    print("-" * 30)
    sorted_names = sort_names(names, scores)
    sorted_scores = np.sort(scores)[::-1]
    
    print("  Sorted Results:")
    for name in sorted_names:
        score_idx = np.where(names == name)[0][0]
        print(f"    {name:10s}: {scores[score_idx]} points")
    
    print("\n  Expected order: Hannah (99), Jung (91), Abdul (85), Astrid (71), Mauve (62)")
    print("=" * 60)