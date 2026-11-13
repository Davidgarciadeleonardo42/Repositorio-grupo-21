# Datos
Esta carpeta contiene datos relevantes para el proyecto: la **secuencia del gen S** y de la **proteína Spike** del **SARS-CoV-2** en formato FASTA (referencia y cinco variantes), además de **metadatos** asociados descargados de NCBI.

Estos datos son comunes y sirven como base para análisis (comparación de las variantes).

## Contenido
| **Archivo** | **Descripción** | **Formato** |
|---|---|---|
| **spike_gen_S_NC_045512.fasta** | Secuencia de nucleótidos del gen S (3822 nt) | FASTA |
| **proteina_Spike_P0DTC2.fasta** | Secuencia de aminoácidos de la proteína Spike de referencia (1273 aa) | FASTA |
| **NOMBRE_ALPHA.fasta** | Secuencia de aminoácidos de la proteína Spike, variante Alpha | FASTA |
| **NOMBRE_BETA.fasta** | Secuencia de aminoácidos de la proteína Spike, variante Beta | FASTA |
| **NOMBRE_GAMMA.fasta** | Secuencia de aminoácidos de la proteína Spike, variante Gamma | FASTA |
| **NOMBRE_DELTA.fasta** | Secuencia de aminoácidos de la proteína Spike, variante Delta | FASTA |
| **NOMBRE_OMICRON.fasta** | Secuencia de aminoácidos de la proteína Spike, variante Omicron | FASTA |
| **data_report.jsonl** | Metadatos del gen S (identificadores, posición, descripción) | JSON Lines |
| **product_report.jsonl** | Informe de la proteína codificada (YP_009724390.1) | JSON Lines |

## Fuente de las secuencias
- **Gen S**: NCBI Datasets, GeneID 43740568. Genoma de referencia NC_045512.2, región 21563-25384.
- **Proteína Spike (referencia)**: UniProt P0DTC2 (SPIKE_SARS2). Su equivalente en NCBI RefSeq es YP_009724390.1.
- **Variante Alpha**: GenBank BFP61150.1
- **Variante Beta**: GenBank XNC78828.1
- **Variante Gamma**: GenBank YBL65226.1
- **Variante Delta**: GenBank YCR25796.1
- **Variante Omicron**: GenBank YGA56012.1
- **Metadatos**: NCBI Datasets, GeneID 43740568.

<sub>***Fecha de descarga: Noviembre de 2026***</sub>