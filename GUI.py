# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.adv

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ID Ingeniería - Carga de Muestras", pos = wx.DefaultPosition, size = wx.Size( 649,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.menu = wx.MenuBar( 0 )
		self.menu_empresa = wx.Menu()
		self.crear_empresa = wx.MenuItem( self.menu_empresa, wx.ID_ANY, u"Nueva empresa", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_empresa.Append( self.crear_empresa )
		
		self.menu.Append( self.menu_empresa, u"Empresas" )
		self.Bind(wx.EVT_MENU, self.nueva_empresa, self.crear_empresa) 
		
		def nueva_empresa(self,event):
			event.Skip()
			
		self.help_menu = wx.Menu()
		self.manual = wx.MenuItem( self.help_menu, wx.ID_ANY, u"Manual de usuario", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.manual )
		
		self.menu.Append( self.help_menu, u"Ayuda" ) 
		
		self.SetMenuBar( self.menu )
		
		
		self.Centre( wx.BOTH )

	
	def __del__( self ):
		pass
	
class MainPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 641,445 ), style = wx.TAB_TRAVERSAL )
		
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		MAIN_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.Titulo = wx.StaticText( self, wx.ID_ANY, u"Carga de Muestras", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Titulo.Wrap( -1 )
		self.Titulo.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		MAIN_bSizer.Add( self.Titulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.line_hor1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MAIN_bSizer.Add( self.line_hor1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Empresa1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Empresa = wx.StaticText( self, wx.ID_ANY, u"Empresa", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ALIGN_LEFT )
		self.Empresa.Wrap( -1 )
		self.Empresa.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		Empresa1.Add( self.Empresa, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		EmpresasChoices = []
		self.Empresas = wx.Choice( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 300,-1 ), EmpresasChoices)
		self.Empresas.SetSelection( 0 )
		self.Empresas.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
		
		Empresa1.Add( self.Empresas, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )
		
		
		MAIN_bSizer.Add( Empresa1, 0, wx.EXPAND, 5 )
		
		Fecha1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Fecha = wx.StaticText( self, wx.ID_ANY, u"Fecha de Extraccion", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ALIGN_LEFT )
		self.Fecha.Wrap( -1 )
		self.Fecha.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		Fecha1.Add( self.Fecha, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.date_picker = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 300,30 ), wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		self.date_picker.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		Fecha1.Add( self.date_picker, 0, wx.ALL, 5 )
		
		
		MAIN_bSizer.Add( Fecha1, 0, wx.EXPAND, 5 )
		
		TA = wx.BoxSizer( wx.HORIZONTAL )
		
		self.TA_Simples = wx.CheckBox( self, wx.ID_ANY, u"Simples", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TA_Simples.SetValue(False) 
		self.TA_Simples.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		TA.Add( self.TA_Simples, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.TAS_Simples = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SP_ARROW_KEYS, 1, 2, 1 )
		TA.Add( self.TAS_Simples, 0, wx.ALL, 5 )
		
		self.TA_Completas = wx.CheckBox( self, wx.ID_ANY, u"Completas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TA_Completas.SetValue(True) 
		self.TA_Completas.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		TA.Add( self.TA_Completas, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.TAS_Completas = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.SP_ARROW_KEYS, 3, 6, 4 )
		TA.Add( self.TAS_Completas, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.TA_Ambas = wx.CheckBox( self, wx.ID_ANY, u"Simples y Completas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TA_Ambas.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		TA.Add( self.TA_Ambas, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.TA_Entry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TA_Entry.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		TA.Add( self.TA_Entry, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		MAIN_bSizer.Add( TA, 0, wx.EXPAND, 5 )
		
		self.line_hor2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MAIN_bSizer.Add( self.line_hor2, 0, wx.EXPAND |wx.ALL, 5 )
		
		Muestra_entry = wx.BoxSizer( wx.HORIZONTAL )
		
		muestras_pickChoices = []
		self.muestras_pick = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, muestras_pickChoices, wx.CB_DROPDOWN|wx.CB_SORT )
		Muestra_entry.Add( self.muestras_pick, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.manual_order = wx.ToggleButton( self, wx.ID_ANY, u"Ordenar Manualmente", wx.DefaultPosition, wx.DefaultSize, 0 )
		Muestra_entry.Add( self.manual_order, 0, wx.ALL, 5 )
		
		
		MAIN_bSizer.Add( Muestra_entry, 1, wx.EXPAND, 5 )
		
		autocomplete_bsizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.AutoComplete_Entry = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		autocomplete_bsizer.Add( self.AutoComplete_Entry, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.add_equipo = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
		autocomplete_bsizer.Add( self.add_equipo, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		MAIN_bSizer.Add( autocomplete_bsizer, 1, wx.EXPAND)
		
		Muestras_Botones = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Muestras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.Muestras.SetMinSize( wx.Size( 400,150 ) )
		
		Muestras_Botones.Add( self.Muestras, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.line_ver1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		Muestras_Botones.Add( self.line_ver1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Botones = wx.BoxSizer( wx.VERTICAL )
		
		self.Cargar = wx.Button( self, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Botones.Add( self.Cargar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Limpiar = wx.Button( self, wx.ID_ANY, u"Limpiar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Botones.Add( self.Limpiar, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Open_Carga = wx.Button( self, wx.ID_ANY, u"Abrir Carga", wx.DefaultPosition, wx.DefaultSize, 0 )
		Botones.Add( self.Open_Carga, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Open_Visco = wx.Button( self, wx.ID_ANY, u"Abrir Viscosidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		Botones.Add( self.Open_Visco, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		Muestras_Botones.Add( Botones, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		MAIN_bSizer.Add( Muestras_Botones, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( MAIN_bSizer )
		self.Layout()
		
		# Connect Events
		self.Empresas.Bind( wx.EVT_CHOICE, self.select_database )
		self.TA_Simples.Bind( wx.EVT_CHECKBOX, self.S_check_event )
		self.TA_Completas.Bind( wx.EVT_CHECKBOX, self.C_check_event )
		self.TA_Ambas.Bind( wx.EVT_CHECKBOX, self.SyC_check_event )
		self.muestras_pick.Bind( wx.EVT_COMBOBOX, self.agregar_equipo )
		self.manual_order.Bind( wx.EVT_TOGGLEBUTTON, self.order_manual )
		self.AutoComplete_Entry.Bind( wx.EVT_TEXT_ENTER, self.add_muestra )
		self.add_equipo.Bind( wx.EVT_BUTTON, self.add_muestra )
		self.Cargar.Bind( wx.EVT_BUTTON, self.data_entry )
		self.Limpiar.Bind( wx.EVT_BUTTON, self.clear_input )
		self.Open_Carga.Bind( wx.EVT_BUTTON, self.open_carga )
		self.Open_Visco.Bind( wx.EVT_BUTTON, self.open_visco )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def add_muestra( self, event ):
		event.Skip()


	def select_database( self, event ):
		event.Skip()
	
	def S_check_event( self, event ):
		event.Skip()
	
	def C_check_event( self, event ):
		event.Skip()
	
	def SyC_check_event( self, event ):
		event.Skip()
	
	def agregar_equipo( self, event ):
		event.Skip()
	
	def order_manual( self, event ):
		event.Skip()
	
	
	
	def data_entry( self, event ):
		event.Skip()
	
	def clear_input( self, event ):
		event.Skip()
	
	def open_carga( self, event ):
		event.Skip()
	
	def open_visco( self, event ):
		event.Skip()
	
class dialog_Numeracion ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ID Ingeniería - Carga de Muestras", pos = wx.DefaultPosition, size = wx.Size( 500,245 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer_dialog = wx.BoxSizer( wx.VERTICAL )
		
		self.tittle_dialog = wx.StaticText( self, wx.ID_ANY, u"Numeracion de Muestras", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.tittle_dialog.Wrap( -1 )
		self.tittle_dialog.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer_dialog.Add( self.tittle_dialog, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_dialog.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.textCtrl_dialog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		bSizer_dialog.Add( self.textCtrl_dialog, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_dialog )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
class dialog_NuevaEmpresa ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ID Ingeniería - Nueva Empresa", pos = wx.DefaultPosition, size = wx.Size( 351,120 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer_NuevaEmpresa = wx.BoxSizer( wx.VERTICAL )
		
		bSizerH1_NuevaEmpresa = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tittle_NuevaEmpresa = wx.StaticText( self, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.tittle_NuevaEmpresa.Wrap( -1 )
		self.tittle_NuevaEmpresa.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizerH1_NuevaEmpresa.Add( self.tittle_NuevaEmpresa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_NuevaEmpresa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerH1_NuevaEmpresa.Add( self.text_NuevaEmpresa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer_NuevaEmpresa.Add( bSizerH1_NuevaEmpresa, 1, wx.EXPAND|wx.TOP, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_NuevaEmpresa.Add( self.m_staticline4, 0, wx.ALL|wx.EXPAND)
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_cancel = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.button_cancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.button_NuevaEmpresa = wx.Button( self, wx.ID_ANY, u"Crear empresa", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.button_NuevaEmpresa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer_NuevaEmpresa.Add( bSizer13, 1|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_NuevaEmpresa )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_cancel.Bind( wx.EVT_BUTTON, self.close )
		self.button_NuevaEmpresa.Bind( wx.EVT_BUTTON, self.append_empresa )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()
	
	def append_empresa( self, event ):
		event.Skip()
	
class dialog_Error ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ID Ingeniería - Carga de Muestras", pos = wx.DefaultPosition, size = wx.Size( 419,270 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer_Error = wx.BoxSizer( wx.VERTICAL )
		
		self.text_Error = wx.StaticText( self, wx.ID_ANY, u"¡Error!", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.text_Error.Wrap( -1 )
		self.text_Error.SetFont( wx.Font( 18, 70, 90, 92, False, wx.EmptyString ) )
		self.text_Error.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer_Error.Add( self.text_Error, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.line_error = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer_Error.Add( self.line_error, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.text_Erorr2 = wx.StaticText( self, wx.ID_ANY, u"Las siguientes muestras aparecen al menos dos veces:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.text_Erorr2.Wrap( -1 )
		self.text_Erorr2.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.text_Erorr2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizer_Error.Add( self.text_Erorr2, 0, wx.ALL | wx.EXPAND, 5 )
		
		self.textCtrl_Error = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(380,100), wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer_Error.Add( self.textCtrl_Error, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_error = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_error.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.button_error.Bind(wx.EVT_BUTTON, self.close_error)
		bSizer_Error.Add( self.button_error, 1, wx.ALL | wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer_Error )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
        

	def __del__( self ):
		pass

