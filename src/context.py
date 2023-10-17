from db import *
from ui import *
from map import *
from ai import *

class Context():
    def fn_init(self): 
        self._db=DbSqlite();
        self._ui=UiFlet();
        self._map=MapKaKaoAPI();
        self._ai=AiChatGPT();

    def fn_start(self): pass;
        #self._ui.fn_start();
    def fn_stop(self): pass
    def fn_enable(self): pass
    def fn_disable(self): pass
