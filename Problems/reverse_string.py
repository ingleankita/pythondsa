def reverse_string(s):
    reversed_s = ""
    # range(start, stop, step)
    # -1 step tells python to traverse the string in reverse
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s


def reverse_string_v2(s):
    """This method utilizes Python's slicing notation. In Python, string[start:stop:step] allows you to extract a
    portion of a string based on the specified step size. By specifying -1 as the step, it tells Python to start from
    the end of the string and move towards the beginning, effectively reversing the string."""
    return s[::-1]


print(reverse_string_v2("abcd"))
