# FROM continuumio/anaconda3
FROM continuumio/miniconda3:24.1.2-0

WORKDIR /usr/src/app

COPY . .

RUN conda install -y tensorflow flask pillow

EXPOSE 3000

CMD [ "python", "server.py" ]
