import os
import xlrd
import xlwt
import datetime

def leer_informes(empresa,years,files,ruta):
    empresa_data = []
    data = []
    print('Leyendo datos de ' + empresa)
    for j in range(len(years)):
        for f in files:
            book = xlrd.open_workbook(ruta + '/' + empresa + '/' + years[j] + '/' + f )
            sheet = book.sheet_by_index(0)
            data = [[sheet.cell_value(r+8, c+1) for c in range(sheet.ncols-1)] for r in range(sheet.nrows-8)]
            data = [d for d in data if d[2] != '']
            for row in data:
                fecha=datetime.datetime(*xlrd.xldate_as_tuple(row[2],book.datemode))
                row[2]=fecha
            empresa_data.extend(data)
            book.release_resources()
            del book
    compare = empresa_data.copy()
    for muestra in empresa_data:
        for muestra2 in compare:
            if muestra[1] == muestra2[1] and muestra[6] == muestra2[6] and muestra[12] == muestra2[12] and muestra[2] > muestra2[2]:
                compare.remove(muestra2)
    empresa_data = compare
    return empresa_data

now = datetime.datetime.now()
current_year=str(now.year)
ruta = '//sid-01/Laboratorio/2-CALIDAD LABORATORIO/3-Control de informes GAM+'
#ruta = 'P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+'
cy_list = [current_year]



empresas = os.listdir(ruta)
empresas = [e for e in empresas if '.' not in e]
empresas.remove('Clarin')
empresas.remove('Trigalia Molino 3 Arroyos')

for e in empresas:
    
    if os.path.exists(ruta + '/' + e + '/' + current_year):
        new_files = os.listdir(ruta + '/' + e + '/' + current_year)
        new_files = [n for n in new_files if '.xlsx' in n or '.xls' in n]
        txt = open(str(os.path.dirname(os.path.realpath(__file__))) + '/registro/' + e + '.txt','r+')
        existing_files = txt.read().split(',')

        nf_list = []
        for nf in new_files:
            
            append = True    
            for ef in existing_files:
                if nf == ef:
                    append = False
            if append == True:
                txt.write(',' + nf)
                nf_list.append(nf)
              
        if nf_list !=[] :
            print('Agregando ' + str(len(nf_list)) + ' informe(s) a la base de datos de ' + e )         
            append_data = leer_informes(e,cy_list,nf_list,ruta)
            book = xlrd.open_workbook(str(os.path.dirname(os.path.realpath(__file__))) + '/database/' + e + '.xls')
            sheet = book.sheet_by_index(0)
            data  = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
            data.remove(data[0])
            for row in data:    
                date_time_obj = datetime.datetime.strptime(row[10], '%Y-%m-%d %H:%M:%S')
                row[10]=date_time_obj
            for r in append_data:
                for d in data:
                    if r[1] == d[0] and r[6] == d[1] and r[12] == d[2] and r[0] == d[3]:
        
                        if r[2] > d[10]:
                            data.remove(d)
            book.release_resources()
            del book
        
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
            for d in  range(len(data)):
                worksheet.write(d+1,0, data[d][0])
                worksheet.write(d+1,1, data[d][1])
                worksheet.write(d+1,2, data[d][2])
                worksheet.write(d+1,3, data[d][3])
                worksheet.write(d+1,4, data[d][4])
                worksheet.write(d+1,5, data[d][5])
                worksheet.write(d+1,6, data[d][6])
                worksheet.write(d+1,7, data[d][7])
                worksheet.write(d+1,8, data[d][8])
                worksheet.write(d+1,9, data[d][9])
                worksheet.write(d+1,10, '%s' % data[d][10])
            for r in range(len(append_data)):
                worksheet.write(len(data)+1+r,0, append_data[r][1])
                worksheet.write(len(data)+r+1,1, append_data[r][6])
                worksheet.write(len(data)+r+1,2, append_data[r][12]) 
                worksheet.write(len(data)+r+1,3, append_data[r][0])  
                worksheet.write(len(data)+r+1,4, append_data[r][7])
                worksheet.write(len(data)+r+1,5, append_data[r][27])
                worksheet.write(len(data)+r+1,6, append_data[r][25])
                worksheet.write(len(data)+r+1,7, append_data[r][26])
                worksheet.write(len(data)+r+1,8, append_data[r][13])
                worksheet.write(len(data)+r+1,9, append_data[r][14])
                worksheet.write(len(data)+r+1,10, '%s' % append_data[r][2])
            workbook.save(str(os.path.dirname(os.path.realpath(__file__))) + '/database/' + e + '.xls')
input('Presione ENTER para SALIR')                 










