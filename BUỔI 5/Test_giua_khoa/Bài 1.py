# Bài 1:
numbers = list(map(int, input().split()))

counter = {}
for num in numbers:
    counter[num] = counter.get(num, 0) + 1

result = []
for num, count in counter.items():
    if count % 5 == 0 and count % 10 != 0:
        result.append(num)

print(*result)

