with open("19/data.txt", "r") as file:
    data = file.read().strip().split("\n\n")
    data = [section.split(", ") if i == 0 else section.split("\n")
            for i, section in enumerate(data)]

patterns = data[0]
designs = data[1]

# * Part 1

# ! IDEA: Dynamic Programming
# ! We can use dynamic programming to solve this problem.
# ! We will work backwards from the end of the design string.
# ! At each position, we will check if any of the patterns can match
# ! the substring starting at the current position.
# ! If a pattern matches and the remaining string can be formed, we can
# ! form the substring starting at the current position.
# ! We will store this information in a dp array.


def solve(design, patterns):
    n = len(design)
    # dp[i] represents whether we can form the substring from index i to end
    dp = [False] * (n + 1)
    # Empty string can always be formed
    dp[n] = True

    # Work backwards from the end of the string
    for i in range(n-1, -1, -1):
        for pattern in patterns:
            # Check if pattern matches at current position and remaining string can be formed
            if (i + len(pattern) <= n and
                design[i:i+len(pattern)] == pattern and
                    dp[i + len(pattern)]):
                dp[i] = True
                break

    # Return whether entire string can be formed
    return dp[0]


res = sum(solve(design, patterns) for design in designs)
print(res)


# * Part 2

# ! IDEA: Dynamic Programming
# ! If a pattern matches, we can add the number of ways to form the
# ! remaining string to the total number of ways to form the substring
# ! starting at the current position.
# ! We will store this information in a dp array.


def count_combinations(design, patterns):
    n = len(design)
    # dp[i] represents the number of ways to form the substring from i to the end
    dp = [0] * (n + 1)
    # Empty string has 1 way to be formed
    dp[n] = 1

    # Work backwards from the end of the string
    for i in range(n-1, -1, -1):
        total = 0
        for pattern in patterns:
            # Check if pattern matches at the current position
            if (i + len(pattern) <= n and
                    design[i:i+len(pattern)] == pattern):
                # Add the number of ways to form the remaining string
                total += dp[i + len(pattern)]
        dp[i] = total

    return dp[0]


res = sum(count_combinations(design, patterns) for design in designs)
print(res)
