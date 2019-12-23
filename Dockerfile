FROM jupyter/datascience-notebook:9b06df75e445

COPY requirements.txt ./

RUN pip install -r requirements.txt