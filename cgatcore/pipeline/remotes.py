'''
Remotes.py - Functions to execute cgat-core in the cloud 
'''

import os


CGATCORE_MOUNTPOINT = "/mnt/cgacore"
CGATCORE_SEARCHPATH = os.path.dirname(os.path.dirname(__file__))


def singluarity_statement(path_img, cmd,args="", envvars=None, container=None,
                    shell=None):
    '''
    Execute command using singularity container 
    '''

    if envvars:
        envvars = " ".join("SINGLULARITYENV_%s=%s" % (k, v) for k, v in envvars.items())
    else:
        envvars = ""

    if shell is None:
        shell = "sh"
    else:
        shell = os.path.split(shell)[-1]

    mount
    args += " --bind %s:%s" % (CGATCORE_SEARCHPATH, CGATCORE_MOUNTPOINT)

    if container:
        args += " --pwd %s" % (container)

    statement = "%s singularity exec --home %s %s %s %s -c %s " % (envvars, os.getcwd(),
                                                                   args, path_img, shell,
                                                                   cmd.replace("'", r"'\''"))

    return statement
