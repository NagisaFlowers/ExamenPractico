FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

#Automatizacion de infraestructura digital II
#Prof. FROYLAN ALONSO PEREZ ALANIS
# GRAU MORENO MANUEL  - 220550