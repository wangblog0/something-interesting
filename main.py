import random

# 生成一个1到100之间的随机整数
answer = random.randint(1, 100)

# 设置一个变量来记录猜测的次数
guess_count = 0

# 设置一个循环来不断地猜测
while True:
    # 输入一个数字
    guess = int(input("请输入一个1到100之间的数字："))

    # 增加猜测的次数
    guess_count += 1

    # 判断猜测是否正确
    if guess == answer:
        # 如果正确，打印恭喜信息，并退出循环
        print(f"恭喜你，你在第{guess_count}次就猜对了！")
        break
    elif guess < answer:
        # 如果太小，打印提示信息，并继续循环
        print("太小了，再大一点！")
    else:
        # 如果太大，打印提示信息，并继续循环
        print("太大了，再小一点！")
