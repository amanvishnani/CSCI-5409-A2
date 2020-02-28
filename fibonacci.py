import datetime as datetime

start = datetime.datetime.now()
def Fibonacci(N):
    all = []
    f1 = 0
    f2 = 1
    for i in range(N):
        if i is 0:
            all.append(f1)
        elif i is 1:
            all.append(f2)
        else:
            temp = f1 + f2
            f1 = f2
            f2 = temp
            all.append(f2)
    print(",".join([str(k) for k in all]))

fd = open('input.txt')
for i in fd:
    N = int(i)
    Fibonacci(N)

end = datetime.datetime.now()

print(f"################# Start Time: {start} ##############")
print(f"################# End Time: {end} ##############")