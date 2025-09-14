def balanced_brackets(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    opens = set(pairs.values())
    stack: list[str] = []

    for ch in s:
        if ch in opens:
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            # if we truly expect ONLY brackets, treat others as invalid:
            return False
    return not stack


# True cases
print(balanced_brackets("()"))
print(balanced_brackets("([]){}"))
print(balanced_brackets("{[()()]}"))

# False cases
print(balanced_brackets("({)}"))  # wrong nesting
print(balanced_brackets("("))  # unclosed
print(balanced_brackets("())"))  # extra close
