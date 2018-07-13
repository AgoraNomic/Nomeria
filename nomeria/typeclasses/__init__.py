import evennia


@classmethod
def _from_cmds(cls, cmds, name, **kwargs):
    """
    Dynamically generates and returns a new CmdSet subclass.

    Args:
        cmds - an iterable of commands to be added
        name - name of the subclass

    Kwargs:
        All kwarg keys not listed above will be added to the
        namespace of the generated subclass
    """

    def at_cmdset_creation(self):
        for cmd in cmds:
            self.add(cmd)

    namespace = dict(at_cmdset_creation=at_cmdset_creation, **kwargs)
    return type(name, (cls,), namespace)


evennia.CmdSet.from_cmds = _from_cmds
