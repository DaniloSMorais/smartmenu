# Usando imagem slim para produção
FROM python:3.11-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório da aplicação
WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copia dependências e instala
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o projeto
COPY . /app/

EXPOSE 8000

# Comando para rodar com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "smartmenu.wsgi:application"]
