
import requests
import pandas as pd
from validate_docbr import CPF
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_URL = "https://api.sistemajuridico.com/usuarios"  # Substitua pela URL real da API
cpf_validator = CPF()

def validar_cpf(cpf):
    """Valida CPF usando biblioteca validate-docbr"""
    return cpf_validator.validate(str(cpf))

def atualizar_usuario(usuario):
    """Envia os dados do usuário para a API se o CPF for válido"""
    if not validar_cpf(usuario['cpf']):
        logging.warning(f"CPF inválido para usuário {usuario['nome']}")
        return False

    try:
        response = requests.post(API_URL, json=usuario)

        if response.status_code == 200:
            logging.info(f"Usuário {usuario['nome']} atualizado com sucesso.")
            return True
        elif response.status_code == 400:
            logging.error(f"Erro de validação para {usuario['nome']}: {response.json()}")
            return False
        else:
            logging.error(f"Erro ao atualizar {usuario['nome']}: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        logging.exception(f"Exceção ao atualizar {usuario['nome']}: {e}")
        return False

def main():
    try:
        df = pd.read_excel('usuarios.xlsx')
    except FileNotFoundError:
        logging.error("Arquivo 'usuarios.xlsx' não encontrado.")
        return

    # Verificar se colunas obrigatórias existem
    campos_esperados = ['nome', 'cpf', 'email']
    for campo in campos_esperados:
        if campo not in df.columns:
            logging.error(f"Coluna obrigatória '{campo}' não encontrada no Excel.")
            return

    sucesso = 0
    falha = 0

    for _, row in df.iterrows():
        usuario = row.to_dict()
        if atualizar_usuario(usuario):
            sucesso += 1
        else:
            falha += 1

    logging.info(f"Processamento finalizado: {sucesso} sucesso(s), {falha} falha(s).")

if __name__ == "__main__":
    main()
