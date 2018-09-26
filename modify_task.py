#!/usr/bin/env python3


def run(task="NoTask"):
    task += "\n"
    fd = open("task_table", "r+")
    tag_task = fd.readlines()
    tag_task[0] = task
    fd.close()
    fd = open("task_table", "r+")
    fd.writelines(tag_task)
    fd.close()
if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(task=argv[1])
    else:
        run()
