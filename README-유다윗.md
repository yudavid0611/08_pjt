# 08_PJT

## 좋아요 기능 구현

### `views.py`
- 수정 사항
  - **context**
    - 현재 좋아유 여부에 대한 데이터를 `is_liked` 변수에 저장
    - 현재 좋아유 수에 대한 데이터를 `likes_count`에 저장
  - **return**
    - `JsonResponse(context)`를 통해 두 변수를 반환

- 어려웠던 점
  - `return JsonResponse(context)`를 로그인 여부를 파악하는 if문 안쪽에 넣으면 axios로 에러를 넘겨주지 않고 .then에 response 인자로 들어간다. 그래서 if문 밖으로 빼주었다.

### `profile.html`
- 수정 사항
  - **form tag**
    - `data-user-id` 속성을 통해 `review.pk` 전달
    - id 설정
  - **script**
    - `csrf-token`, `reviewId` 에 대한 데이터 변수에 저장
    - `axios`를 이용하여 `POST` 요청
    - 요청이 정상적으로 이루어 질 경우
      - 좋아요 버튼의 텍스트 변경
      - 좋아요 수 변경

- 어려웠던 점
  - csrf 토큰을 select할 때 .value를 꼭 써줘야 한다.
  - .catch를 써줌으로써 에러 메시지를 출력하는 게 디버깅할 때 좋다.

### 후기
  - 직접 코딩하기 전에 어떤 식으로 개발해나갈 것인지 미리 충분히 시간을 들여 기획하는 것이 처음에는 조금 느릴지 몰라도 추후 수정사항이 적어져 좋다.
  - 함께 프로젝트를 수행하는 것이 더 양질의 결과물을 낼 수 있고, 또한 서로 모르는 부분, 헷갈리는 부분을 질문하며 배움이 두 배가 되는 것 같다.