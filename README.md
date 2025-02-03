# 24kng - adminpage

## 애플리케이션 실행

애플리케이션은 Docker를 사용하여 컨테이너화되어 있습니다. 애플리케이션을 실행하려면 Docker와 Docker Compose가 설치되어 있어야 합니다.

1. **`.env` 파일 생성**:
    `.env.example` 파일을 복사하여 `.env` 파일을 만들고 필요한 환경 변수를 채웁니다.

2. **컨테이너 빌드 및 실행**:
    ```sh
    docker compose up -d
    ```

    이 명령어는 Docker Hub에서 미리 빌드된 Docker 이미지를 가져와 컨테이너를 시작합니다.

## 참고 사항

- `myproject`와 `videoupload` 디렉토리는 코드 관리와 협업을 위해 사용됩니다. 이 디렉토리들은 애플리케이션의 소스 코드를 포함하고 있습니다.
- 애플리케이션을 실행할 때는 Docker 이미지와 필요한 설정 파일(`docker-compose.yml`, `nginx` 폴더, `.env`)만 로컬에 필요합니다.
- Docker 이미지를 최신 상태로 유지하기 위해 Docker Hub에서 최신 이미지를 가져오십시오.
- 현재 workflows/deploy.yml 코드는 프로젝트용으로 작성되어 테라폼 코드가 제거되어 있습니다.
