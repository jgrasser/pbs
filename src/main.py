#!/usr/bin/env python3

import argparse, sys
import pbs, jaws, player

actions = {
    'stations': jaws,
    'station': jaws,
    'shows': pbs,
    'episodes': pbs,
    'seasons': pbs,
    'portalplayer': player
}

def main():
    parser = argparse.ArgumentParser(
               description='Search and play video content from PBS.org')

    parser.add_argument('action', type=str, choices=actions.keys())

    parser.add_argument('--callsign', type=str, required='station' in sys.argv)

    parser.add_argument('--show', type=str,
                        required='episodes' in sys.argv or 'seasons' in sys.argv)

    parser.add_argument('--season_cid', type=str, required='episodes' in sys.argv)
    
    parser.add_argument('--legacy_tp_media_id', type=str, required='player' in sys.argv)
    
    try:
        args = parser.parse_args()
    except:
        sys.exit(-1)

    action = args.action
    api = actions.get(args.action)

    output = getattr(api, action)(**vars(args))

    import json
    print(json.dumps(output,indent=4))

if __name__ == '__main__':
    main()
