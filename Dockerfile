FROM python:3.8-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Added FastAPI run command for the backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
