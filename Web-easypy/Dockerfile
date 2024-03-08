FROM python:3.7-stretch
WORKDIR /app

RUN pip install flask 
# COPY ./app.py /app/app.py
COPY ./run.sh /run.sh
COPY ./flag /flag

#RUN useradd hsctf && echo "hsctf hard nproc 10" >> /etc/security/limits.conf && chmod +x /run.sh
RUN chmod +x /run.sh
CMD [ "/run.sh" ]
