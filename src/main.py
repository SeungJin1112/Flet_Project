from context import *
from ui import *

if __name__ == "__main__":
    ctx = Context();
    ctx.fn_start();

    ui_mainscreen = FletUiMainscreen(ctx.fn_get_instance());
    ui_mainscreen.fn_start();

    #db_test = ctx.fn_get_instance()._db;
    #db_test.fn_json_to_sql_data("{\"예상 병명\": [\"편두통\", \"감기\"], \"성분\": [\"아세트아미노펜\", \"진통제\"]}");
    #db_data = db_test.fn_get_main_ingredient("{\"예상 병명\": [\"편두통\", \"감기\"], \"성분\": [\"아세트아미노펜\", \"진통제\"]}");

    #print(db_data);
