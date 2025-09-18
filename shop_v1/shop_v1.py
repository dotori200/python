import pymysql
# 1. DB 연동 
conn = pymysql.connect (
    host = "127.0.0.1",
    user = "root",
    password = 'root1234',
    database = 'shop_db'
)

print ('접속 성공')
conn.close() # 접속 해제

# 2. 각 테이블 별 
    # C - insert
    # R - select
    # U - update
    # D - delete
# 3. 메소드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별, 구매횟수, 평균구매액

# 4. 기능 구현과 테스트가 되면 -> streamlit