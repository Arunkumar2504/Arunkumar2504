a = "malayalam"
b=""

for i in range(len(a),0,-1):
    b = b + a[i-1]
    # print(b, end='')
if b == a:
    print("yes")
else:       
    print("no")