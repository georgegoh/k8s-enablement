FROM python:3.9

WORKDIR /usr/src/app

RUN wget -O /tmp/psmisc_23.2-1_amd64.deb http://ftp.us.debian.org/debian/pool/main/p/psmisc/psmisc_23.2-1_amd64.deb
RUN dpkg -i /tmp/psmisc_23.2-1_amd64.deb
RUN rm -f /tmp/psmisc_23.2-1_amd64.deb
RUN wget -O /tmp/stress_1.0.4-4_amd64.deb http://ftp.us.debian.org/debian/pool/main/s/stress/stress_1.0.4-4_amd64.deb
RUN dpkg -i /tmp/stress_1.0.4-4_amd64.deb
RUN rm -f /tmp/stress_1.0.4-4_amd64.deb

RUN adduser --home /usr/src/app flask
RUN chown flask:flask /usr/src/app
USER flask

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000/tcp

CMD [ "sh", "-c", "FLASK_APP=/usr/src/app/app.py FLASK_ENV=development FLASK_DEBUG=0 python -m flask run --host=0.0.0.0 --no-debugger" ]