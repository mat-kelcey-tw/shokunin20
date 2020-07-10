#!/usr/bin/env python3

from ortools.linear_solver import pywraplp
import sys

num_children = 3
task_points = list(map(int, sys.stdin))

if sum(task_points) % num_children != 0:
    print(f"FAILDOG, task points sum to {sum(task_points)}"
          f" which can't be allocated between {num_children} children.",
          file=sys.stderr)
    exit(1)

task_ids = list(range(len(task_points)))
children_ids = list(range(num_children))

solver = pywraplp.Solver('simple_mip_program',
                         pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

# define a variable corresponding to task t being allocated to child c
# x[t, c] = 1 denotes task t has been allocated to child c
x = {}
for t in task_ids:
    for c in children_ids:
        x[t, c] = solver.IntVar(0, 1, name="t_%d_c_%d" % (t, c))

# constraint 1: each task is allocated to one, and only one, child.
# i.e. x[t, c] summed over children must be 1
for t in task_ids:
    num_children_doing_task = sum(x[t, c] for c in children_ids)
    solver.Add(num_children_doing_task == 1)

# constraint 2: each child must do an equal amount of the work.
# i.e. x[(t, c)] summed over tasks must be equal for all kids.
equal_amount_of_work = sum(task_points) // 3
for c in children_ids:
    total_task_points_for_child = sum(
        x[t, c] * task_points[t] for t in task_ids)
    solver.Add(total_task_points_for_child == equal_amount_of_work)

# in terms of optimisation we don't really need anything minimised or maximised,
# we're just looking for a feasible solution. so let's just maximise a value
# which we know will be equal to num tasks x num children.
objective = solver.Objective()
for t in task_ids:
    for c in children_ids:
        objective.SetCoefficient(x[t, c], 1.0)
objective.SetMaximization()

# finally run solver, and check a solution was found.
status = solver.Solve()
if status != pywraplp.Solver.OPTIMAL:
    print("sorry, no solution; :(", file=sys.stderr)
    exit(2)

# dump solution.
for c in children_ids:
    tasks = []
    for t in task_ids:
        if x[t, c].solution_value() == 1:
            tasks.append(t)
    print("child %d is allocated tasks %s" % (c, tasks))
