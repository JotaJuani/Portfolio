FROM python:3.10-alpine

ENV PATH="/SCRIPTS:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers

RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /portfolioweb

COPY ./portfolioweb /portfolioweb

WORKDIR /portfolioweb
COPY ./scripts /scripts  
RUN chmod +x /scripts/* 

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol 
RUN chmod -R 755 /vol/web

USER user 

CMD ["/scripts/entrypoint.sh"]