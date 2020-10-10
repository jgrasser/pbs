from . import us_state_abbrev
from . import utils
import argparse, json

def show(argv):
    parser = argparse.ArgumentParser(
               usage='pbs.py station [-h]',
               description='Search and play video content from PBS.org')

    parser.add_argument('--callsign', type=str, required=True)
    args = parser.parse_args(argv)

    # https://jaws.pbs.org/localization/false/?callsign=wttw
    output = utils.client('GET', path=f'/localization/false/?callsign={args.callsign}', host='https://jaws.pbs.org')
    return json.dumps(output.get('station'))
