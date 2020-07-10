task allocation using CBC_MIXED_INTEGER_PROGRAMMING solver
from [ortools](https://developers.google.com/optimization) 

```
./allocate_tasks.py --num-children 3< task_points.txt

child 0 is allocated tasks [3, 5]
child 1 is allocated tasks [0, 1, 2]
child 2 is allocated tasks [4, 6]
```

```
./allocate_tasks.py --num-children 3 < task_points.no_soln.txt
FAILDOG, task points sum to 31 which can't be allocated between 3 children.
```

```
./gen_data.py --num-children 20 --total-child-task-size 50 | shuf > task_points.larger.txt
wc -l task_points.larger.txt
292

time ./allocate_tasks.py --num-children 20 < task_points.larger.txt

child 0 is allocated tasks [5, 28, 32, 48, 73, 74, 77, 91, 100, 132, 178, 179, 196, 222, 240, 247, 259, 262, 273]
child 1 is allocated tasks [10, 15, 21, 22, 30, 33, 41, 65, 85, 102, 126, 129, 140, 184, 231, 263]
child 2 is allocated tasks [6, 13, 72, 83, 86, 108, 142, 175, 183, 211, 215, 248, 288]
child 3 is allocated tasks [20, 23, 66, 75, 89, 105, 127, 134, 158, 185, 218, 236, 255]
child 4 is allocated tasks [7, 12, 16, 47, 103, 143, 161, 176, 188, 238, 254, 289]
child 5 is allocated tasks [9, 19, 44, 120, 131, 152, 153, 181, 206, 220, 223, 229, 265, 286, 290]
child 6 is allocated tasks [50, 55, 68, 104, 113, 138, 169, 195, 204, 207, 237, 269, 280, 281, 282]
child 7 is allocated tasks [14, 39, 57, 69, 107, 116, 128, 145, 162, 167, 171, 191, 210, 253]
child 8 is allocated tasks [58, 80, 96, 114, 155, 172, 201, 216, 221, 224, 239, 243, 261, 270, 277]
child 9 is allocated tasks [25, 54, 67, 82, 92, 125, 177, 186, 190, 213, 230, 242, 250, 275, 285]
child 10 is allocated tasks [37, 46, 51, 76, 101, 139, 144, 174, 180, 182, 214, 234, 245, 257, 284]
child 11 is allocated tasks [0, 1, 29, 31, 64, 88, 111, 136, 160, 166, 168, 198, 208, 246, 264, 267]
child 12 is allocated tasks [35, 36, 38, 61, 78, 90, 118, 173, 192, 200, 217, 258, 268, 287]
child 13 is allocated tasks [11, 26, 49, 60, 87, 112, 141, 150, 194, 197, 235, 249, 266]
child 14 is allocated tasks [4, 8, 84, 94, 121, 123, 154, 170, 193, 212, 228, 260, 271, 274, 276]
child 15 is allocated tasks [24, 42, 53, 63, 79, 109, 115, 117, 148, 156, 165, 225, 252, 278]
child 16 is allocated tasks [34, 43, 45, 59, 97, 110, 122, 133, 137, 146, 203, 226, 241, 251, 279, 283]
child 17 is allocated tasks [17, 18, 62, 106, 119, 135, 149, 159, 205, 209, 232, 233, 244]
child 18 is allocated tasks [27, 40, 52, 70, 93, 98, 147, 151, 163, 187, 189, 202, 227, 272]
child 19 is allocated tasks [2, 3, 56, 71, 81, 95, 99, 124, 130, 157, 164, 199, 219, 256, 291]

real	0m4.653s
user	0m4.567s
sys	0m0.073s
```