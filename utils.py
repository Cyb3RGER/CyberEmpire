import os

prog_name = 'CyberEmpire - Yo-Gi-Oh LotD:LE Randomizer'


def delete_folder(dir, delete_this=True):
    if not os.path.isdir(dir):
        return
    for entry in os.scandir(dir):
        if entry.is_file():
            os.remove(entry)
        else:
            delete_folder(entry)
    if delete_this:
        os.rmdir(dir)