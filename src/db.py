from context import *
import csv
import sqlite3 as sql3
import os

g_sql3_instance = None;
##################################################
g_DEFINE_CREATE_TABLE_APPROXIMATELY = """
    CREATE TABLE IF NOT EXISTS T_APPROXIMATELY
    (
        seq INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        desc TEXT
    )
""";
#-------------------------------------------------
g_DEFINE_CREATE_TABLE_DISEASES = """
    CREATE TABLE IF NOT EXISTS T_DISEASES 
    (
        seq INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        desc TEXT,
        list_approximately TEXT
    )
""";
#-------------------------------------------------
g_DEFINE_CREATE_TABLE_REPORT = """
""";
##################################################

class DbSqlite():
    _con = None;
    _c = None;

    def __init__(self):
        global g_sql3_instance;

        if g_sql3_instance == None:
            g_sql3_instance = self; 
    
    def fn_start(self):
            self.fn_init_create_tables();
            self.fn_init_insert_tables();

    def fn_end(self): 
        if self._con != None: 
            self._con.close();

    def fn_enable(self): pass;
    def fn_disable(self): pass;
##################################################
    def fn_init_create_tables(self):
        self._con = sql3.connect('auto_medic.db');
        self._c = self._con.cursor();

        self._c.execute(g_DEFINE_CREATE_TABLE_APPROXIMATELY);
        self._c.execute(g_DEFINE_CREATE_TABLE_DISEASES);
        self._c.execute(g_DEFINE_CREATE_TABLE_REPORT);

        self._con.commit();
        self._con.close();
##################################################
    def fn_init_insert_tables(self):
        lists_insert_data = [["approximately.csv","T_APPROXIMATELY","(NULL,?,?)"], 
                     ["diseases.csv","T_DISEASES","(NULL,?,?,?)"], 
                     ["report.csv","",""]];
        
        self._con = sql3.connect('auto_medic.db');
        self._c = self._con.cursor();

        for list_insert_data in lists_insert_data:
            csv_name, table_name, args = list_insert_data;

            if os.path.exists(csv_name):
                with open(csv_name, 'r') as file:
                    reader = csv.reader(file);

                    for row in reader:
                        self._c.execute("INSERT INTO "+table_name+" VALUES "+args, row);
    
        self._con.commit();
        self._con.close();



