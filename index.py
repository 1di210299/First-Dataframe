#Lee el archivo "enaho_preprocesado.xlsx". 
#Cree un dataframe que contenga a los empleados en 
#el sector formal de Lima Metropolitana y la Sierra Norte y que perciban un ingreso 
#mensual mayor o igual al sueldo mínimo establecido por la ley.


import pandas as pd

preprocesado = pd.read_excel('../data/raw/enaho_proprocesado.xlsx')
preprocesado


Lima_sierra_norte = preprocesado[(preprocesado['dominio'] == 'Lima Metropolitana') | 
                                 (preprocesado['dominio'] == 'Sierra Norte') & 
                                 (preprocesado['ingreso_anual_principal']>1025)]

Lima_sierra_norte