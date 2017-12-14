# simple-pyreport
Sample python code for report generation.

## Step1:
### Install virtual environment
```buildoutcfg
HaraMac:simple-pyreport haranadhagupta$ pip install virtualenv
Requirement already satisfied: virtualenv in /Library/Python/2.7/site-packages
HaraMac:simple-pyreport haranadhagupta$ 
```
### Create the virtual environment folder.
```buildoutcfg
HaraMac:simple-pyreport haranadhagupta$ 
HaraMac:simple-pyreport haranadhagupta$ virtualenv env --no-site-packages
New python executable in /Users/haranadhagupta/docs/dev/clones/simple-pyreport/env/bin/python
Installing setuptools, pip, wheel...done.
HaraMac:simple-pyreport haranadhagupta$ 
```
### Activate the v-env
```buildoutcfg
HaraMac:simple-pyreport haranadhagupta$ 
HaraMac:simple-pyreport haranadhagupta$ source env/bin/activate
(env) HaraMac:simple-pyreport haranadhagupta$ 
```


## Step2:
install jinja 2 in virtual environment
```buildoutcfg
(env) HaraMac:simple-pyreport haranadhagupta$ pip install jinja
Requirement already satisfied: jinja in ./env/lib/python2.7/site-packages
(env) HaraMac:simple-pyreport haranadhagupta$ 
```

## Step3:
### Verify the environment, for python version and installed packages.
```buildoutcfg
(env) HaraMac:simple-pyreport haranadhagupta$ pip freeze
Jinja==1.2
Jinja2==2.10
MarkupSafe==1.0
(env) HaraMac:simple-pyreport haranadhagupta$
(env) HaraMac:simple-pyreport haranadhagupta$ python
Python 2.7.10 (default, Feb  7 2017, 00:08:15) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(env) HaraMac:simple-pyreport haranadhagupta$
```

## Step4:
### go to input file folder, 
#### __Note: (this folder should have both template, and json files.)__
### run the code
```buildoutcfg
(env) HaraMac:simple-pyreport haranadhagupta$ 
(env) HaraMac:simple-pyreport haranadhagupta$ 
(env) HaraMac:simple-pyreport haranadhagupta$ ls
LICENSE			README.md		env			requirements.txt	simplereport
(env) HaraMac:simple-pyreport haranadhagupta$ 
(env) HaraMac:simple-pyreport haranadhagupta$ cd simplereport/
(env) HaraMac:simplereport haranadhagupta$ ls
__init__.py		input.json		markup_gen.py		other_trails		report_base.tmpl
(env) HaraMac:simplereport haranadhagupta$ python markup_gen.py 
<html>
<body>
<table style="width:100%">
  <tr>
    <th>key1</th> <th>key2</th> <th>key3</th> <th>key4</th>
  </tr>
    
        <tr> <td>100</td> <td>100</td>
        <td>100</td> <td>100</td> </tr>
    
        <tr> <td>200</td> <td>200</td>
        <td>200</td> <td>200</td> </tr>
    
        <tr> <td>300</td> <td>300</td>
        <td>300</td> <td>300</td> </tr>
    
        <tr> <td>400</td> <td>400</td>
        <td>400</td> <td>400</td> </tr>
    
        <tr> <td>500</td> <td>500</td>
        <td>500</td> <td>500</td> </tr>
    
</table>
</body>
</html>
(env) HaraMac:simplereport haranadhagupta$ 
(env) HaraMac:simplereport haranadhagupta$ 
```