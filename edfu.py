def generate_and_reverse(start, end):
    if start > end:
        print("Invalid input: starting digit should be less than or equal to the ending digit.")
        return
    
    # Generate numbers between start and end (inclusive)
    numbers = list(range(start, end + 1))
    print("Original sequence:", numbers)
    
    # Reverse using slicing
    reversed_numbers = numbers[::-1]
    print("Reversed sequence:", reversed_numbers)
