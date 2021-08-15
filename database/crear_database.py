import os
import xlrd
import xlwt
import datetime
from operator import itemgetter


def leer_informes(empresa,years,files,ruta):
    empresa_data = []
    data = []
    print('Leyendo datos de ' + empresa)
    for j in range(len(years)):
        print('Año ' + str(years[j]) + ':')
        files[j] = [f for f in files[j] if '~' not in f]
        for f in files[j]:
            try:
                book = xlrd.open_workbook(ruta +'/' + empresa + '/' + years[j] + '/' + f )
                sheet = book.sheet_by_index(0)
                data = [[sheet.cell_value(r+8, c+1) for c in range(sheet.ncols-1)] for r in range(sheet.nrows-8)]
                data = [d for d in data if d[2] != '']
                for row in data:
                    fecha=datetime.datetime(*xlrd.xldate_as_tuple(row[2],book.datemode))
                    row[2]=fecha
                empresa_data.extend(data)
                book.release_resources()
                del book
            except Exception as e:
                print(f + ' : ' + e + '\n') 
    compare = empresa_data.copy()
    for muestra in empresa_data:
        for muestra2 in compare:
            if str(muestra[0]) == str(muestra2[0]) and muestra[1] == muestra2[1] and muestra[6] == muestra2[6] and muestra[12] == muestra2[12] and muestra[2] > muestra2[2]:
                compare.remove(muestra2)
    empresa_data = compare   
    return empresa_data

def write_informes(empresa_data,empresa):
    print('Escribiendo datos...')
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Datos')
    worksheet.write(0,0,label = 'Equipo')
    worksheet.write(0,1,label = 'Componente')
    worksheet.write(0,2,label = 'P.E')
    worksheet.write(0,3,label = 'Ubicacion GAM')
    worksheet.write(0,4,label = 'Estado anterior')
    worksheet.write(0,5,label = 'Visc anterior')
    worksheet.write(0,6,label = 'Visc Max')
    worksheet.write(0,7,label = 'Visc Min')
    worksheet.write(0,8,label = 'ISO Max')
    worksheet.write(0,9,label = 'ISO ant')
    worksheet.write(0,10,label = 'Fecha')
    for l in range(len(empresa_data)):
        worksheet.write(l+1,0, empresa_data[l][1])
        worksheet.write(l+1,1, empresa_data[l][6])
        worksheet.write(l+1,2, empresa_data[l][12])
        worksheet.write(l+1,3, empresa_data[l][0])
        worksheet.write(l+1,4, empresa_data[l][7])
        worksheet.write(l+1,5, empresa_data[l][27])
        worksheet.write(l+1,6, empresa_data[l][25])
        worksheet.write(l+1,7, empresa_data[l][26])
        worksheet.write(l+1,8, empresa_data[l][13])
        worksheet.write(l+1,9, empresa_data[l][14])
        worksheet.write(l+1,10, '%s' % empresa_data[l][2])
    workbook.save(str(os.path.dirname(os.path.realpath(__file__))) + '/database/' + empresa + '.xls' )   
    print('Done!')


empresas = os.listdir('P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+') 
empresas = [e for e in empresas if '.' not in e]
empresas.remove('Clarin')
empresas.remove('Centrales de la Costa')
empresas.remove('Ek Roboter')
empresas.remove('Huincul')
empresas.remove('Las Leñas')
empresas.remove('TENARIS COLOMBIA')
years = []

for e in empresas:
    years.append(os.listdir('P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+/' + e))
    years[empresas.index(e)] = [y for y in years[empresas.index(e)] if os.path.isdir('P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+/' + e + '/' + y)]
temp = []
files = []
for i in  range(0,len(empresas)):
    temp.clear()
    for y in years[i]:
        temp.append(os.listdir('P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+/' + empresas[i] + '/' + y))
    files.append(temp.copy())
    for i in range(len(files)):
        for j in range(len(files[i])):
            for f in files[i][j]:
                if not '.xls' in f:
                    files[i][j].remove(f)
    txt = open('D:/Carga_Portable/database/registro/' + empresas[i] + '.txt','a+')
    try:
        for archivo in files[i][-1]:
            txt.write(archivo+ ',')
        txt.close()
    except Exception as e:
        print(e)    


for e in range(len(empresas)):
    empresa_data = leer_informes(empresas[e],years[e],files[e],'P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+')
    write_informes(empresa_data,empresas[e])
input('press ENTER to EXIT')    
                        

  






