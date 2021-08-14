import GUI
import Global_Data
import wx
import os
import re
import datetime

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def date_converter(date):
    assert isinstance(date, wx.DateTime)
    if date.IsValid():
        ymd = map(int, date.FormatISODate().split('-'))
        return datetime.date(*ymd)
    else:
        return None    

class MainFrame(GUI.MainFrame):
    def __init__(self,parent):
        GUI.MainFrame.__init__(self,parent)
        
    def nueva_empresa(self, event):
        empresamsg.Show(True)        

class MainPanel(GUI.MainPanel):
    def __init__(self,parent):
        GUI.MainPanel.__init__(self,parent)        
        self.Empresas.SetItems(Global_Data.initialize())
        self.AutoComplete_Entry.AutoComplete(MyClassCompleter())
        
    def select_database(self,event):
        self.empresas_int = self.Empresas.GetCurrentSelection()
        lista_muestras = Global_Data.pick_database(self.empresas_int)
        lista_muestras.sort(key = natural_keys)
        self.muestras_pick.Clear()

        for i in range(len(lista_muestras)):
            self.muestras_pick.Append(lista_muestras[i])

    def S_check_event(self,event):
        self.TA_Completas.SetValue(False)
        self.TA_Ambas.SetValue(False)

    def C_check_event(self,event):
        self.TA_Simples.SetValue(False)
        self.TA_Ambas.SetValue(False)

    def SyC_check_event(self,event):
        self.TA_Simples.SetValue(False)
        self.TA_Completas.SetValue(False)

    def agregar_equipo(self,event):
        muestra = self.muestras_pick.GetValue()
        self.Muestras.AppendText(muestra + '\n')
        self.muestras_pick.SetValue('')

    def add_muestra(self,event):
        muestra = self.AutoComplete_Entry.GetValue()
        self.Muestras.AppendText(muestra + '\n')
        self.AutoComplete_Entry.SetValue('')    

    def data_entry(self,event):
        RAW_Muestras = self.Muestras.GetValue().split('\n')
        #Agrega un check para ver si hay muestras repetidas
        repetidas = []
        for i in range(len(RAW_Muestras)):
            for j in range(len(RAW_Muestras)):
                if RAW_Muestras[i] == RAW_Muestras[j] and i != j:
                    repetidas.append(RAW_Muestras[i])
        repetidas = list(dict.fromkeys(repetidas))            

        if len(repetidas) >> 0:
            for i in range(len(repetidas)):    
                errormsg.textCtrl_Error.AppendText(repetidas[i] + '\n')
            errormsg.Show(True)
            return

        for muestra in RAW_Muestras:
            if muestra == '':
                RAW_Muestras.remove(muestra)                      

        CDM = len(RAW_Muestras)
        Empresa_INT = self.Empresas.GetCurrentSelection()
        Empresa = Global_Data.empresas_list[Empresa_INT]
        Fecha = str(date_converter(self.date_picker.GetValue()))
        

        if self.TA_Simples.GetValue() == True :
            Muestras_list = []
            TA = self.TAS_Simples.GetValue()
            if self.manual_order.GetValue() == False:
                ORDERED_Muestras = RAW_Muestras.copy()
                ORDERED_Muestras.sort(key=natural_keys)
                for i in range (0,CDM):
                    Muestras_list.append([ORDERED_Muestras[i],TA])
            else:
                for i in range (0,CDM):
                    Muestras_list.append([RAW_Muestras[i],TA])        

            Global_Data.EXCEL_carga(Empresa, CDM, Muestras_list, Fecha)    

        elif self.TA_Completas.GetValue() == True:
            TA = self.TAS_Completas.GetValue()
            Muestras_list = []
            Hmany = CDM
            if self.manual_order.GetValue() == False:    
                ORDERED_Muestras = RAW_Muestras.copy()
                ORDERED_Muestras.sort(key=natural_keys)
            
                for i in range (0,CDM):
                    Muestras_list.append([ORDERED_Muestras[i],TA])
            else:
                for i in range(0,CDM):
                    Muestras_list.append([RAW_Muestras[i],TA])

            Global_Data.EXCEL_carga(Empresa, CDM, Muestras_list, Fecha)
            Global_Data.EXCEL_visco(Empresa, CDM, Muestras_list, Fecha, Hmany)        

        elif self.TA_Ambas.GetValue() == True :
            TAC = self.TAS_Completas.GetValue()
            TAS = self.TAS_Simples.GetValue()
            Rango_Completas = int(self.TA_Entry.GetValue())
            Muestras_Simples = []
            Muestras_Completas = []
            for i in range (0,Rango_Completas):
                Muestras_Completas.append(RAW_Muestras[i])
            for j in range (Rango_Completas,CDM):
                Muestras_Simples.append(RAW_Muestras[j])
                
            if self.manual_order.GetValue() == False:    
                Muestras_Completas.sort(key=natural_keys)
                Muestras_Simples.sort(key=natural_keys)    

            Muestras_list = []
            for i in range (0,Rango_Completas):        
                Muestras_list.append([Muestras_Completas[i],TAC])
            for j in range (0,len(Muestras_Simples)):
                Muestras_list.append([Muestras_Simples[j],TAS])    
            

            Global_Data.EXCEL_carga(Empresa, CDM, Muestras_list, Fecha)
            Global_Data.EXCEL_visco(Empresa, CDM, Muestras_list, Fecha, Rango_Completas)

        int_list =Global_Data.numerar_list(RAW_Muestras,Muestras_list)
        nummsg.textCtrl_dialog.Clear()
        nummsg.add_muestras(RAW_Muestras,int_list)
        nummsg.Show(True)
                                        
    def clear_input(self,event):
        self.Muestras.Clear()
        self.TA_Entry.Clear()

    def open_carga(self,event):
        os.startfile(Global_Data.rutaOUT + 'Para carga/Midiendo')

    def open_visco(self,event):
        os.startfile(Global_Data.rutaOUT + 'Calculo de Viscosidad/Midiendo')

    def create_empresa(self,event):
        empresamsg.Show(True)

    def update_list(self):
        self.Empresas.SetItems(Global_Data.initialize())

