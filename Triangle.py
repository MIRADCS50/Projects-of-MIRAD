angles = list(map(int, input().split()))
if sum(angles)==180 and max(angles)==90:
    print("Yes")
else:
    print("No")

