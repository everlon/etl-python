import pandas as pd
import os, glob
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_excel_files(folder_path):
    """
    Retorna uma lista de caminhos de arquivos Excel na pasta especificada.

    Parameters:
    folder_path (str): Caminho para a pasta contendo os arquivos Excel.

    Returns:
    list: Lista de caminhos de arquivos Excel.
    """
    return glob.glob(os.path.join(folder_path, '*.xlsx'))

def process_file(excel_file):
    """
    Processa um único arquivo Excel e retorna um DataFrame.

    Parameters:
    excel_file (str): Caminho para o arquivo Excel.

    Returns:
    pd.DataFrame: DataFrame com os dados processados do arquivo.
    """
    try:
        df = pd.read_excel(excel_file)
        file_name = os.path.basename(excel_file)
        df['filename'] = file_name

        if 'brasil' in file_name.lower():
            df['location'] = 'br'
        elif 'france' in file_name.lower():
            df['location'] = 'fr'
        elif 'italian' in file_name.lower():
            df['location'] = 'it'

        df['campaign'] = df['utm_link'].str.extract(r'utm_campaign=(.*)')

        return df

    except Exception as e:
        logging.error(f"Erro ao ler o arquivo {excel_file}: {e}")
        return None

def save_to_excel(dfs, output_file):
    """
    Salva uma lista de DataFrames em um único arquivo Excel.

    Parameters:
    dfs (list): Lista de DataFrames a serem concatenados e salvos.
    output_file (str): Caminho para o arquivo Excel de saída.
    """
    if dfs:
        result = pd.concat(dfs, ignore_index=True)
        result.to_excel(output_file, index=False, engine="xlsxwriter")
        logging.info(f"Arquivo salvo com sucesso em: {output_file}")
    else:
        logging.info("Sem dados para a Data-Ready.")

def main(folder_path, output_file):
    """
    Função principal para processar arquivos Excel em uma pasta e salvar o resultado em um único arquivo Excel.

    Parameters:
    folder_path (str): Caminho para a pasta contendo os arquivos Excel.
    output_file (str): Caminho para o arquivo Excel de saída.
    """
    excel_files = get_excel_files(folder_path)

    if not excel_files:
        logging.info("Nenhum arquivo de planilha encontrado.")
        return

    dfs = [process_file(file) for file in excel_files if process_file(file) is not None]
    save_to_excel(dfs, output_file)

if __name__ == "__main__":
    folder_path = 'src/data/raw'
    output_file = os.path.join("src", "data", "ready", "dataready_file.xlsx")
    main(folder_path, output_file)
