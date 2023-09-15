import argparse

import logger
import ui
from randomizer import Randomizer
from utils import prog_name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog=prog_name,
        description='meow')
    parser.add_argument("--game_path", type=str, default=None)
    parser.add_argument('--no_gui', action='store_true')
    parser.add_argument("--settings_path", type=str, default="settings.json")
    parser.add_argument('-s', '--seed', type=str, default=None,
                        help='seed used to determine randomization. the same seed will always crate the same '
                             'randomization.')
    parser.add_argument('-f', '--force_extract', action='store_true', help='force (re-)extraction of the game files')
    parser.add_argument('-d', '--dry', '--dry-run', action='store_true',
                        help='do not create output other then a log file')
    parser.add_argument('-p', '--placement-folder', '--placement',
                        help='do not create output other then a log file')
    args = parser.parse_args()
    logger.setup_logging()
    if args.no_gui:
        rando = Randomizer()
        rando.setup_from_args(args, True)
        rando_gen = rando.run()
        for i in rando_gen:
            print(i)
    else:
        ui.run_ui(args)
