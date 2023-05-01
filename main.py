import argparse
import re
from matplotlib import pyplot as plt
import time

def main(args: argparse.Namespace):
    plt.ion()
    results = []
    figure, ax = plt.subplots(figsize=(10, 8))
    line1, = ax.plot(results)
    while True:
        try:
            line = input()
        except EOFError:
            break
        print(line, args.regex)
        match = re.match(args.regex, line)
        if match is None:
            continue
        res = match.group(args.group)
        res = float(res)
        print(res)
        
        results.append(res)
        line1.set_xdata(range(len(results)))
        line1.set_ydata(results)
        ax.relim()
        ax.autoscale_view()
        figure.canvas.draw()
        figure.canvas.flush_events()
        # time.sleep(0.001)
    plt.ioff()
    plt.show()
    #     plt.plot(results)
    #     plt.pause(0.05)
    #     plt.draw()
    #     plt.clf()
    #     plt.show()
    #     time.sleep(0.05)
    # plt.ioff()

parser = argparse.ArgumentParser(description='Plot from log')
parser.add_argument('--regex', type=str, help='regex to match', default=r'^.*pyd: \S+ \S+ (-?(0|[1-9]+[0-9]*)(\.[0-9]*)?)$')
parser.add_argument('--group', type=int, help='group to fetch', default=1)

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)