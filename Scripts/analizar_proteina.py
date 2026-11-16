import argparse
import sys
from collections import Counter
from utils_bio import leer_secuencia_fasta

# Clasificación bioquímica estándar de los aminoácidos
GRUPOS_QUIMICOS = {
    'Apolares (Hidrofóbicos)': 'AVLIMFWP',
    'Polares (Sin carga)': 'STCYNQ',
    'Ácidos (Carga negativa)': 'DE',
    'Básicos (Carga positiva)': 'KRH'
}

def analizar_secuencia(secuencia):
    """Calcula estadísticas y propiedades químicas de la secuencia peptídica."""
    longitud = len(secuencia)
    if longitud == 0:
        print("Error: La secuencia proporcionada está vacía.")
        sys.exit(1)

    # Conteo absoluto de cada aminoácido
    conteos = Counter(secuencia)
    
    # Agrupación por propiedades químicas
    estadisticas_grupos = {grupo: 0 for grupo in GRUPOS_QUIMICOS}
    
    for aa, cantidad in conteos.items():
        for grupo, letras_grupo in GRUPOS_QUIMICOS.items():
            if aa in letras_grupo:
                estadisticas_grupos[grupo] += cantidad
                break
                
    # Imprimir reporte
    print(f"{"="*40}")
    print(f"ANÁLISIS DE PERFIL PROTEICO")
    print(f"{"="*40}")
    print(f"Longitud total: {longitud} aminoácidos\n")
    
    print("[+] Composición por grupos químicos:")
    for grupo, cantidad in estadisticas_grupos.items():
        porcentaje = (cantidad / longitud) * 100
        print(f"    - {grupo}: {cantidad} ({porcentaje:.2f}%)")
        
    print("\n[+] Top 5 Aminoácidos más frecuentes:")
    for aa, cantidad in conteos.most_common(5):
        porcentaje = (cantidad / longitud) * 100
        print(f"    - {aa}: {cantidad} ({porcentaje:.2f}%)")
    print(f"{"="*40}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analiza las propiedades químicas de una secuencia proteica.")
    parser.add_argument("archivo", help="Ruta al archivo FASTA con la secuencia de la proteína")
    args = parser.parse_args()

    # Se reutiliza el lector modular para ignorar las cabeceras '>' del FASTA
    secuencia_proteina = leer_secuencia_fasta(args.archivo)
    
    # Validar que no contenga nucleótidos puros por error (opcional pero recomendado)
    if set(secuencia_proteina).issubset({'A', 'T', 'C', 'G', 'N'}):
        print("Advertencia: La secuencia parece ser ADN, no una proteína traducida.")
        
    analizar_secuencia(secuencia_proteina)
