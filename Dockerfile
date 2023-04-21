FROM    python:3.10
WORKDIR /project
COPY    ./app ./app 
COPY    ./run.py .
COPY    ./requirements.txt .
RUN     pip install --no-cache-dir -r requirements.txt 
EXPOSE  8000

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "-w","1", "--env", "PYTHONHASHSEED=0", "run:server"]
