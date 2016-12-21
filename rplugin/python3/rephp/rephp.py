import subprocess


class RePhp:
    def __init__(self, nvim):
        self.__nvim = nvim
        self.__php_exe = self.__nvim.eval('g:rephp_executable')

    def run(self, mode):
        content = ''
        if mode == 'v':
            content = self.get_last_visual_seclection()
        else:
            content = self.__nvim.current.line

        self.eval_code(content)

    def get_last_visual_seclection(self):
        start_pos = self.__nvim.call('getpos', '\'<')
        end_pos = self.__nvim.call('getpos', '\'>')
        start = start_pos[1] - 1
        end = end_pos[1]
        return ''.join(
            [line.strip() for line in self.__nvim.current.buffer[start:end]]
        )

    def eval_code(self, code):
        code = code.replace("'", "\'")
        cmd = [self.__php_exe, '-r', code]
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        output = 'echo ' + '"' + result.stdout.decode('utf-8') + '"'
        self.__nvim.command(output)
