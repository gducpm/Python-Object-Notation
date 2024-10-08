import json
import os
def pyon_clear(filename):
    """Clears the contents of the specified file."""
    if not filename or not os.path.exists(filename):
        return False
    with open(filename, 'w') as file:
        file.write("")
    return True
def pyon_save(data_dict, filename):
    """Saves the entire dictionary as JSON to the specified file."""
    if not filename:
        return False
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}
    existing_data.update(data_dict)
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)
    return True
def pyon_load(filename, dataname):
    """Loads a specific entry from the JSON file."""
    if not filename or not os.path.exists(filename):
        return False
    with open(filename, 'r') as file:
        content = json.load(file)
        return content.get(dataname, False)
