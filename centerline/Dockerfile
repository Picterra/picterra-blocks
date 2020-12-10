FROM osgeo/gdal:3.2.0

RUN apt-get update && apt-get install -y python3-pip

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY block.py /block.py

CMD ["python", "block.py"]
