#!/usr/bin/python

import jinja2
import json


def get_markup(rep_templ_file, input_json_file):
    templateLoader = jinja2.FileSystemLoader( searchpath="./" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( rep_templ_file )
    json_data = json.load(open(input_json_file))
    return template.render(json_data)


if __name__ == '__main__':
    rep_templ_file, input_json_file = "./report_base.tmpl", "input.json"
    print get_markup(rep_templ_file, input_json_file)
