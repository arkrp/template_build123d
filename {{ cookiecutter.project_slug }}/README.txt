Project Name: {{ cookiecutter.project_name}}

Author: {{ cookiecutter.author }}

Description: {{ cookiecutter.project_short_description }}

Files:
makefile - automatically set up and run the program
    make offline - switches the make to offline mode, eg will not check online.
main.py - python file specifying the assembly
requirements.txt - Specific pip packages which will guarenteed run this
soft_requirements.txt - List of packages which should be enough, but is not stable. Used for offline installs.
