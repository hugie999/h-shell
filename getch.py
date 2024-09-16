#yoinked from https://stackoverflow.com/a/22085679
import sys
import select
import tty
import termios
import contextlib

class keyboardHolder(contextlib.AbstractContextManager):
    def __init__(self) -> None:
        super().__init__()
        self.started:bool = False
        self.old_settings:any = None
    @property
    def isData(self):
        if not self.started:
            raise ValueError('not started!')
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    def __enter__(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        try:
            tty.setcbreak(sys.stdin.fileno())
        except Exception as e:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
            raise e
        return self
    def read(self) -> str:
        return sys.stdin.read(1)
    def __exit__(self, exc_type: any, exc_value: any, traceback: any) -> bool | None:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
        return super().__exit__(exc_type, exc_value, traceback)
    # def __exit__(self,a,b,c) -> None:
    #     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
