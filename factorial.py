import datetime as datetime

start = datetime.datetime.now()
def factorial(N):
    if N < 2:
        return 1
    return factorial(N-1) * N

fd = open('input.txt')
for i in fd:
    N = int(i)
    print(N, " -> ", factorial(N))

end = datetime.datetime.now()

print("################# Start Time:", start, "##############")
print("################# End Time:", end, "##############")