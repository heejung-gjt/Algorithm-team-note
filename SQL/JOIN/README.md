## JOIN이란
조인이란 둘 이상의 테이블을 연결하여 데이터를 검색하는 방법이다   
여러 테이블에 저장된 데이터를 한 번에 조회해야 할 필요가 있을때 사용한다   
- 보통 둘 이상의 행들의 공통된 값 Primary key 및 Foreign key값을 사용하여 조인한다   
- 두개의 테이블을 select문장 안에서 조인하려면 적어도 하나의 컬럼이 그 테이블 사이에서 공유되어야 한다

### LEFT JOIN
외부조인으로 값이 없더라도 연결이 가능하다 (아직 부서가 없는 사람은 내부 조인에서는 나오지 않지만 외부 조인에서는 부서가 null값인 사람도 출력된다)    
- LEFT는 LEFT의 왼쪽에 기재된 item table을 기준으로 Table이 만들어진다
- 기존의 정보들이 업데이트 될 경우 무엇이 누락/업데이트 되었는지 LFET, RIGHT JOIN으로 알 수 있다

__외부 조인 - 왼쪽 기준__   

```sql
SELECT COLUMN명
FROM 테이블-A명
LEFT JOIN TABLE-B명 ON 조건;
```

__외부 조인 - 오른쪽 기준__   

```sql
SELECT COLUMN명
FROM 테이블-A명
RIGHT JOIN TABLE-B명 ON 조건;
```

### left join 예시
```sql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
```


<br>

### INNER JOIN
INNER JOIN은 mysql에서 JOIN키워드로 사용된다. 일반적으로 사용되는 JOIN이다.    
INNER JOIN의 경우에는 데이터가 NULL로 나오는 경우에는 해당 값이 나오지 않는다    

![Inner](https://user-images.githubusercontent.com/64240637/135619498-9bddf98c-1b95-414a-be6d-3e62da03bba5.png)


### inner join 예시

예를 들어 고객 테이블과 주문 테이블이 있다고 가정해보자. 이때 특정 고객이 주문한 주문 내역만 보고 싶을때 join을 사용하면 쉽게 얻을 수 있다

```sql
SELECT ord.order_date, ord.order_amount
FROM customer AS cus
JOIN orders AS ord ON cus.customer_id = ord.customer_id
WHERE customer_id = 3
```

- JOIN 키워드를 이용해서 연결한 테이블을 지정한다(order과 customer)    
- AS를 사용하여 이름을 변경할 수 있다
- ON 키워드로 각 테이블의 어떤 키를 사용해 연결할지를 정해준다   
- customer의 id가 3인 유저가 주문한 order_date, order_amount내역을 출력한다    


<br>
<br>


##### reference
[https://m.blog.naver.com/kxv1031/221791577556](https://m.blog.naver.com/kxv1031/221791577556)     
[https://til-devsong.tistory.com/95](https://til-devsong.tistory.com/95)