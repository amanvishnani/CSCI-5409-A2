import datetime as datetime

start = datetime.datetime.now()
def factorial(N):
    if N < 2:
        return 1
    return factorial(N-1) * N

fd = open('input.txt')
req_id = 1
for i in fd:
    N = int(i)
    print("RequestID:",req_id, "N:", N, " -> ", factorial(N))

end = datetime.datetime.now()

print("################# Start Time:", start, "##############")
print("################# End Time:", end, "##############")