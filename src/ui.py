from context import *
import flet as ft

g_ui_instance = None;

class UiFlet():
    _ui_ft = None;
    
    _ui_mainscreen = None;
    _ui_searchbar = None;
    _ui_panel = None;
    _ui_mapbutton = None;

    def __init__(self):
        global g_ui_instance;

        if g_ui_instance == None:
            g_ui_instance = self; 
        
        if self._ui_ft == None:
            self._ui_ft = ft;

    def fn_init(self): 
        self._ui_mainscreen=FletUiMainscreen();
        self._ui_searchbar=FletUiSearchbar();
        self._ui_panel=FletUiPanel();
        self._ui_mapbutton=FletUiMapbutton();
    
        self._ui_list = [self._ui_mainscreen, 
                         self._ui_searchbar, 
                         self._ui_panel, 
                         self._ui_mapbutton];
    
        for iter in self._ui_list:
                iter.fn_init();
    
    def fn_start(self): pass;
    def fn_stop(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

class FletUiMainscreen():
    
    def __init__(self): pass;

    def fn_init(self): 
        global g_ui_instance;

        if g_ui_instance != None and g_ui_instance._ui_ft != None:
            g_ui_instance._ui_ft.app(target=g_ui_instance._ui_mainscreen.fn_flet_main);

    def fn_start(self): pass;
    def fn_stop(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

    def fn_flet_main(self, page): 
        page.add(g_ui_instance._ui_ft.Text(value="Hello, world!"));

class FletUiSearchbar():
    def __init__(self): 
        self.fn_init();
    
    def fn_init(self): pass;
    def fn_start(self): pass;
    def fn_stop(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

class FletUiPanel():
    def __init__(self): 
        self.fn_init();
    
    def fn_init(self): pass;
    def fn_start(self): pass;
    def fn_stop(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

class FletUiMapbutton():
    def __init__(self): 
        self.fn_init();
    
    def fn_init(self): pass;
    def fn_start(self): pass;
    def fn_stop(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;



