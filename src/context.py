import threading

from db import *
from map import *
from ai import *
from ui import *

g_instance = None; # Singleton

class Context():

    def __init__(self):
        global g_instance;
        
        if g_instance == None:
            g_instance = self;

            self._db=DbSqlite();
            self._map=MapKaKaoAPI();
            self._ai=AiChatGPT();
            self._ui=UiFlet();
    
            self._list=[self._db, self._map, self._ai, self._ui];
        
    def fn_start(self): 
        for iter in self._list:
            if self._ui != iter:
                t = threading.Thread(target=iter.fn_start);
                t.start();
                t.join();
            else:
                iter.fn_start();
    
    def fn_end(self): 
        for iter in self._list:
            iter.fn_end();
        
    def fn_enable(self): 
        for iter in self._list:
            iter.fn_enable();
    
    def fn_disable(self): 
        for iter in self._list:
            iter.fn_disable();

    def fn_get_instance(self): 
        if g_instance != None:
            return g_instance;
