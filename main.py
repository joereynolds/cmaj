import argparse

import cmaj


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scale',)
    parser.add_argument('--chord',)

    args = parser.parse_args()

    if args.scale:
        print(cmaj.scale(args.scale))

    if args.chord:
        print(cmaj.chord(args.chord))

if __name__ == '__main__':
    run()

