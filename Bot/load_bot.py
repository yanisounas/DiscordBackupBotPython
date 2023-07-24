from importlib import import_module
from CLI import *

clear_screen()

for d in ["Commands", "Events"]:
    log_info(f"Loading {d}...")
    count = 0
    for file in os.listdir(f"Bot/{d}"):
        if file != "__init__.py" and file != "__pycache__" and not file.startswith('dev.'):
            try:
                import_module(f"Bot.{d}.{file[:-3]}")
                log_success(f"{file} Loaded")
                count += 1
            except Exception as e:
                log_warning(f"{file} Failed\nDebug {e}\n")
    log_info(f"{count} {d} loaded\n")
    time.sleep(3)
