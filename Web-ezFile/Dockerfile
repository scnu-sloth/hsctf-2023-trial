FROM php:7.4.5-apache

COPY ./Th1s_i5_y0u_fl4g.txt /Th1s_i5_y0u_fl4g.txt
COPY ./cron-file /cron-file
COPY ./start.sh /start.sh

# COPY ./src/config_file.php /var/www/html/
# COPY ./src/index.php /var/www/html/
# COPY ./src/show.php /var/www/html/

RUN mkdir /var/www/html/upload
RUN cp /etc/apt/sources.list /etc/apt/sources.list_bak

COPY ./sources.list /etc/apt/sources.list

# RUN cat /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update
RUN apt-get -y upgrade --fix-missing
RUN chmod 777 /start.sh
#RUN chmod 777 /var/spool/cron/crontabs/root
RUN apt-get install -y vim --fix-missing
RUN apt-get install -y cron
RUN service cron start
RUN crontab /cron-file 
# RUN service cron restart

#ENTRYPOINT ["/start.sh"]
# CMD ["/start.sh"]


EXPOSE 80