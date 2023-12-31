# -- 코드를 입력하세요

# SELECT 
#     A.CAR_ID,
#     CASE WHEN COUNT (DISTINCT AVAILABILITY) = 2 THEN '대여중' 
#     ELSE '대여 가능' END AS AVAILABILITY
# FROM(
# SELECT CAR_ID,
#     CASE WHEN '2022-10-16' BETWEEN DATE(START_DATE) AND DATE(END_DATE) 
#     OR DATE(END_DATE) = '2022-10-16' THEN '대여중' 
#     ELSE '대여 가능' END AS AVAILABILITY
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# ) A
# GROUP BY CAR_ID
# ORDER BY CAR_ID DESC



SELECT C.CAR_ID, C.AVAILABILITY
FROM (
    SELECT
        A.CAR_ID,
        CASE
            WHEN '2022-10-16' BETWEEN B.START_DATE AND B.END_DATE THEN "대여중" ELSE "대여 가능"
        END AS AVAILABILITY,
        A.HISTORY_ID,
        ROW_NUMBER() OVER(PARTITION BY A.CAR_ID ORDER BY A.HISTORY_ID ASC) AS RNUM
    FROM (
            SELECT
                CAR_ID,
                MAX(HISTORY_ID) AS HISTORY_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            GROUP BY CAR_ID

            UNION

            SELECT CAR_ID, HISTORY_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE '2022-10-16' BETWEEN START_DATE AND END_DATE) A

    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B ON A.HISTORY_ID=B.HISTORY_ID) C
WHERE C.RNUM = 1
ORDER BY C.CAR_ID DESC;