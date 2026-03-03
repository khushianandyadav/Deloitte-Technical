def newPassword(a, b):
    i = 0
    j = 0
    result = []

    # Interleave characters from both strings
    while i < len(a) and j < len(b):
        result.append(a[i])
        result.append(b[j])
        i += 1
        j += 1

    # Append remaining characters (if any)
    if i < len(a):
        result.append(a[i:])
    if j < len(b):
        result.append(b[j:])

    return "".join(result)


# Example usage
a = "hackerrank"
b = "mountain"
print(newPassword(a, b))
