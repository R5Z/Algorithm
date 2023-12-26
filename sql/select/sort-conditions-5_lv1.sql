/* 최댓값 구하기 - 가장 최근에 보호소에 들어 온 동물의 입소 시간
    programmers */

SELECT MAX(DATETIME) AS DATETIME
FROM ANIMAL_INS;


/* 최솟값 구하기 - 가장 먼저 보호소에 들어 온 동물의 입소 시간
    programmers */

SELECT MIN(DATETIME) AS DATETIME
FROM ANIMAL_INS;