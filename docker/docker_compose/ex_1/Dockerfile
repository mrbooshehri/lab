FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirments.txt requirments.txt
RUN pip install -r requirments.txt
COPY . .
CMD ["flask","run"]
