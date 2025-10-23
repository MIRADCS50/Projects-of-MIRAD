angles = list(map(int, input().split()))
if all(angle > 0 for angle in angles) and sum(angles)==180 and max(angles)==90:
    print("Yes")
else:
    print("No")

