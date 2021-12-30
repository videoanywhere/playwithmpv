import os
from urllib import parse
from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

app = Flask(__name__)

MPV_CMD_OPTIONS = "--http-header-fields='referer:https://www.bilibili.com/','user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.39'"


@app.route("/")
@use_args({"cmd": fields.Str(required=True)}, location="querystring")
def shellcmd(args):
    args = parse.unquote(args['cmd']).split(' ')
    if args[0] == "mpv":
        if len(args) == 2:
            cmd = args[0] + ' "' + args[1] + '" ' + MPV_CMD_OPTIONS
        else:
            return args[0] + ": bad cmd, wrong number of parmas "
    else:
        return args[0] + ": bad cmd, not implement"
    status = os.system(cmd)
    return "shell_cmd_status: {}".format(status)


def start():
    app.run(port=50000)
