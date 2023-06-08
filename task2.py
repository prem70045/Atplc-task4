def is_armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return True
    else:
        return False

armstrong_nums = []
for num in range(100, 501):
    if is_armstrong(num):
        armstrong_nums.append(num)

print("Armstrong numbers between 100 and 500:")
print(armstrong_nums)
