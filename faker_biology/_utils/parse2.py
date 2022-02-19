#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 10:05:04 2022

@author: richard
"""
import re, json, pprint
from collections import deque

## parses list of links. use pandoc to convert from mediawiki to gfm
## e.g. pandoc organs-wk-raw.py -f mediawiki -t gfm -o organs.md
## TODO handle titles and depth of lists depending on title
def parse_lines(lines):
    curr_depth = 0
    title_depth = 0
    line_index = 0
    stack = deque()
    for line in lines:
        ## ignore blank /whitespace
        if len(line) == 0 or line.isspace():
            continue
        depth, title_depth = get_depth2(line, title_depth)
        #  print(f"depth of {line} is {depth}")line
        line = line.rstrip("\n*[]").lstrip("#- ")
        match = re.findall(r"\[([^\[\]]+)\]", line)
        print(f"match is {match}")
        content = match[0] if len(match) > 0 else line
        if depth > curr_depth:
            stack.append({content: {}})
        elif depth == curr_depth:
            d = stack[-1]
            d[content] = {}
        elif depth < curr_depth:
            ## might be exiting a deeply nested structure back to top
            jump = curr_depth - depth
            print(content)
            pop_stack(stack, jump, 0)
            stack[-1][content] = {}

        curr_depth = depth
        line_index = line_index + 1
    jump = curr_depth
    pop_stack(stack, jump, 1)

    return stack[0]


def categories(data: dict):
    return list(data.keys())


def pop_stack(stack, diff: int, to: int):
    while diff != to:
        nested = stack.pop()
        ## uses fact all dicts are ordered by entry
        key = list(stack[-1].keys())[-1]
        stack[-1][key] = nested
        diff = diff - 1


def get_depth(line):
    m = re.match(r"(\*+)", line)
    return len(m.group())


def get_depth2(line, title_depth):
    if line.startswith("####"):
        return 3, 3
    elif line.startswith("###"):
        return 2, 2
    elif line.startswith("##"):
        return 1, 1
    else:
        #  print(line)
        m = re.match(r"^(\s+)", line)
        if m is None:
            return title_depth + 1, title_depth
        spaces = len(m.group())
        depth = spaces / 4
        return depth + title_depth + 1, title_depth


def dict_leaves(data: dict, leaves=[]):
    nodes = data.keys()
    for key in nodes:
        subnode = data[key]
        if len(subnode) > 0:
            dict_leaves(subnode, leaves)
        else:
            leaves.append(key)


def leaves_by_category(data: dict, category: str):
    leaves = []
    dict_leaves(data[category], leaves)
    return leaves


senses = {}
with open("enzymes.md") as data:
    lines = data.readlines()
    senses = parse_lines(lines)

    leaves = []
    dict_leaves(senses, leaves)
    print(leaves)
#    print(categories(senses))
# print(leaves_by_category(senses, "Eye"))
with open("enzymes.json", "w") as jsonw:
    jsonw.write(json.dumps(senses, indent=4))
