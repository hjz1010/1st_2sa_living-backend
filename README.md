## 1차 프로젝트 Back-end 소개

- 가구 판매 사이트 [까사리빙](https://www.casa.co.kr/) 클론 프로젝트
- 2주 간의 프로젝트 기간 동안 완성을 목표로 사이트 필수 구현기능을 구현했습니다.
- 개발환경 초기세팅, DB모델링, 기능 별 앱 구현

### 개발 인원 및 기간

- 개발기간 : 2022/7/18 ~ 2022/7/29 (2주)
- 개발 인원 : 프론트엔드 4명, 백엔드 3명
- [프론트 github 링크](https://github.com/wecode-bootcamp-korea/35-1st-2sa-living-frontend)

### 프로젝트 선정이유

- 지금까지 익힌 내용을 바탕으로 하면서도, 구현해 본 적 없는 기능들을 가진 사이트인 점에 중점을 두고 선정했습니다.

### DB 모델링
![](./1st_project_modeling.png)

### 프로젝트 시연 영상
[![2Sa_living](https://img.youtube.com/vi/znviVvNpcWo/0.jpg)](https://www.youtube.com/watch?v=znviVvNpcWo)


<br>

## 적용 기술 및 구현 기능

### 적용 기술

> Back-End : Python, Django web framework, Bcrypt, JWT, My SQL

<br>


### 구현 기능

&nbsp;&nbsp; \- 회원가입 / 로그인
```
- 제품 카테고리 및 서브 카테고리 제공
- 제품 리스트 
  - 카테고리 별 제품 
  - 페이지네이션 (limit 값 선택가능) 
  - 제품 정렬방식 선택 기능 (id순, 신상품순, 높은 가격순, 낮은 가격순, 판매량순)
  - 필터링 기능 (색상, 브랜드, 가격)
- 제품 정보 상세보기
  - 관련 상품 리스트 제공
```
&nbsp;&nbsp; \- 장바구니    
&nbsp;&nbsp; \- 주문하기     
&nbsp;&nbsp; \- 리뷰 


<br>

## Reference

- 이 프로젝트는 [까사리빙](https://www.casa.co.kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
