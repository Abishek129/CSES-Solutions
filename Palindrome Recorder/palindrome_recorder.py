from collections import Counter

def make_palindrome(s):
    char_count = Counter(s)
    odd_char = None
    odd_count = 0
    
    # Check for palindrome possibility
    for char, count in char_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_char = char
        if odd_count > 1:
            return "NO SOLUTION"
    
    # Create a list to build the palindrome
    result = [None] * len(s)
    left, right = 0, len(s) - 1
    
    # If there is an odd character, place it in the center
    if odd_char:
        result[len(s) // 2] = odd_char
        char_count[odd_char] -= 1
    
    # Fill the remaining characters symmetrically
    for char, count in char_count.items():
        while count > 0:
            result[left] = result[right] = char
            left += 1
            right -= 1
            count -= 2
    
    return "".join(result)

# Example usage
s = input().strip()
print(make_palindrome(s))
