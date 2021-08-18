# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.adv
import Global_Data

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 616,430 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		MAIN_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.Titulo = wx.StaticText( self, wx.ID_ANY, u"Carga de Muestras", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.Titulo.Wrap( -1 )
		self.Titulo.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		MAIN_bSizer.Add( self.Titulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.line_hor1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MAIN_bSizer.Add( self.line_hor1, 0, wx.EXPAND |wx.ALL, 5 )
		
		Empresa = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Empresa = wx.StaticText( self, wx.ID_ANY, u"Empresa", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ALIGN_LEFT )
		self.Empresa.Wrap( -1 )
		self.Empresa.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		Empresa.Add( self.Empresa, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		EmpresasChoices = []
		self.Empresas = wx.Choice( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 300,-1 ), EmpresasChoices )
		self.Empresas.SetSelection( 0 )
		self.Empresas.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		Empresa.Add( self.Empresas, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5 )
		
		
		MAIN_bSizer.Add( Empresa, 0, wx.EXPAND, 5 )
		
		Fecha = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Fecha = wx.StaticText( self, wx.ID_ANY, u"Fecha de Extraccion", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ALIGN_LEFT )
		self.Fecha.Wrap( -1 )
		self.Fecha.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		Fecha.Add( self.Fecha, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.date_picker = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 300,30 ), wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		self.date_picker.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		Fecha.Add( self.date_picker, 0, wx.ALL, 5 )
		
		
		MAIN_bSizer.Add( Fecha, 0, wx.EXPAND, 5 )
		
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
		
		self.add_equipo = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Muestra_entry.Add( self.add_equipo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.create_equipo = wx.Button( self, wx.ID_ANY, u"Crear Equipo", wx.DefaultPosition, wx.DefaultSize, 0 )
		Muestra_entry.Add( self.create_equipo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		MAIN_bSizer.Add( Muestra_entry, 1, wx.EXPAND, 5 )
		
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
		self.menu = wx.MenuBar( 0 )
		self.menu_empresa = wx.Menu()
		self.crear_empresa = wx.MenuItem( self.menu_empresa, wx.ID_ANY, u"Crear empresa", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_empresa.Append( self.crear_empresa )
		
		self.menu.Append( self.menu_empresa, u"Empresa" ) 
		
		self.help_menu = wx.Menu()
		self.manual = wx.MenuItem( self.help_menu, wx.ID_ANY, u"Manual de Usuario", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.manual )
		
		self.menu.Append( self.help_menu, u"Ayuda" ) 
		
		self.SetMenuBar( self.menu )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Empresas.Bind( wx.EVT_CHOICE, self.select_database )
		self.TA_Simples.Bind( wx.EVT_CHECKBOX, self.S_check_event )
		self.TA_Completas.Bind( wx.EVT_CHECKBOX, self.C_check_event )
		self.TA_Ambas.Bind( wx.EVT_CHECKBOX, self.SyC_check_event )
		self.muestras_pick.Bind( wx.EVT_COMBOBOX, self.agregar_equipo )
		self.muestras_pick.Bind( wx.EVT_TEXT_ENTER, self.agregar_equipo )
		self.add_equipo.Bind( wx.EVT_BUTTON, self.agregar_equipo )
		self.create_equipo.Bind( wx.EVT_BUTTON, self.crear_equipo )
		self.Cargar.Bind( wx.EVT_BUTTON, self.data_entry )
		self.Limpiar.Bind( wx.EVT_BUTTON, self.clear_input )
		self.Open_Carga.Bind( wx.EVT_BUTTON, self.open_carga )
		self.Open_Visco.Bind( wx.EVT_BUTTON, self.open_visco )
		self.Bind( wx.EVT_MENU, self.create_empresa, id = self.crear_empresa.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
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
	
	
	
	def crear_equipo( self, event ):
		event.Skip()
	
	def data_entry( self, event ):
		event.Skip()
	
	def clear_input( self, event ):
		event.Skip()
	
	def open_carga( self, event ):
		event.Skip()
	
	def open_visco( self, event ):
		event.Skip()
	
	def create_empresa( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog1
###########################################################################

class ErrorDiag ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		dialogBox = wx.BoxSizer( wx.VERTICAL )
		
		self.error_msg = wx.StaticText( self, wx.ID_ANY, u"ERROR", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.error_msg.Wrap( -1 )
		self.error_msg.SetFont( wx.Font( 25, 70, 90, 90, False, wx.EmptyString ) )
		
		dialogBox.Add( self.error_msg, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.dialog_msg = wx.StaticText( self, wx.ID_ANY, u"Hay una muestra que aparece al menos dos veces", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.dialog_msg.Wrap( -1 )
		self.dialog_msg.SetFont( wx.Font( 13, 70, 90, 90, False, wx.EmptyString ) )
		
		dialogBox.Add( self.dialog_msg, 0, wx.ALL|wx.EXPAND, 5 )
		
		error_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.close_msg = wx.Button( self, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		error_sizer.Add( self.close_msg, 1, wx.ALL, 5 )
		
		
		dialogBox.Add( error_sizer, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( dialogBox )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.close_msg.Bind( wx.EVT_BUTTON, self.close_dialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close_dialog( self, event ):
		event.Skip()
	

class new_empresa_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Carga de Muestras - Nueva Empresa", pos = wx.DefaultPosition, size = wx.Size( 373,119 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		ned_bsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.ned_tittle = wx.StaticText( self, wx.ID_ANY, u"Nueva Empresa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ned_tittle.Wrap( -1 )
		self.ned_tittle.SetFont( wx.Font( 20, 70, 90, 90, False, wx.EmptyString ) )
		
		ned_bsizer.Add( self.ned_tittle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		ned_bsizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ned_empresa = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		ned_bsizer2.Add( self.ned_empresa, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.crear_empresa = wx.Button( self, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		ned_bsizer2.Add( self.crear_empresa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		ned_bsizer.Add( ned_bsizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( ned_bsizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.crear_empresa.Bind( wx.EVT_BUTTON, self.append_empresa )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def append_empresa( self, event ):
		event.Skip()

class numeracion_dialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u'Carga de Muestras - Numerar', pos = wx.DefaultPosition, size = wx.Size( 499,243 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Numeracion de Muestras", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.numeracion_muestras = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE )
		bSizer1.Add( self.numeracion_muestras, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass

