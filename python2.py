class Member:
    def __init__(self, name, phone_number, sex):
        self.name = name
        self.phone_number = phone_number
        self.sex = sex

memberList = []

while True:
    name = input("이름을 입력하세요: ")
    if name == "그만" :
        for x in memberList:
            print("이름은 %s, 전화번호는 %s, 성별은 %s, 입니다." %(x.name, x.phone_number, x.sex))
        break

    phone_number = input("전화번호를 입력하세요: ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요) : ")

    if sex == "male" :
        sex = "male"
    elif sex == "female" :
        sex = "female"
    else :
        sex = "unknown"

    add_member = Member(name, phone_number, sex)
    memberList.append(add_member)

    for i in memberList:
        print("이름은 %s, 전화번호는 %s, 성별은 %s, 입니다." %(i.name, i.phone_number, i.sex))