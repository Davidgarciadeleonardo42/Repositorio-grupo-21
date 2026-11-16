import argparse
import sys

# Diccionario codones
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_'
}

def leer_secuencia(ruta_archivo):
    """Lee el archivo txt y limpia la secuencia."""
    try:
        with open(ruta_archivo, 'r') as file:
            secuencia = file.read().replace('\n', '').replace(' ', '').upper()
            return secuencia
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        sys.exit(1)

def traducir_a_proteina(secuencia_adn):
    """Traduce la secuencia de ADN a proteína asumiendo el marco de lectura +1."""
    proteina = ""
    for i in range(0, len(secuencia_adn) - (len(secuencia_adn) % 3), 3):
        codon = secuencia_adn[i:i+3]
        proteina += CODON_TABLE.get(codon, '?') # '?' si hay nucleótidos ambiguos (N)
    return proteina

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traduce una secuencia de ADN a Proteína.")
    parser.add_argument("archivo", help="Ruta al archivo TXT con la secuencia de ADN")
    args = parser.parse_args()

    adn = leer_secuencia(args.archivo)
    proteina = traducir_a_proteina(adn)
    
    print(f"Longitud ADN: {len(adn)} pb")
    print(f"Secuencia Proteica Resultante:\n{proteina}")
