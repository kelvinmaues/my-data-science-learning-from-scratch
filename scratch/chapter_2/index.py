
# The pound sung marks the start of a comment. Python itself
# ignores the comments, but they're helpful for anyone reading the code.
for i in [1, 2, 3, 4, 5]:
  print(i)
  for j in [1, 2, 3, 4, 5]:
    print(j)
    print(i + j)
  print(i)
print("done looping")