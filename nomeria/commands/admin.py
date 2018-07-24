from command import Command
from subprocess import Popen, PIPE


class CmdGit(Command):
    """
    Run git pull

    Usage:
        git-update
    """

    key = "git-update"
    locks = "cmd:perm(Developer)"

    def func(self):
        proc = Popen("git pull", shell=True, stderr=PIPE, stdout=PIPE)
        self.caller.msg(proc.communicate())
