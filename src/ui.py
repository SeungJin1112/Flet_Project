import flet as ft
import time
import threading

from flet_map import FletMap
from context import *
from ai import *
from db import *
from map import *

g_ui_instance = None;

g_ui_title = "AutoMedic";
g_ui_theme_mode = "dark";

g_prompt_data=None;

##################################################
class UiFlet():
    _ui_ft = None;
    _ui_page = None;
#-------------------------------------------------
    _ui_main_con = None;
    _ui_map_con = None

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
    _db_instance = None;
    _map_instance = None;
    _ai_instance = None;
    _ui_instance = None;

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

        searchbar = FletUiSearchbar(self._ui_instance, self._ai_instance);
        searchbar.fn_start();
        mapView =  FletUiMap(self._ui_instance);
        mapView.fn_start();
        panel = FletUiPanel(self._ui_instance, self._db_instance, self._map_instance);
        panel.fn_start();

##################################################
class FletUiSearchbar():
    _instance = None;
    _ai_instance = None;

    _text_field = None;

    def __init__(self, ui, ai): 
        self._instance = ui.fn_get_instance();
        self._ai_instance = ai.fn_get_instance();
    
    def fn_start(self):

        self._text_field = self._instance._ui_ft.TextField(
            hint_text="Send a message",
            autofocus=True,
            shift_enter=True,
            min_lines=1,
            max_lines=5,
            filled=True,
            expand=True
        );
        
        searchbar_container = self._instance._ui_ft.Container(
            content=self._instance._ui_ft.Row([
                self._text_field,
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
    def fn_searchbar_click(self, e): 
        global g_prompt_data;

        ai_prompt = AiPrompt(self._ai_instance);
        #------------------------------
        #test request
        #ai_prompt.fn_start();
        #------------------------------
        prompt = self._text_field.value;
        g_prompt_data = ai_prompt.fn_prompt(prompt);
        pass;

##################################################
g_ui_panel_con = None;
g_ui_panel_top = None;
g_ui_panel_bottom = None;

class FletUiPanel():
    _instance = None;

    _panel_offset = -0.9;

    def __init__(self, ui, db, map): 
        self._instance = ui.fn_get_instance();
        self._db_instance = db.fn_get_instance();
        self._map_instance = map.fn_get_instance();
    
    def fn_start(self):
        global g_ui_panel_con;

        def animate(e):
            if self._panel_offset == 0:
                self._panel_offset = -0.9;

                if g_ui_panel_con != None:
                    g_ui_panel_con.offset = self._instance._ui_ft.transform.Offset(self._panel_offset, 0);
                
                self._instance._ui_page.update();


            elif self._panel_offset == -0.9:
                self._panel_offset = 0;

                if g_ui_panel_con != None:
                    g_ui_panel_con.offset = self._instance._ui_ft.transform.Offset(self._panel_offset, 0);

                self._instance._ui_page.update();

        time.sleep(1);

        g_ui_panel_con=self._instance._ui_ft.Container(
            width=500,
            height=(self._instance._ui_page.height * 0.9), 
            bgcolor=self._instance._ui_ft.colors.BLACK,
            border_radius=20,
            offset=self._instance._ui_ft.transform.Offset(self._panel_offset, 0),
            animate_offset=self._instance._ui_ft.animation.Animation(300),
            on_click=animate,
        );

        self._instance._ui_main_con.content = self._instance._ui_ft.Column([g_ui_panel_con]);
        self._instance._ui_page.update();

        t = threading.Thread(target=self.fn_enable);
        t.start();
        t.join();

    def fn_end(self): pass;
    def fn_enable(self): 
        global g_ui_panel_con;

        data_bottom = self._map_instance.searchKeywords()

        columns_bottom = [
            self._instance._ui_ft.DataColumn(self._instance._ui_ft.Text("약국, 병원 이름")),
            self._instance._ui_ft.DataColumn(self._instance._ui_ft.Text("주소"))
        ]

        rows = []
        for index, row in data_bottom.iterrows():
            data_row = self._instance._ui_ft.DataRow(
                cells=[
                    self._instance._ui_ft.DataCell(self._instance._ui_ft.Text(row['stores'])),
                    self._instance._ui_ft.DataCell(self._instance._ui_ft.Text(row['road_address']))
                ]
            )
            rows.append(data_row)

        data_table = self._instance._ui_ft.DataTable(columns=columns_bottom, rows=rows)

        '''
        list_view = self._instance._ui_ft.ListView()

        for index, row in data_bottom.iterrows():
            list_item = self._instance._ui_ft.Row([
                self._instance._ui_ft.Text(row['stores'], width=200),
                self._instance._ui_ft.Text(row['road_address'], width=200)
            ])
            list_view.controls.append(list_item)
        '''

        while True:
            time.sleep(1);

            g_ui_panel_top = self._instance._ui_ft.Container(
                expand=True,
                height=(self._instance._ui_page.height * 0.45), 
                bgcolor=self._instance._ui_ft.colors.GREY_900,
                border_radius=20
            );

            g_ui_panel_bottom = self._instance._ui_ft.Container(
                content=data_table,
                expand=True,
                height=(self._instance._ui_page.height * 0.45), 
                width=self._instance._ui_page.width, 
                bgcolor=self._instance._ui_ft.colors.GREY_900,
                border_radius=20
            );

            data_top = None;
            list_top = None;

            if g_prompt_data != None:
                data_top = self._db_instance.fn_get_main_ingredient(g_prompt_data);

                #<table 방식> //패널 하단 같은 경우는 테이블 방식 사용을 추천함.
                #columns_top = [self._instance._ui_ft.DataColumn(self._instance._ui_ft.Text("약 명칭"))];
                #table_top = self._instance._ui_ft.DataTable(columns=columns_top, 
                #                                        rows=[self._instance._ui_ft.DataRow(
                #                                            cells=[self._instance._ui_ft.DataCell
                #                                                   (self._instance._ui_ft.Text(d)) for d in row]) for row in data_top]);

                list_top = self._instance._ui_ft.ListView(spacing=10, padding=20);
                for item in data_top:
                    list_top_item = self._instance._ui_ft.Row([self._instance._ui_ft.Text(item, color=self._instance._ui_ft.colors.WHITE)]);
                    list_top.controls.append(list_top_item);
                    
                time.sleep(1);

            if data_top:
                g_ui_panel_top.content = list_top;
            
            print(data_top);

            g_ui_panel_con.content = self._instance._ui_ft.Column([g_ui_panel_top, g_ui_panel_bottom]);
            _ui_panel_map_stack = self._instance._ui_ft.Stack([self._instance._ui_map_con, g_ui_panel_con])
            self._instance._ui_main_con.content = _ui_panel_map_stack
            self._instance._ui_page.update();

    def fn_disable(self): pass;

##################################################
class FletUiMap():
    _instance = None;

    def __init__(self, ui): 
        self._instance = ui.fn_get_instance();
    
    def fn_start(self):
        self._instance._ui_map_con = self._instance._ui_ft.Container(
            self._instance._ui_ft.ListView(
                expand=True,
                controls=[
                    FletMap(expand=True, latitude=37.496504195637826, longtitude=126.95707883612786, zoom=15, screenView = [8,4],)
                ]
            )
        )

    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################


