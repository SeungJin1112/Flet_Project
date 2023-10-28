from context import *
import flet as ft

g_ui_instance = None;

##################################################
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
    
    def fn_start(self): 
        self._ui_mainscreen=FletUiMainscreen();
        self._ui_searchbar=FletUiSearchbar();
        self._ui_panel=FletUiPanel();
        self._ui_mapbutton=FletUiMapbutton();
    
        self._ui_list = [self._ui_mainscreen, 
                         self._ui_searchbar, 
                         self._ui_panel, 
                         self._ui_mapbutton];
    
        for iter in self._ui_list:
                iter.fn_start();

    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################
class FletUiMainscreen():
    
    def __init__(self): pass;

    def fn_start(self): 
        global g_ui_instance;

        if g_ui_instance != None and g_ui_instance._ui_ft != None:
            g_ui_instance._ui_ft.app(target=g_ui_instance._ui_mainscreen.fn_flet_main, view=ft.WEB_BROWSER);
    
    def fn_end(self): pass;
    def fn_enable(self): pass;
    def fn_disable(self): pass;

    def fn_flet_main(self, page):
        def view_pop(e):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        def send_message_click(e):
            page.go("/result")

        def route_change(e):
            page.views.clear()
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Container(
                            content=ft.Text(
                                "AutoMedic",
                                size=50,
                                color='white',
                                font_family='poppins',
                                weight=ft.FontWeight.BOLD,
                            ),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            alignment=ft.alignment.center,
                            border_radius=5,
                            padding=5,
                            expand=True,
                        ),
                        ft.Row(
                            [
                                ft.TextField(
                                    hint_text="증상을 입력하세요",
                                    autofocus=True,
                                    shift_enter=True,
                                    min_lines=1,
                                    max_lines=5,
                                    filled=True,
                                    border=ft.InputBorder.NONE,
                                    bgcolor=ft.colors.SURFACE_VARIANT,
                                    expand=True,
                                    #on_submit=send_message_click,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SEND_ROUNDED,
                                    tooltip="검색 결과 확인",
                                    on_click=send_message_click,
                                ),
                            ]
                        )
                    ],
                )
            )
            if page.route == "/result":
                page.views.append(
                    ft.View(
                        "/result",
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Text(
                                            "panel area", 
                                            size=20, 
                                            color='black', 
                                            font_family='poppins', 
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        border_radius=5,
                                        padding=10,
                                        height=page.height,
                                        expand=2,
                                    ),
                                    ft.Container(
                                        content=ft.Text(
                                            "map area", 
                                            size=20, 
                                            color='black', 
                                            font_family='poppins', 
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        alignment=ft.alignment.center,
                                        bgcolor=ft.colors.SURFACE_VARIANT,
                                        border_radius=5,
                                        padding=10,
                                        height=page.height,
                                        expand=3,
                                    )
                                ]
                            )
                        ],
                    )
                )
            page.update()

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        page.go(page.route)
##################################################
class FletUiSearchbar():
    def __init__(self): pass;
    def fn_start(self): pass;
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



