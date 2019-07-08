import argparse

import cmaj


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--scale',)
    parser.add_argument('--chord',)
    parser.add_argument('--freq', nargs=2)

    args = parser.parse_args()

    if args.scale:
        print(cmaj.scale(args.scale))

    if args.chord:
        print(cmaj.chord(args.chord))

    if args.freq:
        print(cmaj.partial(int(args.freq[0]), int(args.freq[1])))

if __name__ == '__main__':
    run()

