#!/usr/bin/python3
#
# Copyright 2018 British Broadcasting Corporation
#
# Author: Michael Sparks <michael.sparks@bbc.co.uk>
#
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import json

debug = 0 # Controls whether parsing error causes a crash or a warning

def slurp(filename):
    f = open(filename)
    raw = f.read()
    f.close()
    return raw


# -- Simple Command line UI tools ----------------------------------------------
def banner(what, detail):
    print(what,":")
    print("--------------------------------------------------------------")
    if type(detail) in [ dict, list ]:
        print(json.dumps(detail, indent=4))
    else:
        print(detail)
    print("--------------------------------------------------------------")
    print()


def choose_numerical_option(tag, minoption, maxoption, default=None):
    while True:
        option = input(tag)
        if default:
            if option == "":
                return default
        try:
            opt_num = int(option)
            if minoption <= opt_num <= maxoption:
                return opt_num
        except ValueError:
            pass # same error message as below

        print("Must be a value between %d and %d (inclusive)" % (minoption, maxoption))


def display_menu(menu_items):
    print("Menu.")
    print()
    for menu_item in menu_items:
        print(menu_item)

    print()




