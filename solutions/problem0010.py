"""Problem #10 [Medium]

This problem was asked by Apple.

Implement a job scheduler which takes in a function `f` and an integer `n`,
and calls `f` after `n` milliseconds.
"""

import heapq
import time
from typing import Callable, List, NamedTuple


Job = Callable[[], None]


class JobRecord(NamedTuple):
    run_at: float
    job: Job


class JobScheduler:
    """Job scheduler."""

    def __init__(self) -> None:
        self.waiting_jobs: List[JobRecord] = []

    def schedule(self, job: Job, n: int) -> None:
        """Schedule a job to be called after `n` milliseconds."""

        heapq.heappush(
            self.waiting_jobs,
            JobRecord(run_at=time.time() + (n / 1000), job=job),
        )

    def all_done(self) -> bool:
        """Check if all scheduled jobs were called."""

        return len(self.waiting_jobs) == 0

    def run_once(self) -> None:
        """Run one iteration of the scheduler."""

        while self.waiting_jobs and self.waiting_jobs[0].run_at < time.time():
            job = heapq.heappop(self.waiting_jobs).job
            job()

    def run(self, delay=0.001) -> None:
        """Run the scheduler."""

        while not sched.all_done():
            sched.run_once()
            time.sleep(delay)


def gen_job(msg: str) -> Job:
    """Return a job printing the given message."""

    def job() -> None:
        print(f'{time.time():.3f} -- {msg}')

    return job


if __name__ == '__main__':
    sched = JobScheduler()
    sched.schedule(gen_job('job #1'), 1000)
    sched.schedule(gen_job('job #2'), 2000)
    sched.schedule(gen_job('job #3'), 1500)

    print(f'{time.time():.3f} -- start')
    sched.run()
