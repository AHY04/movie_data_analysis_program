# TMDB 영화 데이터 분석 프로젝트

## 1. 프로젝트 의의
Python을 활용해 TMDB API에서 영화 데이터를 수집하여 CSV파일을 생성하고, 정규화된 MySQL 스키마로 적재한 뒤, 다대다 관계를 포함한 분석 쿼리를 작성하여 데이터를 시각화 한다.

- API -> CSV -> MySQL까지 데이터를 적재하는 과정 전체를 경험
- 단순 데이터 수집이 아닌 정규화, 적재, 분석, 데이터 시각화까지 완전한 데이터 파이프라인 설계 및 구현
- JOIN, GROUP BY등 SQL을 활용한 분석 쿼리 작성 능력 향상

## 2. 단계별 진행 내용 및 유의사항

### 1단계 - TMDB API 영화 데이터 수집
- 'get_popular_movies()'함수를 선언하여 인기 영화 목록 가져오기
- 'get_movie_detail()'함수를 선언하여 영화 상세 정보 가져오기
- 수집 항목: 영화 기본 정보, 장르, 감독

*유의사항
- 'append_to_response="credits"'로 감독 정보까지 수집
- API 호출 제한(RATE LIMIT) 주의
- TMDP API사이트에서 파라미터 이름, 구조 등과 같은 서버규약 확인

### 2단계 - CSV파일 생성
- 생성파일:
- movies_raw.csv
- genres.csv
- directors.csv
- movie_genres.csv
- movie_directors.csv

*유의사항
- 반복문 활용으로 인해 'genres.csv'와 'directors.csv'에 중복된 데이터가 저장되는데, 이를 제거하지 않으면 PK 충돌로 인해 MySQL에 적재 불가
- 따라서 'genres.csv'는 'genre_id'기준, 'directors.csv'는 'director_id'기준으로 중복 제거 필요
- CSV파일 생성 후, 저장 경로 및 파일 존재 여부 확인

### 3단계 - MySQL 테이블 생성
- 테이블 설계:
- 'movies' (PK: movie_id)
- 'genres' (PK: genre_id)
- 'directors' (PK: director_id)
- 'movie_genres' (PK: movie_id+genre_id, FK: movie_id(movies), genre_id(genres))
- 'movie_directors' (PK: movie_id+director_id, FK: movie_id(movies), director_id(directors))

*유의사항
- CSV파일의 컬럼과 DB 컬럼의 순서가 일치하는지 확인
- UTF-8 설정 필수(한글 영화 제목 대응)

### 4단계 - CSV->MySQL 적재
- pandas + mysql.connector 사용
- 적재 순서: movies -> genres -> directors -> movie_genres -> movie_directors

*유의사항
- 부모 테이블 먼저 적재 후 자식 테이블 적재(FK 제약으로 인해 부모 테이블이 없으면 INSERT 실패)
- 실행 후 데이터가 잘 적재되었는지 확인

### 5단계 - SQL분석 & 인사이트
- 다대다 JOIN을 활용한 분석 쿼리 작성:
- 감독별 영화 제작량 TOP10
- 감독별 평균 영화 평점 TOP10
- 영화 평점 TOP10
- 장르별 영화 비율
- 장르별 평균 평점

*유의사항
- AVG, COUNT 사용 시 데이터 중복으로 인한 부적절한 집계가능성 검토
