import argparse

import cmaj


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scale',)

    args = parser.parse_args()

    if args.scale:
        print(cmaj.scale(args.scale))

if __name__ == '__main__':
    run()

