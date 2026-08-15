# QA Portfolio – Playwright + Python + Postman/Newman + Azure DevOps

Projeto de portfólio de automação de testes demonstrando:

- Testes de UI com **Playwright + Python** (Page Object Model)
- Testes de API com **Python + requests** (pytest)
- Coleção de **Postman** equivalente, executável via **Newman** no pipeline
- Pipeline de **CI/CD no Azure DevOps** que builda, roda os testes e publica relatórios

## Aplicações usadas para teste
- UI: https://www.saucedemo.com (loja de e-commerce de demonstração)
- API: https://reqres.in (API pública de testes)

Ambas são apps públicas usadas só como alvo de teste — troque pela sua aplicação real quando for aplicar o framework em um projeto de trabalho.

## Estrutura do projeto

```
qa-portfolio-playwright/
├── pages/                  # Page Object Model (camada de UI)
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   ├── ui/
│   │   └── test_login.py   # Testes E2E com Playwright
│   └── api/
│       └── test_users_api.py  # Testes de API com requests
├── postman/
│   └── QA-Portfolio-API.postman_collection.json
├── azure-pipelines.yml      # Pipeline de CI/CD
├── pytest.ini
├── conftest.py
├── requirements.txt
└── .gitignore
```

## Como rodar localmente

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install --with-deps chromium

# Todos os testes
pytest -v

# Só UI
pytest -v -m ui

# Só API
pytest -v -m api

# Relatório HTML
pytest --html=report.html --self-contained-html
```

## Rodando a coleção Postman via Newman

```bash
npm install -g newman
newman run postman/QA-Portfolio-API.postman_collection.json -e postman/environment.json
```

## Decisões técnicas

- **Page Object Model**: cada página tem sua classe, isolando seletores da lógica de teste. Facilita manutenção quando o front muda.
- **Markers do pytest** (`ui`, `api`, `smoke`): permitem rodar subconjuntos de testes no pipeline (ex: só smoke em cada PR, suíte completa à noite).
- **Testes independentes**: cada teste cria seu próprio estado (login, dados), sem depender de ordem de execução — evita flakiness.
- **Postman + Newman no pipeline**: mantém a coleção como documentação viva da API, além dos testes em código.

## Pipeline no Azure DevOps

O `azure-pipelines.yml` executa em cada push/PR:
1. Instala Python e dependências
2. Instala navegadores do Playwright
3. Roda os testes (UI + API)
4. Roda a coleção Postman via Newman
5. Publica os resultados (JUnit XML) e o relatório HTML como artefatos do build

