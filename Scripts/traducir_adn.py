import argparse
import sys
from utils_bio import leer_secuencia_fasta

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

def traducir_a_proteina(secuencia_adn):
    proteina = ""
    for i in range(0, len(secuencia_adn) - (len(secuencia_adn) % 3), 3):
        codon = secuencia_adn[i:i+3]
        proteina += CODON_TABLE.get(codon, '?') 
    return proteina

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Traduce una secuencia de ADN a Proteína.")
    parser.add_argument("archivo", help="Ruta al archivo FASTA/TXT")
    args = parser.parse_args()

    # Llamas a la función importada
    adn = leer_secuencia_fasta(args.archivo)
    proteina = traducir_a_proteina(adn)
    
    print(f"Longitud ADN analizado: {len(adn)} pb")
    print(f"Secuencia Proteica Resultante:\n{proteina}")
