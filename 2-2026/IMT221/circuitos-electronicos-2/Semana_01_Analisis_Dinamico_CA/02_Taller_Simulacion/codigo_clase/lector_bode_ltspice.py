"""
Circuitos Electrónicos II (IMT-221) - UCB Tarija
Script de Limpieza y Visualización de Diagramas de Bode desde LTSpice
Docente: M.Sc. Ing. Bernardo Quiroga Turdera

Descripción:
Este script importa el archivo de texto exportado por el comando .ac de LTSpice,
limpia la sintaxis de caracteres no numéricos (dB, °, paréntesis) y grafica 
la respuesta en frecuencia utilizando el estándar de calidad de publicación.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# 1. Configuración inicial
# Asegúrate de que el archivo TXT de LTSpice esté en la misma carpeta que este script
ARCHIVO_LTSPICE = 'ltspice_export.txt'

def limpiar_columna_compleja(celda):
    """
    Función para extraer Magnitud y Fase de la celda de texto de LTSpice.
    Ejemplo de celda entrante: '(-3.0103dB,-45.0001°)'
    Retorna una tupla de flotantes: (-3.0103, -45.0001)
    """
    if isinstance(celda, str):
        # Utiliza expresiones regulares para extraer los números
        numeros = re.findall(r"[-+]?\d*\.\d+|\d+", celda)
        if len(numeros) >= 2:
            return float(numeros[0]), float(numeros[1])
    return np.nan, np.nan

try:
    # 2. Cargar los datos tabulares de LTSpice
    print("[*] Cargando datos desde LTSpice...")
    df = pd.read_csv(ARCHIVO_LTSPICE, sep='\t', encoding='utf-8')
    
    # Obtener nombres de las columnas reales
    col_freq = df.columns[0]
    col_vout = df.columns[1]
    
    # 3. Limpieza de datos (Data Cleaning)
    print("[*] Limpiando caracteres de ingeniería...")
    # Aplicar la función de limpieza a la columna de salida
    df[['Magnitud_dB', 'Fase_deg']] = df.apply(
        lambda row: limpiar_columna_compleja(row[col_vout]), 
        axis=1, 
        result_type='expand'
    )
    
    # 4. Creación del Gráfico de Bode Profesional (Estilo IEEE)
    print("[*] Generando gráfico de Bode...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    
    # Subplot de Magnitud
    ax1.semilogx(df[col_freq], df['Magnitud_dB'], color='b', linewidth=2, label='V(out)')
    ax1.set_ylabel('Magnitud [dB]', fontweight='bold')
    ax1.set_title('Diagrama de Bode - Red RC Paso-Bajo', fontweight='bold')
    ax1.grid(True, which="both", ls="--", alpha=0.7)
    
    # Marcar el punto de corte de -3dB (aprox 1.59 kHz para R=1k, C=100n)
    ax1.axhline(y=-3.01, color='r', linestyle=':', label='-3 dB (Frec. de Corte)')
    ax1.legend()

    # Subplot de Fase
    ax2.semilogx(df[col_freq], df['Fase_deg'], color='g', linewidth=2)
    ax2.set_ylabel('Fase [Grados]', fontweight='bold')
    ax2.set_xlabel('Frecuencia [Hz]', fontweight='bold')
    ax2.grid(True, which="both", ls="--", alpha=0.7)
    
    # Marcar los -45 grados teóricos
    ax2.axhline(y=-45.0, color='r', linestyle=':', label='-45°')
    ax2.legend()
    
    # Ajustar layout y mostrar
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"[ERROR] No se encontró el archivo '{ARCHIVO_LTSPICE}'.")
    print("Asegúrate de exportar los datos desde LTSpice en la misma carpeta del script.")
except Exception as e:
    print(f"[ERROR INESPERADO] Ocurrió un fallo en la ejecución: {e}")