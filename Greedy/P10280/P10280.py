from sys import stdin

stdin = open("./input.txt", 'r')

# n : pizza의 수 , p: 선호하는 pizza의 index
n, p = map(int, stdin.readline().rstrip().split())

if (n - 1) % 3 == 0:
    # Alice가 피자를 select하는 횟수
    alice_num = (n - 1) // 3
    # Bob이 피자를 select하는 횟수
    bob_num = (n - 1) // 3
elif (n - 1) % 3 == 1:
    # Alice가 피자를 select하는 횟수
    alice_num = (n - 1) // 3 + 1
    # Bob이 피자를 select하는 횟수
    bob_num = (n - 1) // 3
else:
    # Alice가 피자를 select하는 횟수
    alice_num = (n - 1) // 3 + 1
    # Bob이 피자를 select하는 횟수
    bob_num = (n - 1) // 3 + 1


if p > bob_num and p < n - alice_num + 1:
    print("YES")
else:
    print("NO")
