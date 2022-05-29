FROM python:3.9 
WORKDIR /recipe_api
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP=./recipe_api/index.py
ENV FLASK_ENV=development
CMD ["source $(pipenv --venv)/bin/activate", "&" "flask", "run", "--host=0.0.0.0"]

