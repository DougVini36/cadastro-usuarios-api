
# 📥 Cadastro Automático de Usuários via API

Automação em Python para envio de dados de usuários (nome, CPF e e-mail) a uma API de sistema jurídico a partir de um arquivo Excel.

## 🚀 Funcionalidades

- Validação real de CPF com `validate-docbr`
- Leitura de planilhas Excel com `pandas`
- Envio dos dados para uma API REST
- Registro de sucesso ou falha para cada envio
- Planilha de exemplo incluída

## 🛠️ Tecnologias utilizadas

- Python 3.x
- pandas
- requests
- openpyxl
- validate-docbr

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/cadastro-usuarios-api.git
cd cadastro-usuarios-api
pip install -r requirements.txt
```

## 🧪 Como usar

1. Edite o arquivo `usuarios.xlsx` com os dados dos usuários (colunas: `nome`, `cpf`, `email`)
2. Execute o script:

```bash
python cadastrar_usuarios.py
```

3. Acompanhe o log no terminal sobre os usuários cadastrados com sucesso ou falha.

## 📄 Exemplo de planilha

| nome        | cpf         | email               |
|-------------|-------------|---------------------|
| João Silva  | 12345678901 | joao@example.com    |
| Maria Souza | 98765432100 | maria@example.com   |

---

## 📬 Contato

Projeto por [Seu Nome](https://www.linkedin.com/in/seu-perfil).  
Em caso de dúvidas ou contribuições, entre em contato!
