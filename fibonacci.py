import datetime as datetime

start = datetime.datetime.now()

request_id = 1

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
    print("RequestID:",request_id, "N:",N, " -> ",",".join([str(k) for k in all]))

fd = open('input.txt')
for i in fd:
    N = int(i)
    Fibonacci(N)
    request_id = request_id + 1

end = datetime.datetime.now()

print("################# Start Time:", start, "##############")
print("################# End Time:", end, "##############")