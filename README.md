# Fatec Projeto V

Bem-vindo ao repositório do **Projeto V** – uma iniciativa destinada aos alunos do 2º semestre de 2022. Este projeto reúne um agente de Inteligência Artificial focado em Educação, com a proposta de elaborar simulados com níveis progressivos de dificuldade.

## Índice

- [Requisitos](#requisitos)
- [Descrição do Projeto](#descrição-do-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Utilizar o Projeto](#como-utilizar-o-projeto)
- [Como Contribuir](#como-contribuir)

## Requisitos

- **Docker**: Certifique-se de que o Docker está instalado em sua máquina.  
  [Instruções para instalação](https://docs.docker.com/get-docker/)

## Descrição do Projeto

O projeto utiliza o modelo de IA **llama3.1**, que é executado pelo serviço Ollama dentro de um ambiente configurado via `docker-compose`. Essa solução foi desenvolvida para apoiar a criação de simulados educativos, ajustando os desafios conforme o nível de dificuldade.

## Estrutura do Projeto

- **/llm**:  
  Diretório responsável pela integração e criação do agente de IA.

- **/backend**:  
  Diretório dedicado ao desenvolvimento de uma API utilizando o framework [FastAPI](https://fastapi.tiangolo.com/).

## Como Utilizar o Projeto

Para iniciar o ambiente de desenvolvimento, siga os passos abaixo:

1. **Verifique a instalação do Docker**: Confirme que o Docker está instalado e funcionando em sua máquina.
2. **Execute o Docker Compose**:  
   Na raiz do projeto, execute o comando abaixo para construir e iniciar os containers:

   ```bash
   docker-compose up --build
   ```

   > **Nota:** O projeto está configurado para fazer o bind do serviço backend com o diretório `./app/` mapeado para `:/app/app/`. Assim, alterações realizadas nesse diretório serão refletidas na próxima execução do `docker-compose`.

## Como Contribuir

Contribuições são muito bem-vindas! Se você faz parte do curso de Ciência de Dados, siga as orientações abaixo para colaborar:

1. **Crie uma branch**: Cada grupo deve criar sua própria branch para desenvolver as funcionalidades ou correções desejadas.
2. **Realize as alterações**: Faça as modificações necessárias em sua branch.
3. **Abra um Pull Request (PR)**: Envie seu PR para a branch `master`. 
4. **Validação do Código**: O PR passará por uma revisão para garantir a qualidade e a aderência ao projeto.

