k = int(input())
money = []
for _ in range(k):
    num = int(input())
    money.append(num) if num else money.pop()
print(sum(money))