class ErrorDiag(GUI.dialog_Error):
    def __init__(self,parent):
        GUI.dialog_Error.__init__(self,parent)

    def close_error(self,event):
        self.textCtrl_Error.Clear()
        errormsg.Show(False)    

class NumDiag(GUI.dialog_Numeracion):
    def __init__(self,parent):
        GUI.dialog_Numeracion.__init__(self,parent)

    def add_muestras(self,raw_list,int_list):
        for i in range(len(raw_list)):
            self.textCtrl_dialog.AppendText(str(int_list[i]) + '-  ' + raw_list[i] + '\n')   


class NempDiag(GUI.dialog_NuevaEmpresa):
    def __init__(self,parent):
        GUI.dialog_NuevaEmpresa.__init__(self,parent)

    def append_empresa(self,event):
        new_empresa = self.text_NuevaEmpresa.GetValue()
        Global_Data.add_empresa(new_empresa)
        panel.update_list()
        empresamsg.Show(False)

    def close(self,event):
        self.text_NuevaEmpresa.Clear()
        empresamsg.Show(False)    

class MyClassCompleter(wx.TextCompleter):
    def __init__(self):
        wx.TextCompleter.__init__(self)
        self._iLastReturned = wx.NOT_FOUND
        self._sPrefix = ''
    def Start(self, prefix):
        self._sPrefix = prefix.lower()
        self._iLastReturned = wx.NOT_FOUND
        self.pool = Global_Data.pick_database(panel.empresas_int)
        for item in self.pool:
            if item.lower().startswith(self._sPrefix):
                return True
        # Nothing found
        return False

    def GetNext(self):
        for i in range(self._iLastReturned+1, len(self.pool)):
            if self.pool[i].lower().startswith(self._sPrefix):
                self._iLastReturned = i
                return self.pool[i]
        # No more corresponding item
        return ''

    

app = wx.App(False)
frame = MainFrame(None)
frame.Show(True)
panel = MainPanel(frame)
panel.Show(True)
errormsg = ErrorDiag(None)
errormsg.Show(False)
nummsg = NumDiag(None)
nummsg.Show(False)
empresamsg = NempDiag(None)
empresamsg.Show(False)
app.MainLoop()
