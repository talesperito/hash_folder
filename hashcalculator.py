import os
import hashlib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_file_hash(file_path):


    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(8192): 
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except (IOError, OSError) as e:
        logging.error(f"Erro ao processar {file_path}: {e}")
        return None

def generate_file_hashes(folder_path, output_csv_path):
        
    
    if not os.path.exists(folder_path):
        logging.error(f"Erro: A pasta {folder_path} não existe.")
        return

    file_hashes = []
    ignored_files = {"desktop.ini"}

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            
            if filename.startswith(".") or filename in ignored_files:
                continue
            
            file_hash = calculate_file_hash(file_path)
            if file_hash:  # Ignora arquivos com erro de hash
                file_hashes.append((filename, file_hash))
                logging.info(f"Arquivo processado: {filename}, Hash: {file_hash}")


    hash_df = pd.DataFrame(file_hashes, columns=['Nome do Arquivo', 'Hash SHA-256'])
    hash_df.to_csv(output_csv_path, index=False, sep=';')
    logging.info(f"\nHashes salvos em: {output_csv_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calcula hashes SHA-256 de arquivos em uma pasta.")
    parser.add_argument("folder_path", help="Caminho da pasta com os arquivos.")
    parser.add_argument("output_csv_path", help="Caminho para salvar o CSV de saída.")
    args = parser.parse_args()

    generate_file_hashes(args.folder_path, args.output_csv_path)
