FROM python:3.9-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 시스템 패키지 업데이트 및 MySQL 개발 헤더 설치
RUN apt-get update && apt-get install -y \
    libpq-dev \
    default-libmysqlclient-dev \
    build-essential \
    && apt-get clean

# pip 업그레이드
RUN pip install --upgrade pip

COPY requirements.txt /app/

# requirements.txt에서 종속성 설치
RUN pip install -r requirements.txt

COPY . /app/

# static 파일을 미리 수집합니다.
RUN python manage.py collectstatic --noinput

# gunicorn을 사용하여 앱 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
