    FROM  python

    WORKDIR /usr/src/app

    RUN pip install  --upgrade pip

    COPY  ./requiments.txt /usr/src/app/requiments.txt

    RUN  pip install  -r requiments.txt

    COPY  . /usr/src/app/   

    CMD [ "python3", "run.py"]


