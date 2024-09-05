# Etapa de construcción
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Etapa final
FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copiar todos los archivos de la aplicación
COPY . .

# Establecer Gunicorn como el servidor WSGI para producción
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8500", "app:app"]



