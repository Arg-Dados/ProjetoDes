import subprocess

def main():
    print("Iniciando o processo de ingestão de dados...")
    subprocess.run(["python3", "scripts/run_ingestion.py"])

    print("Iniciando o processo de processamento de dados...")
    subprocess.run(["python3", "scripts/run_processing.py"])

    print("Processo completo.")

if __name__ == '__main__':
    main()
