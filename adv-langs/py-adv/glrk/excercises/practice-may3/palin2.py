def is_palindrome(text: str):
    if not text:
        return False
    if len(text) < 3:
        return True
    left, right = 0, len(text) - 1

    while left < right:
        while left < right and not text[left].isalpha():
            left += 1
        while left < right and not text[right].isalpha():
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True


# Test
# print(is_palindrome("A man, a plan, a canal: Panama"))  # True
# print(is_palindrome("race a car"))  # False
# print(is_palindrome(" "))  # True
print(is_palindrome("zz apt tpa zz"))
