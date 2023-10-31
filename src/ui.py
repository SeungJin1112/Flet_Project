from context import *
from ai import *

import flet as ft

g_ui_instance = None;

g_ui_title = "AutoMedic";
g_ui_theme_mode = "dark";

##################################################
class UiFlet():
    _ui_ft = None;
    _ui_page = None;

    def __init__(self):
        global g_ui_instance;

        if g_ui_instance == None:
            g_ui_instance = self; 
        
        if g_ui_instance._ui_ft == None:
            g_ui_instance._ui_ft = ft;
    
    def fn_start(self): pass;
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

    def fn_get_instance(self):
        if g_ui_instance != None:
            return g_ui_instance;
##################################################
class FletUiMainscreen():
    _instance = None;

    def __init__(self): 
         _ctx = Context();
         self._instance = self._instance._ui.fn_get_instance();
    
    def fn_start(self): 
        if self._instance != None and self._instance._ui_ft != None:
            self._instance._ui_ft.app(target=self.fn_flet_main, view=ft.WEB_BROWSER);
    
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################
    def fn_option_title(self, page, title):
        if title != None:
            page.title = title;
        else:
            page.title = g_ui_title;
    
        page.update();
#-------------------------------------------------
    def fn_option_theme(self, page, mode):
        if mode == "dark":
            page.theme_mode = "dark";
        elif mode == "light":
            page.theme_mode = "light";
        else:
            page.theme_mode = g_ui_theme_mode;
    
        page.update();
#-------------------------------------------------
# main thread
    def fn_flet_main(self, page):
        if self._instance != None:
             self._instance._ui_page = page;

        self.fn_option_title(page, None);
        self.fn_option_theme(page, None);
        self._instance._ui_page.vertical_alignment = self._instance._ui_page.horizontal_alignment = "center";

        searchbar = FletUiSearchbar(self._instance);
        searchbar.fn_start();

##################################################
class FletUiSearchbar():
    _instance = None;

    def __init__(self, ui): 
        self._instance = ui.fn_get_instance();
    
    def fn_start(self):
        self._instance._ui_page.add(
             self._instance._ui_ft.Container(
                 content=self._instance._ui_ft.Row([
                    self._instance._ui_ft.TextField(
                        hint_text="Send a message",
                        autofocus=True,
                        shift_enter=True,
                        min_lines=1,
                        max_lines=5,
                        filled=True,
                        #border=self._instance._ui_ft.InputBorder.NONE,
                        #bgcolor=self._instance._ui_ft.colors.SURFACE_VARIANT,
                        expand=True                      
                    ),
                    self._instance._ui_ft.IconButton(
                        icon=ft.icons.SEND_ROUNDED#,
                        #on_click=send_message_click
                    )
                ]),
                 alignment=self._instance._ui_ft.alignment.Alignment(0,0.8),
                 expand=True,
             )
        );
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################
class FletUiPanel():
    def __init__(self): pass;
    def fn_start(self): pass;
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################
class FletUiMapbutton():
    def __init__(self): pass;
    def fn_start(self): pass;
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################



