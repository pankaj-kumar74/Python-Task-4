# Task 26: Check Balanced Parentheses
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

if __name__ == "__main__":
    s = input("Enter parentheses string: ")
    print("Balanced:" if is_balanced(s) else "Not Balanced")
