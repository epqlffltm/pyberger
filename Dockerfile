# 1. Python 3.11 슬림 버전 이미지 사용
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 프로젝트 파일 전체 복사
COPY . .

# 5. Django 개발 서버 포트 오픈
EXPOSE 8000

# 6. 서버 실행 명령
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
