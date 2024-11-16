# calls.py

'''

Implement:
    - RecentCounter class which counts the number of recent requests within a certain time frame
    - RecentCounter() Initializes the counter with zero recent requests
    - int ping(int t)
        - Adds a new request at time t where t represents some time in ms
        - Returns the number of requests that have happened in the past 3000ms (including the new request)
            - Return the number of requests that have happened in the inclusive range [t - 3000, t]

Considerations:
    - Guaranteed every call to ping uses a strictly larger value of t than the previous call

'''

from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        start = t - 3000

        while self.requests[0] < start:
            self.requests.popleft()

        return len(self.requests)
