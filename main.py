#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

passage_name = "West of House"
passage_text = "This is an open field west of a white house, with a boarded front door."
passage_prompt = "What would you like to do? "
print(passage_name)
print(passage_text)
user_responce = input(passage_prompt)
if user_responce == "go north":
    print("good job!")
