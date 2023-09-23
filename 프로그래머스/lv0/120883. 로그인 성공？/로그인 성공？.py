def solution(id_pw, db):
    id_ = 0
    pw_ = 0
    for i in db:
        # id.append(i[0])
        # 입력한 아이디와 일치하는 아이디가 있으면
        if id_pw[0] == i[0]:
            # pw까지 일치하는지 확인
            if i[1] == id_pw[1]:
                return 'login'
            else:
                return 'wrong pw'
    return 'fail'