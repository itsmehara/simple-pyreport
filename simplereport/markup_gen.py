#!/usr/bin/python

import jinja2
import json


def get_markup(rep_templ_file, input_json_file):
    templateLoader = jinja2.FileSystemLoader( searchpath="./" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( rep_templ_file )
    json_data = json.load(open(input_json_file))
    return template.render(json_data)


def save_markup(markup, target_file):
    with open(target_file, "w+") as fp:
        fp.write(markup)


def main(template, input_json, output):
    markup = get_markup(template, input_json)
    save_markup( markup, output )


if __name__ == '__main__':
    try:
        rep_templ_file, \
        input_json_file, \
        output_file = "report_base.tmpl", \
                      "input.json",\
                      "output.html"
        # markup = get_markup(rep_templ_file, input_json_file)
        # save_markup( markup, output_file )
        main(rep_templ_file, input_json_file, output_file)
    except Exception as e:
        print("Failed")
        raise e
    else:
        print("Success")
