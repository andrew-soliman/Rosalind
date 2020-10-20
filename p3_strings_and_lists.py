# Rosalind Problem 1.3

# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 

sequence = input("Input list here --> ")
a = 22 
b = 27 
c = 97 
d = 102
print(sequence[a:b+1] + ' ' + sequence[c:d+1])