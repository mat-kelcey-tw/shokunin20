#!/usr/bin/env python3

import argparse
import random

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--total-child-task-size', type=int, default=10)
parser.add_argument('--num-children', type=int, default=3)
opts = parser.parse_args()

for _ in range(opts.num_children):
    task_total = 0
    while True:
        task_size = random.randint(2, 5)
        if task_size + task_total >= opts.total_child_task_size:
            last_task_size = opts.total_child_task_size - task_total
            print(last_task_size)
            break
        task_total += task_size
        print(task_size)
