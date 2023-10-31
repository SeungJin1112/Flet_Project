from context import *
from ui import *

if __name__ == "__main__":
    ctx = Context();
    ctx.fn_start();

    ui_mainscreen = FletUiMainscreen(ctx.fn_get_instance());
    ui_mainscreen.fn_start();
