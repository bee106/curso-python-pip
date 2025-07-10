FROM python:3.8

WORKDIR /charts
COPY requirementes.txt /./requirementes.txt

RUN pip install --no-cache-dir --upgrade -r /. requirementes.txt

COPY . /charts/

CMD bash -c "while true; do sleep 1; done"