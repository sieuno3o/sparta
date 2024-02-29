import random

def play_rock_paper_scissors():
    # 승, 패, 무승부 카운트
    wins, losses, ties = 0, 0, 0
    choices = ['✌🏻', '✊🏻', '🖐🏻']
    
    while True:
        # 사용자 입력
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").strip().lower()
        if user_choice not in ['가위', '바위', '보']:
            print("유효한 입력이 아닙니다")
            continue
        elif user_choice == '가위':
            user_choice = '✌🏻'
        elif user_choice == '바위':
            user_choice = '✊🏻'
        elif user_choice == '보':
            user_choice = '🖐🏻'
        
        # 컴퓨터 선택
        computer_choice = random.choice(choices)
        print(f"\n사용자: {user_choice}\n컴퓨터: {computer_choice}")
        
        # 승패 결정
        if user_choice == computer_choice:
            print("비겼습니다!\n")
            ties += 1
        elif (user_choice == "✌🏻" and computer_choice == "🖐🏻") or \
             (user_choice == "✊🏻" and computer_choice == "✌🏻") or \
             (user_choice == "🖐🏻" and computer_choice == "✊🏻"):
            print("사용자 승리!\n")
            wins += 1
        else:
            print("컴퓨터 승리!\n")
            losses += 1
        
        again = input("다시 하시겠습니까? (y/n): ").strip().lower()
        while again not in ['y', 'n']: 
            print("잘못된 입력입니다.\n")
            again = input("다시 하시겠습니까? (y/n) : ").lower()
        if again == 'n':
            print("게임을 종료합니다")
            print(f"\n승리: {wins}\n패배: {losses}\n무승부: {ties}")
            break
        elif again == 'y':
            continue

if __name__ == "__main__":
    play_rock_paper_scissors()