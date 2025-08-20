# API de Tarefas com Django REST Framework

Este projeto é uma API RESTful para gerenciamento de tarefas (To-Do), desenvolvido como o projeto prático do curso **"Build A Python Django API With Django Rest Framework"**.

Este repositório não apenas demonstra a aplicação bem-sucedida dos conceitos de desenvolvimento de API com Django, mas também serve como um testemunho da minha proficiência em utilizar ferramentas de Inteligência Artificial (LLM) como um copiloto de desenvolvimento. A IA foi empregada para acelerar a produtividade, otimizar código, depurar e gerar documentação técnica de alta qualidade.

## Visão Geral do Projeto

A API permite que os usuários realizem operações CRUD (Criar, Ler, Atualizar, Deletar) em tarefas. Ela foi construída utilizando Python, o framework Django e o Django REST Framework (DRF), seguindo as melhores práticas para a criação de APIs robustas e escaláveis.

### Tecnologias Utilizadas

*   **Backend:** Python, Django
*   **API:** Django REST Framework (DRF)
*   **Banco de Dados:** SQLite (para desenvolvimento)
*   **Ambiente:** Virtual Environment (venv)
*   **Ferramentas de Teste de API:** Postman

## Jornada de Aprendizagem e Competências Adquiridas

Este projeto solidificou meu conhecimento em uma variedade de áreas críticas para o desenvolvimento de back-end e APIs.

### Fundamentos do Django e DRF

*   **Construção de APIs RESTful:** Design e implementação de endpoints seguindo os padrões REST.
*   **Serializers:** Criação de serializers, incluindo `ModelSerializer` e `HyperlinkedModelSerializer`, para converter tipos de dados complexos (como querysets e instâncias de modelo) em tipos de dados nativos do Python, que podem ser facilmente renderizados em `JSON`.
*   **Views e ViewSets:** Utilização de `APIView`, `Generic Views` e `ViewSets` (incluindo `Routers`) para estruturar a lógica de negócios de forma eficiente e reutilizável.
*   **Models:** Definição de modelos de dados no Django ORM para representar a estrutura do banco de dados.
*   **URLs e Roteamento:** Gerenciamento de rotas da API para mapear endpoints para as views correspondentes.
*   **Painel de Administração do Django:** Configuração e personalização do admin para gerenciamento de dados.

### Maestria em Desenvolvimento Assistido por IA (LLM)

Uma das competências mais valiosas que utilizei e aprimorei neste projeto foi a colaboração com Modelos de Linguagem Grandes (LLMs). Esta abordagem moderna de desenvolvimento me permitiu:

*   **Geração de Código Boilerplate:** Acelerar a criação de estruturas repetitivas, como serializers e views iniciais.
*   **Refatoração e Otimização:** Analisar blocos de código e sugerir melhorias de performance e legibilidade.
*   **Depuração Acelerada:** Identificar rapidamente a causa raiz de erros e obter soluções contextuais.
*   **Criação de Documentação Técnica:** Gerar documentação clara e profissional, como esta, que valoriza o projeto para recrutadores e outros desenvolvedores.

## Aplicação Profissional das Habilidades

As competências desenvolvidas neste projeto são diretamente aplicáveis em diversas áreas do mercado de trabalho de tecnologia, incluindo:

*   **Desenvolvimento de Back-end:** Construção da lógica de servidor para aplicações web e mobile.
*   **Criação de Microsserviços:** Desenvolvimento de serviços independentes e coesos que se comunicam via API.
*   **Integração de Sistemas:** Criação de APIs que permitem que diferentes softwares troquem informações de forma segura e padronizada.
*   **Engenharia de Software em Geral:** Aplicação de boas práticas de desenvolvimento, controle de versão (Git) e automação de tarefas.

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd todo_api
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

A API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints da API

Você pode interagir com a API usando ferramentas como o Postman ou `curl`.

| Método | Endpoint              | Descrição                               |
| :----- | :-------------------- | :---------------------------------------- |
| `GET`  | `/tasks/`             | Lista todas as tarefas.                   |
| `POST` | `/tasks/`             | Cria uma nova tarefa.                     |
| `GET`  | `/tasks/<int:pk>/`    | Obtém os detalhes de uma tarefa específica. |
| `PUT`  | `/tasks/<int:pk>/`    | Atualiza uma tarefa específica.           |
| `DELETE`| `/tasks/<int:pk>/`    | Deleta uma tarefa específica.             |

