FROM python:3

WORKDIR .

RUN pip3 install discord.py
RUN pip3 install python-dotenv
RUN pip3 install requests

COPY . .


CMD [ "python3", "3B-main.py" ]
