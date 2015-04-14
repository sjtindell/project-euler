# What are the first 10 digits of the sum of the following one-hundred 50-digit numbers?

answer = 0

with open('euler_13.txt', 'r') as f:
    for line in f:
        answer += int(line.strip())

print(str(answer)[:10])
