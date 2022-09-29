FROM python:3.8

WORKDIR /app

COPY tree_in_line.py /app

CMD ["python", "tree_in_line.py"]