# Moremore

## &nbsp;&nbsp;&nbsp;Description
- "링커리어", "위비티", "씽굿"에 게시된 공모전 데이터를 한 페이지에서 확인
- 검색 기능 및 추천 검색어 기능을 제공하여 필요한 공모전을 빠르게 탐색
- 표시된 공모전을 클릭하면, 해당 공모전 사이트로 이동

## &nbsp;&nbsp;&nbsp;Framework & Version
- **Frontend** : HTML, CSS
- **Backend** : Django (5.0.4), sqlite
- **Crawling** : beautifulsoup (4.12.3), selenium (4.20.0)
- **Data-Processing** : pandas (2.2.2)

## &nbsp;&nbsp;&nbsp;Use
- 버전에 맞는 라이브러리 설치
```shell
pip install django==5.0.4
pip install beautifulsoup4==4.12.3
pip install selenium==4.20.0
pip install pandas=2.2.2
```
- git clone
```shell
git clone https://github.com/ss721229/competition-web.git
```
- save.py 실행 : 공모전 데이터 스크래핑, csv 형태로 해당 디렉터리에 저장
```shell
python save.py
```
- 서버 실행 및 로컬 페이지(http://127.0.0.1:8000/) 접속
```shell
python manage.py runserver
```

## &nbsp;&nbsp;&nbsp;Example
![moremore-Chrome-2024-05-15-09-30-05](https://github.com/ss721229/competition-web/assets/53392184/132e8a1d-980b-45b0-8a67-bbe80677ce58)

## &nbsp;&nbsp;&nbsp;Process
- <a href="https://sanseo.tistory.com/66">공모전 크롤링 (1) - 계획서</a>
- <a href="https://sanseo.tistory.com/71">공모전 크롤링 (2) - 가상환경 및 초기 설정, git remote</a>
- <a href="https://sanseo.tistory.com/72">공모전 크롤링 (3) - mainpage (App 연동, Model 생성)</a>
- <a href="https://sanseo.tistory.com/73">공모전 크롤링 (4) - 데이터 수집 (스크래핑) - 링커리어</a>
- <a href="https://sanseo.tistory.com/77">공모전 크롤링 (5) - 데이터 수집 (스크래핑) - 위비티</a>
- <a href="https://sanseo.tistory.com/78">공모전 크롤링 (6) - 데이터 수집 (스크래핑) - 씽굿</a>
- <a href="https://sanseo.tistory.com/81">공모전 크롤링 (7) - 메인 페이지 (프론트)</a>
- <a href="https://sanseo.tistory.com/83">공모전 크롤링 (8) - 메인 페이지(공모전 표시), 데이터 csv 저장</a>
- <a href="https://sanseo.tistory.com/86">공모전 크롤링 (9) - 세부 페이지(검색, 더보기)</a>
- <a href="https://sanseo.tistory.com/89">공모전 크롤링 - 중간점검</a>
- <a href="https://sanseo.tistory.com/95">공모전 크롤링 (10) - 세부 페이지(검색 기능, 페이지네이션)</a>
- <a href="https://sanseo.tistory.com/96">공모전 크롤링 (11) - 데이터 스크래핑, 디자인 마무리</a>

## &nbsp;&nbsp;&nbsp;Good
- 세 개의 페이지를 따로 봐야하는 불편함을 없애고, 하나의 페이지에서 확인할 수 있다.
- 계획 단계에서 구현하고자 했던 기능을 모두 구현하였다.
- Django 기반에서 프론트엔드/백엔드 구현, 데이터베이스의 개념을 이해하였다.
- 데브코스에서 배운 것을 통해 스크래핑, 웹 페이지 구성을 직접 해본 것에 의의가 있다.

## &nbsp;&nbsp;&nbsp;Bad
- 모든 공모전의 데이터를 가져오면, 사이트 당 약 30분 정도 걸린다.
  - save.py를 다시 실행하더라도 같은 시간이 걸린다.
  - 존재하지 않는 것만 가져오고 스크래핑을 종료하도록 만들면 시간 효율적일 것이다.
- 세부적인 사항보다는 생각했던 기능 구현을 우선으로 진행하였다.
  - 빈 문자열, 공백 검색을 제한하지 않았다.
  - 디자인보다는 각 요소를 페이지에 보여주는 것을 우선시하였다.
  - 모든 코드가 올바르게 동작은 했지만, 모두 효율적인 코드라고는 할 수 없을 것이다.
  - 배포는 고려하지 않았다.
