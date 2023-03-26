from typing import List

class Process:

    def __init__(self, name, arrive_time, running_time, time_slice=50) -> None:
        self.name = name
        self.arrive_time = arrive_time
        self.running_time = running_time
        self.time_slice = time_slice

    def run(self, current_time: int) -> int:
        t = min(self.running_time, self.time_slice)
        self.arrive_time = current_time + t
        self.running_time -= t
        return t

    def is_done(self) -> bool:
        return self.running_time == 0
    
    def __str__(self) -> str:
        return f'({self.name} arrive: {self.arrive_time}, remain: {self.running_time})'
    
    def __eq__(self, tar: object) -> bool:
        if not isinstance(tar, Process):
            return False
        return self.name == tar.name


def schedule(timetable: List[Process]) -> None:

    current_time = 0
    queue = [proc for proc in timetable if proc.arrive_time <= current_time]
    
    while len(queue) > 0:

        print(f'time: {current_time}, queue: {", ".join(list(map(str, queue)))}')

        proc = queue[0]
        queue = queue[1:]

        running_time = proc.run(current_time)
        print(f'time: {current_time}, run {proc.name} for {running_time}ms')
        current_time += running_time

        newly_arrived = [e for e in timetable if e.arrive_time <= current_time and not e.is_done() and e not in queue]
        newly_arrived.sort(key=lambda p: p.arrive_time)

        queue += newly_arrived


schedule([
    Process('P1', 0, 95),
    Process('P4', 15, 65),
    Process('P5', 75, 35),
    Process('P3', 175, 145),
    Process('P2', 201, 10)
])

# will output
"""
time: 0, queue: (P1 arrive: 0, remain: 95)
time: 0, run P1 for 50ms
time: 50, queue: (P4 arrive: 15, remain: 65), (P1 arrive: 50, remain: 45)
time: 50, run P4 for 50ms
time: 100, queue: (P1 arrive: 50, remain: 45), (P5 arrive: 75, remain: 35), (P4 arrive: 100, remain: 15)
time: 100, run P1 for 45ms
time: 145, queue: (P5 arrive: 75, remain: 35), (P4 arrive: 100, remain: 15)
time: 145, run P5 for 35ms
time: 180, queue: (P4 arrive: 100, remain: 15), (P3 arrive: 175, remain: 145)
time: 180, run P4 for 15ms
time: 195, queue: (P3 arrive: 175, remain: 145)
time: 195, run P3 for 50ms
time: 245, queue: (P2 arrive: 201, remain: 10), (P3 arrive: 245, remain: 95)
time: 245, run P2 for 10ms
time: 255, queue: (P3 arrive: 245, remain: 95)
time: 255, run P3 for 50ms
time: 305, queue: (P3 arrive: 305, remain: 45)
time: 305, run P3 for 45ms
"""

        