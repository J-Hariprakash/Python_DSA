def removeParathsis(s):

    temp =""
    count = 0
    result = ""

    for ch in s:
        temp += ch
        if ch =="(":
            count += 1
        elif ch==")":
            count -= 1

        if count == 0:
            temp = temp[1:-1]
            result += temp
            temp = ""

    return result

s = input("Enter a Paranthsis: \n")
result = removeParathsis(s)
print(result)









# We loop through the string and build each primitive using a temp string.
# Once a primitive is complete (open and close count match), we remove its outermost parentheses.
# We then add the inner part (temp[1:-1]) to the final result.
# This uses a simple counter to track open brackets and resets after each primitive.
# Efficient and easy to understand one-pass solution.
