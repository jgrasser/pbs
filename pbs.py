#!/usr/bin/env python3

import argparse, sys
import pbs

actions = [
    'stations',
    'station',
    'shows',
    'episodes',
    'seasons',
    'player'
]

def main():
    parser = argparse.ArgumentParser(
               description='Search and play video content from PBS.org')

    parser.add_argument('action', type=str, choices=actions)

    try:
        args = parser.parse_args([sys.argv[1]])

        if args.action == 'shows':
            print(pbs.shows.list())
        elif args.action == 'seasons':
            print(pbs.seasons.list(sys.argv[2:]))
        elif args.action == 'episodes': 
            print(pbs.episodes.list(sys.argv[2:]))
        elif args.action == 'stations':
            print(pbs.stations.list(sys.argv[2:]))
        elif args.action == 'station':
            print(pbs.station.show(sys.argv[2:]))
        elif args.action == 'player':
            pbs.player.list(sys.argv[2:])

    except IndexError:
        parser.print_help()

if __name__ == '__main__':
    main()
