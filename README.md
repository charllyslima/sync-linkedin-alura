# Projeto de Sincronização de Certificados

Este projeto tem como objetivo ajudar a sincronizar os certificados obtidos na plataforma Alura e no LinkedIn para evitar duplicações e gerenciar seu portfólio de certificações de forma eficiente.

## Requisitos

Antes de executar este projeto, você deve ter as seguintes dependências instaladas:

- [Python](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/charllyslima/sync-linkedin-alura
   cd sync-linkedin-alura
   ```

2. Copie o arquivo de exemplo `.env.example` para `.env` e atualize as credenciais com suas informações:

   ```bash
   cp .env.example .env
   ```

   Abra o arquivo `.env` em um editor de texto e insira suas informações de login:

   ```
   ALURA_EMAIL=seu_email_alura@example.com
   ALURA_PASSWORD=sua_senha_alura
   LINKEDIN_EMAIL=seu_email_linkedin@example.com
   LINKEDIN_PASSWORD=sua_senha_linkedin
   ```

3. Crie um ambiente virtual e instale as dependências do projeto a partir do arquivo `requirements.txt`:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Uso

Após configurar o ambiente, você pode executar o projeto. Certifique-se de que o ambiente virtual esteja ativado:

```bash
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Em seguida, execute o arquivo `main.py`:

```bash
python main.py
```

O projeto automatizará o processo de login no Alura e no LinkedIn, bem como a sincronização dos certificados. Certifique-se de verificar o arquivo `README.md` para obter informações adicionais e atualizações.

## Contribuindo

Se você deseja contribuir para este projeto, siga estas diretrizes:

- Este projeto utiliza um ambiente virtual (venv) para gerenciar suas dependências, incluindo o Jupyter Notebook. O Jupyter Notebook já está incluído no ambiente virtual.

- Para editar e desenvolver usando o Jupyter Notebook, siga estas etapas:

  1. Ative o ambiente virtual:
     ```bash
     source venv/bin/activate  # No Windows: venv\Scripts\activate
     ```
  2. Inicie o Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
  3. Abra o notebook `main.ipynb` no navegador e faça as edições necessárias.

- Após concluir as edições no Jupyter Notebook, você pode gerar o arquivo `main.py` a partir do notebook utilizando o comando a seguir no terminal (dentro do ambiente virtual):
  ```bash
  jupyter nbconvert --to script main.ipynb
  ```

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas e solicitações de pull. Seu feedback é valioso!

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).

```

Lembre-se de substituir `seu-usuario` e outros detalhes relevantes pelos seus próprios dados no URL do repositório e nas configurações do `.env`.
```
