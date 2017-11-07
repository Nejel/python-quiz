2.
ns = [01, 02, 03, 04, 05, 06, 07, 08, 09, 10]
odds = []
for num in ns:
    if num % 2 != 0:
        odds.append(num)

print(odds)


A. SyntaxError
B. [1, 3, 5, 7, 9]
C. [02, 04, 06, 08, 10]
D. ValueError
