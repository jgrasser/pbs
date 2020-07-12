from . import us_state_abbrev
from . import utils
import argparse, json

def list(argv):
    parser = argparse.ArgumentParser(
               usage='pbs.py episodes [-h]',
               description='Search and play video content from PBS.org')

    args = parser.parse_args(argv)

    output = {}
    for state, code in us_state_abbrev.us_state_abbrev.items():
        output[code] = utils.client('GET', path=f'/localization/member/state/{code}', host='https://jaws.pbs.org')
    return json.dumps(output)
