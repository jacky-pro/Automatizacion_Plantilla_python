import pandas as pd
import csv

file_path = r'C:\\Users\\JackelinNuñezAguirre\\Documents\\Prueba_1\\BASE_Lima_reporte_sbp_dxp_abril_Interna1 _ivr.csv'
df = pd.read_csv(file_path, sep=';', encoding='latin-1')
df.columns = df.columns.str.strip()

df['Fecha Nacimiento'] = pd.to_datetime(df['Fecha Nacimiento'], format='%d/%m/%Y', errors='coerce')
current_year = pd.to_datetime('today').year
edad = current_year - df['Fecha Nacimiento'].dt.year

# Limpiar la columna de documentos
df['ï»¿Documento'] = pd.to_numeric(df['ï»¿Documento'], errors='coerce').astype('Int64')
df['NUMERO DOCUMENTO'] = df['ï»¿Documento'].fillna(0).astype(int).astype(str).str.zfill(8)

df_output = pd.DataFrame({
    'DECIL': 10,
    'RUC': df['RUC_Validata'],
    'RAZON SOCIAL': df['Razon Social_Validata'],
    'TIPO CLIENTE': None,
    'NUMERO DOCUMENTO': df['NUMERO DOCUMENTO'],
    'PRIMER NOMBRE': df['Nombre_Completo'],
    'SEGUNDO NOMBRE': None,
    'PRIMER APELLIDO': None,
    'SEGUNDO APELLIDO': None,
    'EDAD': edad,
    'CORREO': None,
    'CELULAR1': df['Numero1'],
    'CELULAR2': df['Numero2'],
    'CELULAR3': df['Numero3'],
    'TELEFONO1': None,
    'TELEFONO2': None,
    'TELEFONO3': None,
    'FLAG AUTORIZACION': None,
    'FLAG CUENTA SUELDO': None,
    'OFERTA COMPRA DEUDA': None,
    'OFERTA CASH': None,
    'RCC SALDO TOTAL': None,
    'RCC SALDO TOTAL CONSUMO': df['SCOTIABANK_DEUDA_TOTAL'],
    'RCC SALDO TC': df['Total Lineas TC'],
    'RCC SALDO LD': df['SBP_PRESTAMO'],
    'RCC SALDO DXP': df['SBP_CONVENIO'],
    'RCC SALDO BBVA TC': None,
    'RCC SALDO BBVA PP': None,
    'RCC SALDO IBK TC': None,
    'RCC SALDO IBK PP': None,
    'RCC SALDO BCP TC': None,
    'RCC SALDO BCP PP': None,
    'RCC SALDO GNB TC': None,
    'RCC SALDO GNB PP': None,
    'RCC SALDO PICHINCHA TC': None,
    'RCC SALDO PICHINCHA PP': None,
    'RCC SALDO BNACION TC': None,
    'RCC SALDO BNACION PP': None,
    'RCC SALDO BCOMERCIO TC': None,
    'RCC SALDO BCOMERCIO PP': None,
    'COLOR': df['COLOR_DXP_Filtro_A_top'],
    'DIRECCION': None,
    'DISTRITO': None,
    'PROVINCIA': None,
    'DEPARTAMENTO': None,
    'ESTRATEGIA': None,
    'RANGO SALDO CONSUMO': None,
    'ENTIDAD A COMPRAR': None,
    'REQUISITO': None,
    'CAMPAÑA': None,
    'CANAL': None,
    'REPROGRAMADOS': None,
    'FLAG RECURRENTE': None,
    'FLAG APLICA CD': None,
    'MONTO ORIGINAL': None,
    'SALDO': None,
    'TOTAL CUOTAS': None,
    'CUOTAS VENCIDAS': None,
    'CUOTAS FALTANTES': None,
    'CUOTAS PAGADAS': None,
    'TASA': None,
    'RCI': None,
    'TERRITORIO': None,
    'UBIGEO': None,
    'TIPO BASE': None,
    'JEFE DE VENTAS': None,
    'GRUPOCONTACTABILIDAD': None,
    'PERFIL_LD': None,
    'TIPO_REGULAR_DESPLIEGUE': None,
    'FLAGLIMAPROVINCIA': None
})

df_output.to_csv('output.csv', index=False, sep=';', encoding='utf-8-sig', quoting=csv.QUOTE_ALL, escapechar='\\')  # type: ignore
