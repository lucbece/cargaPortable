import os
import xlrd
import xlwt
import datetime

def strip_right(text, suffix):
    if not text.endswith(suffix):
        return text
    # else
    return text[:len(text)-len(suffix)]

def leer_informes(years,files):
    empresa_data = []
    data = []
    print('Leyendo datos de Clarin')
    for j in range(len(years)):
        print('Año' + str(years[j]) + ':')
        files[j] = [f for f in files[j] if '~' not in f and '.xls' in f]
        for f in files[j]:
            
            book = xlrd.open_workbook('P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+/Clarin/' + years[j] + '/' + f )
            sheet = book.sheet_by_index(0)
            data = [[sheet.cell_value(r+5,c) for c in range(sheet.ncols)] for r in range(sheet.nrows -8)]
            data = [d for d in data if  d[0] != '' and d[0] != 'Limites']
            for d in data:
                fdate = strip_right(f,'.xls')
            
                d.append(fdate)
                
            empresa_data.extend(data)
            book.release_resources()
            del book
          
    for rename in empresa_data:
        if 'UNIDAD' in rename[0]:
            rename[0].replace('UNIDAD','Unidad')
        if 'unidad' in rename[0].lower():
            if '8a' in rename[0].lower():
                rename[0] = 'Doblador 1 (8A)'
            elif '13a' in rename[0].lower():
                rename[0] = 'Doblador 2 (13A)'
            elif '18a' in rename[0].lower():
                rename[0] = 'Doblador 3 (18A)'
            elif '23a' in rename[0].lower():
                rename[0] = 'Doblador 4 (23A)'
            elif '28a' in rename[0].lower():
                rename[0] = 'Doblador 5 (28A)'
        if 'CENTRAL' in rename[0]:
            rename[0].replace('CENTRAL','Central')        
        if 'central h' in rename[0].lower():
            split = rename[0].split(' ')
            rename[0] = 'Central ' + str(split[-1])
        if 'doblador' in rename[0].lower():
            split2 = rename[0].split(' ')
            if split2[-1].lower() == '8a' or split2[-1] == '8' :
                split2[-1] = '1 (8A)'
                rename[0] = 'Doblador ' + split2[-1]
            elif split2[-1].lower() == '13a':
                split2[-1] = '2 (13A)'
                rename[0] = 'Doblador ' + split2[-1]
            elif split2[-1].lower() == '18a':
                split2[-1] = '3 (18A)'
                rename[0] = 'Doblador ' + split2[-1]
            elif split2[-1].lower() == '23a':
                split2[-1] = '4 (23A)'
                rename[0] = 'Doblador ' + split2[-1]
            elif split2[-1].lower() == '28a':
                split2[-1] = '5 (28A)'
                rename[0] = 'Doblador ' + split2[-1]
        if 'un ' in rename[0].lower():
            rename[0] = rename[0].replace('UN', 'Unidad')


    compare = empresa_data.copy()
    for muestra in empresa_data:

        for muestra2 in compare:

            date1 = datetime.datetime.strptime(str(muestra[-1]), '%Y-%m-%d').date()
            date2 = datetime.datetime.strptime(str(muestra2[-1]), '%Y-%m-%d').date()

            if str(muestra[0]) == str(muestra2[0]) and date1 > date2:
                compare.remove(muestra2)
    empresa_data = compare
    return empresa_data

def write_informes(empresa_data):
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
        worksheet.write(l+1,0, empresa_data[l][0])
        worksheet.write(l+1,1, '-')
        worksheet.write(l+1,2, '-')
        worksheet.write(l+1,3, '-')
        worksheet.write(l+1,4, empresa_data[l][15])
        worksheet.write(l+1,5, empresa_data[l][4])
        worksheet.write(l+1,6,'-')
        worksheet.write(l+1,7,'-')
        worksheet.write(l+1,8,'-')
        worksheet.write(l+1,9,'-')
        worksheet.write(l+1,10, '%s' % empresa_data[l][-1])
    print('Done!')    
    workbook.save(str(os.path.dirname(os.path.realpath(__file__))) + '/database/Clarin.xls' )


    
years = ['2017', '2018', '2019']
files = []
for y in years:
    ext = os.listdir('P:/2-CALIDAD LABORATORIO/3-Control de informes GAM+/Clarin/' + y)
    files.append(ext)

write_informes(leer_informes(years,files))

input('press ENTER to EXIT')