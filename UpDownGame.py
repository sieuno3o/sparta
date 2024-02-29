import random

def up_down_game():
    max_try_num = 100
    while True:
        random_number = random.randint(1, 100)
        print(random_number)
        try_num = 0

        while True:
            if max_try_num != 100: # 최초 시도가 아닐때만 출력 
                print("\n✧·····················*﹡❋ ❋ ❋﹡*·····················✧")
                print("이전 게임 플레이어 최고 시도 횟수는 %s번 입니다" %max_try_num)

            try:
                input_num = int(input("\n숫자를 입력하세요: "))

                if input_num < 0 or input_num > 100: # 범위 벗어났을 경우
                    print("유효한 범위 내의 숫자를 입력하세요.\n")
                    continue

                try_num += 1

                if input_num < random_number: # 비교
                    print("UP")
                elif input_num > random_number:
                    print("DOWN")
                else:
                    max_try_num = min(max_try_num, try_num)
                    print("\n˖♡ ⁺ ᘏ ⑅ ᘏ\n˖°ฅ(  • · •  ฅ)\n정답입니다!\n")
                    print("시도 한 횟수:", try_num)

                    answer = input("다시 시도 하시겠습니까? (y/n): ").lower()
                    while answer not in ['y', 'n']: 
                        print("잘못된 입력입니다.")
                        answer = input("다시 시도 하시겠습니까? (y/n): ").lower()

                    if answer == "y":
                        if max_try_num > try_num:
                            max_try_num = try_num
                            print(max_try_num)
                        break
                    elif answer == "n":
                        print("\n게임을 종료합니다.")
                        exit()

            except ValueError:
                print("숫자만 입력이 가능합니다.")

if __name__ == "__main__" :
    up_down_game()