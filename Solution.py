# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
a, b = input().split()
for i in range(1,int(b) + 1):
    for i in combinations(sorted(a),i):
        print("".join(i))
