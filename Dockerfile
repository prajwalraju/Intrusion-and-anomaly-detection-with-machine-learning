FROM ubuntu 

### install all required packages
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN apt-get install apache2 wget unzip vim cron -y
RUN apt clean 

### anomaly detection repo
WORKDIR /root
RUN wget https://github.com/prajwalraju/Intrusion-and-anomaly-detection-with-machine-learning/archive/refs/heads/master.zip 
RUN unzip master.zip

WORKDIR /root/Intrusion-and-anomaly-detection-with-machine-learning-master
RUN pip install -r requirements.txt
RUN cp settings_template.conf settings.conf

# copy detection files
RUN touch log_position.txt
COPY ./continuousLogDetection.py .
COPY ./predict.py .
COPY ./MODELS/attack_classifier_dt_1687847175.pkl /root/Intrusion-and-anomaly-detection-with-machine-learning-master/MODELS/attack_classifier_dt_1687847175.pkl

# # copy cron
COPY ./cronjob /etc/cron.d/cronjob
COPY continuousLogDetectionContainerSetup.sh continuousLogDetectionContainerSetup.sh
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob

EXPOSE 80
CMD ["bash", "continuousLogDetectionContainerSetup.sh"]