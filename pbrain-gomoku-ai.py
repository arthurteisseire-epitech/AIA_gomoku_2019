#!/usr/bin/python3

from sys import stdin
import dispatcher

for line in stdin:
    dispatcher.dispatch(line)
