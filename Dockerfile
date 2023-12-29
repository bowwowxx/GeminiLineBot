FROM python:3.11
MAINTAINER bowwow
WORKDIR /app

COPY requirements.txt ./
COPY gemini_linebot.py ./
COPY line_bot_base.py ./
COPY .env ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -q -U google-generativeai
CMD ["python3", "gemini_linebot.py", "start"]

EXPOSE 8888