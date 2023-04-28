import random

# 定义一个字典，存储石头剪刀布的规则
rules = {
    "石头": "剪刀",
    "剪刀": "布",
    "布": "石头"
}

# 定义一个列表，存储石头剪刀布的选项
choices = ["石头", "剪刀", "布"]

# 设置一个变量，记录玩家的得分
player_score = 0

# 设置一个变量，记录电脑的得分
computer_score = 0

# 设置一个循环，进行多轮游戏
while True:
    # 随机生成电脑的选择
    computer_choice = random.choice(choices)

    # 输入玩家的选择
    player_choice = input("请输入你的选择（石头/剪刀/布）：")

    # 判断玩家是否输入了有效的选项
    if player_choice in choices:
        # 打印双方的选择
        print(f"你的选择是：{player_choice}")
        print(f"电脑的选择是：{computer_choice}")

        # 判断胜负
        if player_choice == computer_choice:
            # 如果平局，打印提示信息，并继续循环
            print("平局！")
        elif rules[player_choice] == computer_choice:
            # 如果玩家赢了，打印提示信息，并增加玩家的得分
            print("你赢了！")
            player_score += 1
        else:
            # 如果玩家输了，打印提示信息，并增加电脑的得分
            print("你输了！")
            computer_score += 1

        # 打印双方的得分
        print(f"你的得分是：{player_score}")
        print(f"电脑的得分是：{computer_score}")

        # 询问是否继续游戏
        answer = input("是否继续游戏？（是/否）：")

        # 判断是否退出游戏
        if answer == "否":
            # 如果退出，打印结束信息，并退出循环
            print("游戏结束！")
            break
    else:
        # 如果输入了无效的选项，打印错误信息，并继续循环
        print("请输入有效的选项！")
