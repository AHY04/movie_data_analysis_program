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
- 생성파일: movies_raw.csv / genres.csv / directors.csv / movie_genres.csv / movie_directors.csv

*유의사항
- 반복문 활용으로 인해 'genres.csv'와 'directors.csv'에 중복된 데이터가 저장되는데, 이를 제거하지 않으면 PK 충돌로 인해 MySQL에 적재 불가
- 따라서 'genres.csv'는 'genre_id'기준, 'directors.csv'는 'director_id'기준으로 중복 제거 필요
- CSV파일 생성 후, 저장 경로 및 파일 존재 여부 확인
