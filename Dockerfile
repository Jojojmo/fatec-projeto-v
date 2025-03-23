# Use uma imagem base oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema (como o curl e ferramentas de compilação)
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

# Instala o Poetry (ferramenta de gerenciamento de dependências)
RUN curl -sSL https://install.python-poetry.org | python3 - \
  && ln -s /root/.local/bin/poetry /usr/local/bin/poetry


# Configura o Poetry para instalar as dependências no ambiente do sistema (sem criar virtualenv)
RUN poetry config virtualenvs.create false

# Copia os arquivos de configuração do Poetry para a imagem
# (pyproject.toml está na raiz, assim como o poetry.lock)
COPY pyproject.toml poetry.lock* /app/

COPY README.md /app/README.md

# Copia os arquivos do diretório "code" para a imagem
COPY app/ /app/app/


# Configura o Poetry para instalar as dependências no ambiente do sistema (sem criar virtualenv)
RUN poetry install


# Define o comando padrão (ajuste conforme a sua aplicação)
# CMD ["python", "/app/code/cli/petro-links.py"]
