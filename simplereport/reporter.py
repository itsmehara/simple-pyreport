#!/usr/bin/python

import jinja2

templateLoader = jinja2.FileSystemLoader( searchpath="./" )
templateEnv = jinja2.Environment( loader=templateLoader )

file_path1 = "./sample2.jinja"

TEMPLATE_FILE = file_path1 #"./example1.jinja"
template = templateEnv.get_template( TEMPLATE_FILE )

templateVars = {
                "data":{ "title" : "My Title Test Example",
                    "description" : "A simple inquiry of function.",
                    "is_broadband_service": False,
                    "tablevals": {
                        "val1" : 100,
                        "val2" : 200,
                        "val3" : 300,
                        "val4" : 400
                        }
                    }
               }

outputText = template.render( templateVars )

print outputText


