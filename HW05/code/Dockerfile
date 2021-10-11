FROM agrigorev/zoomcamp-model:3.8.12-slim  

RUN pip install pipenv
RUN pip install gunicorn
RUN pip install flask
WORKDIR /app    
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system    
COPY ["predict_app.py", "*.bin", "./"]

EXPOSE 9696 
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_app:app"]