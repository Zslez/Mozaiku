from math   import ceil
from time   import time


__all__ = [
    'progress_bar_func',
    'log_func'
]



def log_func(func, message, log, *args):
    if log:
        print(message)

        result = func(*args)

        print('\tDone.\n')

        return result

    return func(*args)



def progress_bar_func(
        total: int,
        display: bool,
        length: int = 50
    ):

    class Progress:
        '''
        real progress bar class
        '''
        def __init__(self, total, length) -> None:
            self.total = total
            self.length = length
            self.progress = 0

            self.fill = '█'
            self.empty = '-'

            self.tot_str = str(total)

            self.start = time()

            string = ('0/' + self.tot_str).rjust(2 * len(self.tot_str) + 1)

            print(f'[00:00:00.000] - |{self.empty * self.length}| {string}', end = '')


        def update(self):
            self.progress += 1

            fill = ceil(self.progress / self.total * self.length)
            empty = self.empty * (self.length - fill)

            string = str(self.progress) + '/' + self.tot_str
            string = string.rjust(2 * len(self.tot_str) + 1)

            timestr = self.get_time()

            print(f'\r[{timestr}] - |{self.fill * fill + empty}| {string}', end = '')


        def get_time(self):
            end = time() - self.start

            hours       = str(int(end // 3600))
            mins        = str(int((end % 3600) // 60))
            secs, msecs = str(round(end % 60, 3)).split('.')

            hours  = '0' * (2 - len(hours)) + hours
            mins   = '0' * (2 - len(mins )) + mins
            secs   = '0' * (2 - len(secs )) + secs
            msecs += '0' * (3 - len(msecs))

            return hours + ':' + mins + ':' + secs + '.' + msecs


        def end(self):
            string = str(self.progress) + '/' + self.tot_str
            string = string.rjust(2 * len(self.tot_str) + 1)

            timestr = self.get_time()

            print(f'\r[{timestr}] - |{self.fill * self.length}| {string}')


    class EmptyProgress:
        '''
        fake progress bar class
        '''
        def update(self):
            pass

        def end(self):
            pass


    if display:
        return Progress(total, length)

    return EmptyProgress()
