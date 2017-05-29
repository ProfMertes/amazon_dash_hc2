FROM alpine

RUN apk add --update python /
                 py-pip /
                 tcpdump /
                 scapy /
                 && pip install requests
COPY hc2_dash.py /home/dash/

WORKDIR "/home/dash/"
CMD ["python","hc2_dash.py"]