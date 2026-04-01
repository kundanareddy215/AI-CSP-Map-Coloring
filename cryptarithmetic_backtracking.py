# Cryptarithmetic using Backtracking (CSP)
# Problem: SEND + MORE = MONEY

# ---------------------------------------------
# CSP FORMULATION
# Variables: S, E, N, D, M, O, R, Y
# Domain: {0–9}
# Constraints:
#   - All letters must have unique digits
#   - S ≠ 0, M ≠ 0 (no leading zero)
#   - SEND + MORE = MONEY
# ---------------------------------------------

letters = ['S','E','N','D','M','O','R','Y']
solution = {}

# Check constraints
def is_valid_partial(sol):

    # Leading digit constraint
    if 'S' in sol and sol['S'] == 0:
        return False
    if 'M' in sol and sol['M'] == 0:
        return False

    # If all variables assigned → check full equation
    if len(sol) == len(letters):
        SEND = sol['S']*1000 + sol['E']*100 + sol['N']*10 + sol['D']
        MORE = sol['M']*1000 + sol['O']*100 + sol['R']*10 + sol['E']
        MONEY = sol['M']*10000 + sol['O']*1000 + sol['N']*100 + sol['E']*10 + sol['Y']

        return SEND + MORE == MONEY

    return True


# Backtracking function
def backtrack(index, used_digits):

    # If all letters assigned
    if index == len(letters):
        return solution

    letter = letters[index]

    for digit in range(10):

        # Ensure unique digits
        if digit in used_digits:
            continue

        solution[letter] = digit

        # Check constraints
        if is_valid_partial(solution):
            result = backtrack(index + 1, used_digits | {digit})
            if result:
                return result

        # Backtrack
        del solution[letter]

    return None


# Solve CSP
result = backtrack(0, set())

# Print result
print("\nSolution:\n")

SEND = result['S']*1000 + result['E']*100 + result['N']*10 + result['D']
MORE = result['M']*1000 + result['O']*100 + result['R']*10 + result['E']
MONEY = result['M']*10000 + result['O']*1000 + result['N']*100 + result['E']*10 + result['Y']

print("SEND  =", SEND)
print("MORE  =", MORE)
print("MONEY =", MONEY)

print("\nLetter Mapping:")
for k in sorted(result):
    print(f"{k} = {result[k]}")
