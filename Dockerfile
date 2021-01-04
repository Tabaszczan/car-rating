FROM python:3
ENV PYTHONUNBUFFERED=1
ENV SECRET_KEY='jt0f$y6u7cut)&zr(9b+9gsct+h$fgmp!w6nm=)h2x+smemnd1'
WORKDIR /car_rating
COPY requirements.txt /car_rating/
RUN pip install -r requirements.txt
COPY . /car_rating/