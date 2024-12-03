#!/usr/bin/env bash
# vim: filetype=bash
# ----------------------------------------------------------------------
# Get the puzzle input for the given day.
#
# Usage:   ./getinput <day> > file
# Example: ./getinput 1     > ./i/01  # write Day 1 input to "./i/01"

# File that holds your Advent of Code session key.
#
# You can find the session key by checking your browser cookies,
# using the development tools within the browser.
KEYFILE="session.key"

url="https://adventofcode.com/2024/day/${1}/input"
key=`cat ${KEYFILE}`

curl --cookie "session=${key}" ${url}
