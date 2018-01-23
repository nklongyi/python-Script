#!/usr/bin/python
# -*- coding:utf-8 -*-


def find_all_index(arr, item):
    return [i for i, a in enumerate(arr) if a == item]


if __name__ == '__main__':
    print(find_all_index([1, 2, 3, 2, 2], 2))