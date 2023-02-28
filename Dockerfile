FROM python:3

WORKDIR .

RUN pip3 install discord.py
RUN pip3 install python-dotenv
RUN pip3 install requests
RUN pip3 install wavelink
RUN pip3 install PyNaCl

COPY . .


CMD ["python3", "3B-main.py"]
