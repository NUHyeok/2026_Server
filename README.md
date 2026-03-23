# HTTP 서버 프로젝트

Python `socket` 라이브러리만으로 직접 만든 HTTP 서버.
프레임워크 없이 브라우저 요청을 받아 HTML, CSS, 이미지를 응답하는 웹 서버를 구현했다.

---

## 파일 구조

```text
├── server.py         # 메인 서버 (accept loop)
├── function_na.py    # 핵심 함수 모음 (parse, routing, build_response)
├── cv.html           # 서빙할 HTML 파일
├── styles.css        # 스타일시트
├── profile-photo.png # 프로필 이미지
└── yonsei.png        # 이미지
```

---

## 실행 방법

```bash
python server.py
```

브라우저에서 `http://[내IP]:9999` 접속

---

## 배운 개념 정리

### TCP 소켓
- `server_socket` - 연결 요청을 받는 문지기 역할. 항상 열려서 대기
- `client_socket` - 브라우저가 접속할 때마다 새로 생겼다가 `close()`로 사라짐
- 브라우저가 접속할 때 3-way handshake(SYN -> SYN-ACK -> ACK) 과정을 거친 후 `accept()`가 반환됨

### HTTP 요청
- 브라우저가 서버에 보내는 메시지. 첫 줄이 요청 라인 (`GET / HTTP/1.1`)
- 주요 헤더: `Host`, `User-Agent`, `Accept`, `Connection`
- curl은 1번만 요청하지만 브라우저는 응답이 없으면 재시도함

### HTTP 응답
- 상태라인 + 헤더 + 빈 줄(`\r\n`) + 본문 구조
- `Content-Type` - 브라우저가 파일을 올바르게 해석하게 해줌
- `Content-Length` - 본문의 바이트 수. 문자 수가 아니라 바이트 수

### 파일 서빙
- 텍스트 파일(HTML, CSS)은 `'r'` 모드로 읽고 `.encode('utf-8')`
- 이미지 같은 바이너리 파일은 `'rb'` 모드로 읽어야 함

### 라우팅
- 요청 첫 줄에서 경로를 꺼내서 (`path = request_line.split(' ')[1]`) 분기
- 경로에 맞는 파일과 `Content-Type`을 돌려줌
- 없는 경로는 404 응답

---

## 배운 점 / 회고

- Flask 같은 프레임워크가 내부에서 하는 일을 직접 구현해보니 왜 편한지 이해됨
- `Content-Length`를 안 보내도 동작하지만, 보내야 브라우저가 응답을 정확하게 읽음
- 브라우저는 HTML을 받은 뒤 CSS, 이미지를 추가로 요청함. 라우팅이 없으면 CSS가 안 불러와짐
- 소켓 하나로는 한 번에 한 명만 처리 가능. 동시 접속은 멀티스레드가 필요함
