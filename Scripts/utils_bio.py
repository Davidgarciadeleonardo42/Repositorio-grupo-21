import sys

def leer_secuencia_fasta(ruta_archivo):
    """Lee un archivo FASTA o TXT, omitiendo la cabecera y limpiando la secuencia."""
    secuencia = ""
    try:
        with open(ruta_archivo, 'r') as file:
            for linea in file:
                linea = linea.strip()
                if linea.startswith(">"):
                    continue
                secuencia += linea.replace(' ', '').upper()
        return secuencia
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        sys.exit(1)
