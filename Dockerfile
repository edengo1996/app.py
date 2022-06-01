FROM python:3
WORKDIR /usr/src/app
COPY docker_reqs.txt .
RUN pip install --no-cache-dir -r docker_reqs.txt
COPY . .
CMD ["python", "app.py"]