import hou
import shutil
import inspect
from pathlib import Path
import gsops.authentication as auth


GSOPS_BASE_PATH = Path(hou.getenv("GSOPS") or str(Path(inspect.getfile(inspect.currentframe())).parent.parent))
GSOPS_DEFAULT_STATE_DIR = GSOPS_BASE_PATH / ".gsops"
GSOPS_STATE_DIR = Path(hou.getenv("GSOPS_USER_DATA_DIR") or (GSOPS_BASE_PATH / ".gsops"))

GSOPS_STATE_FILES = (
    "config.json",
    ".config_json_touched",
    "popup_init.json",
    "license"
)



def _add_gsops_shelf():
    if not hou.isUIAvailable():
        return

    try:
        gsops_shelf = hou.shelves.shelves()['gsops_shelf']
    except KeyError:
        print("Could not find 'gsops_shelf'.")
        return

    try:
        shelf_set_1 = hou.shelves.shelfSets()['shelf_set_1']
    except KeyError:
        print("Could not find 'shelf_set_1'.")
        return

    # Filter out any deleted shelves safely
    valid_shelves = []
    shelf_names = []
    for shelf in shelf_set_1.shelves():
        try:
            name = shelf.name()
            valid_shelves.append(shelf)
            shelf_names.append(name)
        except hou.ObjectWasDeleted:
            continue

    if gsops_shelf.name() not in shelf_names:
        valid_shelves.append(gsops_shelf)
        shelf_set_1.setShelves(valid_shelves)


def _attempt_authentication_and_setup():
    auth.setup_for_authentication_level(auth.authenticate())


def _setup_initial_state_folder():
    # 0) Nothing to do if state dir is $GSOPS/.gsops
    if GSOPS_DEFAULT_STATE_DIR == GSOPS_STATE_DIR:
        return
    
    # 1) collect all source state files ($GSOPS/.gsops/...) 
    source_state_files = []
    for state_file_name in GSOPS_STATE_FILES:
        state_file_path = GSOPS_DEFAULT_STATE_DIR / state_file_name
        if state_file_path.exists():
            source_state_files.append(state_file_path)
    
    # 2) identify source files that don't already exist in target folder, and keep (source, target) pairs
    source_target_file_path_pairs = []
    for source_state_file_path in source_state_files:
        target_state_file_path = GSOPS_STATE_DIR / source_state_file_path.name
        if target_state_file_path.exists():
            continue
        source_target_file_path_pairs.append((source_state_file_path, target_state_file_path))

    # 3) Proceed to copying files, if any
    if source_target_file_path_pairs:
        GSOPS_STATE_DIR.mkdir(parents=True, exist_ok=True)
        for source_file_path, target_file_path in source_target_file_path_pairs:
            shutil.copy2(source_file_path, target_file_path)


def init():
    _setup_initial_state_folder()
    if hou.isUIAvailable():
        _add_gsops_shelf()
        _attempt_authentication_and_setup()
