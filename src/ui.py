import flet as ft
import time

from context import *
from ai import *
from db import *

g_ui_instance = None;

g_ui_title = "AutoMedic";
g_ui_theme_mode = "dark";

##################################################
class UiFlet():
    _ui_ft = None;
    _ui_page = None;
#-------------------------------------------------
    _ui_main_con = None;

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
    _ui_instance = None;
    _ai_instance = None;

    def __init__(self, instance): 
        self._db_instance = instance._db.fn_get_instance();
        self._map_instance = instance._map.fn_get_instance();
        self._ai_instance = instance._ai.fn_get_instance();
        self._ui_instance = instance._ui.fn_get_instance();
    
    def fn_start(self): 
        if self._ui_instance != None and self._ui_instance._ui_ft != None:
            self._ui_instance._ui_ft.app(port=8550, target=self.fn_flet_main, view=ft.WEB_BROWSER);
    
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
        if self._ui_instance != None:
             self._ui_instance._ui_page = page;
        
        self.fn_option_title(page, None);
        self.fn_option_theme(page, None);

        time.sleep(1);

        main_container = self._ui_instance._ui_ft.Container(
            width=(self._ui_instance._ui_page.width - 1), 
            height=(self._ui_instance._ui_page.height * 0.9), 
            border_radius=20,
            bgcolor=self._ui_instance._ui_ft.colors.GREY_900);

        self._ui_instance._ui_page.add(main_container);
        self._ui_instance._ui_page.update();

        self._ui_instance._ui_main_con = main_container;

        searchbar = FletUiSearchbar(self._ui_instance);
        searchbar.fn_start();
        panel = FletUiPanel(self._ui_instance);
        panel.fn_start();
        mapView =  FletUiMapbutton(self._ui_instance);
        mapView.fn_start();

##################################################
class FletUiSearchbar():
    _instance = None;

    def __init__(self, ui): 
        self._instance = ui.fn_get_instance();
    
    def fn_start(self):
        searchbar_container = self._instance._ui_ft.Container(
            content=self._instance._ui_ft.Row([
                self._instance._ui_ft.TextField(
                    hint_text="Send a message",
                    autofocus=True,
                    shift_enter=True,
                    min_lines=1,
                    max_lines=5,
                    filled=True,
                    expand=True
                ),
                self._instance._ui_ft.IconButton(
                    icon=self._instance._ui_ft.icons.SEND_ROUNDED,
                    on_click=self.fn_searchbar_click
                )
            ])
        );

        self._instance._ui_page.add(
            self._instance._ui_ft.Column(
                controls=[
                    searchbar_container
                ]
            )
        );

        self._instance._ui_page.update();
    
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
    def fn_searchbar_click(e): 
        # map
        pass;

##################################################
class FletUiPanel():
    _instance = None;

    _ui_panel_con = None;
    _ui_panel_top = None;
    _ui_panel_bottom = None;

    _panel_offset = -0.9;

    def __init__(self, ui): 
        self._instance = ui.fn_get_instance();
    
    def fn_start(self):

        def animate(e):
            if self._panel_offset == 0:
                self._panel_offset = -0.9;
                panel_container.offset = self._instance._ui_ft.transform.Offset(self._panel_offset, 0);
                panel_container.update()
            elif self._panel_offset == -0.9:
                self._panel_offset = 0;
                panel_container.offset = self._instance._ui_ft.transform.Offset(self._panel_offset, 0);
                panel_container.update()

        time.sleep(1);

        panel_container=self._instance._ui_ft.Container(
            width=500,
            height=(self._instance._ui_page.height * 0.9), 
            bgcolor=self._instance._ui_ft.colors.GREY_200,
            border_radius=20,
            offset=self._instance._ui_ft.transform.Offset(self._panel_offset, 0),
            animate_offset=self._instance._ui_ft.animation.Animation(300),
            on_click=animate,
        );

        self._instance._ui_main_con.content = self._instance._ui_ft.Column([panel_container]);
        self._instance._ui_page.update();
    
        self._instance._ui_panel_con = panel_container;
    
        self.fn_enable();

    def fn_end(self): pass;
    def fn_enable(self): 

        panel_top = self._instance._ui_ft.Container(
            width=450,
            height=(self._instance._ui_page.height * 0.4), 
            bgcolor=self._instance._ui_ft.colors.BLACK
        );
    
        panel_bottom = self._instance._ui_ft.Container(
            width=450,
            height=(self._instance._ui_page.height * 0.4), 
            bgcolor=self._instance._ui_ft.colors.BLACK
        );
    
        self._instance._ui_panel_con = self._instance._ui_ft.Column([panel_top, panel_bottom]);
        self._instance._ui_page.update();
    
        self._instance._ui_panel_top = panel_top;
        self._instance._ui_panel_bottom = panel_bottom;

    def fn_disable(self): pass;

##################################################
class FletUiMapbutton():
    _instance = None;

    def __init__(self, ui): 
        self._instance = ui.fn_get_instance();
    
    def fn_start(self): pass;
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################



