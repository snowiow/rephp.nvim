import neovim
from rephp.rephp import RePhp


@neovim.plugin
class RePhpHandlers(object):
    def __init__(self, nvim):
        self.rephp = RePhp(nvim)

    @neovim.function('RePhp')
    def function_handler(self, args):
        self.rephp.run(args[0])
