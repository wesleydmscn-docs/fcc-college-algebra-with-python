# Put a zero in for the unknown value

numerator1 = 1
denominator1 = 2

numerator2 = 4
denominator2 = 0

if numerator2 == 0:
    answer = denominator2 * numerator1 / denominator1
    print("numerator2 = ", answer)

if denominator2 == 0:
    answer = numerator2 * denominator1 / numerator1
    print("denominator2 = ", answer)
