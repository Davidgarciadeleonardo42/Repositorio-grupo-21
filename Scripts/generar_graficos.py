import argparse
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from utils_bio import leer_secuencia_fasta

# Clasificación bioquímica
GRUPOS_QUIMICOS = {
    'Apolares (Hidrofóbicos)': 'AVLIMFWP',
    'Polares (Sin carga)': 'STCYNQ',
    'Ácidos (Carga negativa)': 'DE',
    'Básicos (Carga positiva)': 'KRH'
}

def generar_grafico_composicion(secuencia, ruta_salida):
    """Genera y guarda un gráfico de barras con la composición de aminoácidos."""
    conteos = Counter(secuencia)
    estadisticas_grupos = {grupo: 0 for grupo in GRUPOS_QUIMICOS}
    
    for aa, cantidad in conteos.items():
        for grupo, letras_grupo in GRUPOS_QUIMICOS.items():
            if aa in letras_grupo:
                estadisticas_grupos[grupo] += cantidad
                break

    # Configuración del gráfico con Seaborn
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    grupos = list(estadisticas_grupos.keys())
    cantidades = list(estadisticas_grupos.values())
    
    ax = sns.barplot(x=grupos, y=cantidades, palette="viridis", hue=grupos, legend=False)
    
    plt.title('Perfil Químico de la Secuencia Proteica', fontsize=16, pad=15)
    plt.ylabel('Frecuencia Absoluta', fontsize=12)
    plt.xlabel('Grupos Químicos', fontsize=12)
    plt.xticks(rotation=15)
    
    # Añadir las etiquetas de datos sobre cada barra
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=11, color='black', xytext=(0, 5), 
                    textcoords='offset points')

    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=300)
    print(f"Gráfico guardado exitosamente en: {ruta_salida}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera gráficos a partir de una secuencia FASTA.")
    parser.add_argument("archivo_entrada", help="Ruta al archivo FASTA")
    parser.add_argument("archivo_salida", help="Ruta donde guardar la imagen (.png)")
    args = parser.parse_args()

    secuencia = leer_secuencia_fasta(args.archivo_entrada)
    generar_grafico_composicion(secuencia, args.archivo_salida)
