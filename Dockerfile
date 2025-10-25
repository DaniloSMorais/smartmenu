# Base leve para produção
FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório do app
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app/

# Garante permissões corretas
RUN chmod -R 755 /app

# Copia arquivos estáticos (após copiar o projeto!)
RUN python manage.py collectstatic --noinput

# Expondo porta do Gunicorn
EXPOSE 8000

# Comando para iniciar o app com Gunicorn
CMD ["gunicorn", "smartmenu.wsgi:application", "--workers", "3", "--bind", "0.0.0.0:8000"]
