FROM quay.io/bandit145/scsu-test-python3:latest
RUN pip3 install flask
COPY app.py /app.py
EXPOSE 5000/tcp
ENTRYPOINT FLASK_APP=/app.py flask run --host=0.0.0.0
