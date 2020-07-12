from . import utils
import argparse, json

def list(argv):
   parser = argparse.ArgumentParser(
              usage='pbs.py episodes --show SHOW --seasoncid SEASONCID',
              description='Search and play video content from PBS.org')

   parser.add_argument('--show', type=str, required=True)
   parser.add_argument('--seasoncid', type=str, required=True)

   args = parser.parse_args(argv)

   return json.dumps(utils.client('GET', f'/show/{args.show}/seasons/{args.seasoncid}/episodes/?start=0&limit=24'))
