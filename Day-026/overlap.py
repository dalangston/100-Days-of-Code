with open('file1.txt') as f:
    f1 = [int(line.strip()) for line in f if line != '\n']

with open('file2.txt') as f:
    f2 = [int(line.strip()) for line in f if line != '\n']

result = [num for num in f1 if num in f2]

# Write your code above 👆

print(result)



