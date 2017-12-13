#!/usr/bin/python

import jinja2
import json


def prepare_markup():
    templateLoader = jinja2.FileSystemLoader( searchpath="./" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( "./report_base.tmpl" )
    templateVars = json.load(open("input.json"))
    outputText = template.render(templateVars)
    return outputText


if __name__ == '__main__':
    print prepare_markup()
