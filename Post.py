import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        # SHA-256 해싱 알고리즘을 사용하여 비밀번호 해싱
        hasher = hashlib.sha256()
        hasher.update(password.encode('utf-8'))
        return hasher.hexdigest()

    def check_password(self, password):
        return self.hash_password(password) == self.password

    def display(self):
        print(f"회원 이름: {self.name}, 회원 아이디: {self.username}")

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

members = []
posts = []

# 미리 만들어진 회원 데이터
members.append(Member("김시은", "sieun", "pass123"))
members.append(Member("강민석", "minseok", "pass456"))
members.append(Member("양민우", "minwoo", "pass789"))

# 각 회원별로 세 개씩의 게시글 미리 생성
posts.append(Post("첫 번째 게시글", "김시은의 첫 번째 게시글", "sieun"))
posts.append(Post("두 번째 게시글", "김시은의 두 번째 게시글", "sieun"))
posts.append(Post("세 번째 게시글", "김시은의 세 번째 게시글", "sieun"))

posts.append(Post("첫 번째 게시글", "강민석의 첫 번째 게시글", "minseok"))
posts.append(Post("두 번째 게시글", "강민석의 두 번째 게시글", "minseok"))
posts.append(Post("세 번째 게시글", "강민석의 세 번째 게시글", "minseok"))

posts.append(Post("첫 번째 게시글", "양민우의 첫 번째 게시글", "minwoo"))
posts.append(Post("두 번째 게시글", "양민우의 두 번째 게시글", "minwoo"))
posts.append(Post("세 번째 게시글", "양민우의 세 번째 게시글", "minwoo"))

def create_member():
    name = input("이름을 입력하세요: ")
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    members.append(Member(name, username, password))
    print("\n회원 가입이 완료되었습니다.")

def login_and_create_post():
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    for member in members:
        if member.username == username and member.check_password(password):
            title = input("\n게시글 제목을 입력하세요: ")
            content = input("게시글 내용을 입력하세요: ")
            posts.append(Post(title, content, username))
            print("\n게시글이 생성되었습니다.")
            return
    print("\n아이디 또는 비밀번호가 잘못되었습니다.")

def display_members():
    for member in members:
        member.display()

def display_posts_by_user():
    username = input("게시글을 조회할 사용자의 아이디를 입력하세요: ")
    for post in posts:
        if post.author == username:
            print(post.title)

def display_posts_by_keyword():
    keyword = input("검색할 단어를 입력하세요: ")
    for post in posts:
        if keyword in post.content:
            print(post.title)

while True:
    print("\n* ੈ♡‧₊˚* · ✧₊♡* ੈ✧‧₊˚")
    print("1: 회원 가입")
    print("2: 로그인하여 게시글 작성")
    print("3: 회원 목록 보기")
    print("4: 특정 사용자의 게시글 보기")
    print("5: 특정 단어가 포함된 게시글 보기")
    print("0: 종료")
    choice = input("\n원하는 작업의 번호를 입력하세요: ")
    print()

    if choice == "1":
        create_member()
    elif choice == "2":
        login_and_create_post()
    elif choice == "3":
        display_members()
    elif choice == "4":
        display_posts_by_user()
    elif choice == "5":
        display_posts_by_keyword()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도해주세요.")
