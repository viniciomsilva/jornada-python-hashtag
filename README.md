# Jornada Python | Hashtag | SET. 2025

Este repositório contém os códigos dos projeto desenvolvidos na Jornada Python
da Hashtag em setembro de 2025.

No evento foram desenvolvidos quatro projetos em Python, abordando as principais
áreas onde o Python têm destaque: automação de tarefas; análise de dados; e IA.

## Começando

**\#1. Clonar o repositório**

```bash
git clone https://github.com/viniciomsilva/jornada-python-hashtag.git <MyProjectFolderName>
```

**\#2. Iniciar o Ambiente Virtual Python e Instalar as Dependências**

```bash
python -m venv .venv

pip install -r requirements.txt
```

**\#3. Baixar os Dados**

Todos os arquivos de dados devem ficar na pasta ` ./data/ ` na raiz do projeto.

* Os arquivos ` .csv ` não estão no repositório. Baixe-os [aqui](https://www.dropbox.com/scl/fo/11sbrez5g9ymifinrsxif/APKpco4zH0RJxuVpa2k3o7k?rlkey=jk64ht763xgfvrsodstm60568&st=u6x9tjo9&dl=0).
  * Salve-os sem renomear na pasta ` ./data/ `.
* A chave de API da OpenAI não está no repositório:
  1. Crie uma conta na [OpenAI API Platform](https://auth.openai.com/log-in).
  2. Crie um *Novo Projeto*.
  3. Pegue a sua API key.
  4. Crie o arquivo ` api_key.txt ` na pasta ` /data/ ` e salve a chave nele.

> NOTA: O arquivo ` api_key.txt ` deve ter apenas uma linha com a chave.

## Cada Projeto

* Dia #1 | [Python Power Up](./python_power_up/): Automação de cadastro de produtos.
* Dia #2 | [Python Insights](./python_insights/): Análise de cancelamentos de serviço.
* Dia #3 | [Python IA](./python_ia/): Análise de dados e previsão de nota de crédito de clientes com IA.
* Dia #3 | [Python Dev](./python_dev/): Chatbot com IA da OpenAI. Estilo ChatGPT.
