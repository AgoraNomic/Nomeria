from commands.command import Command
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

        for sec in range(1, 30):
            if proc.poll() is not None:
                for message in proc.communicate():
                    self.caller.msg(message)
                break

            self.caller.msg("...")
            yield 1
        else:
            proc.kill()
            self.caller.msg('"git pull" took too long and was killed.')
