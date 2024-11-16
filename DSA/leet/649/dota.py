# dota.py

'''

Concept:
    - Two parties
        - The Radiant
        - The Dire
    - Senate
        - Consists of senators coming from the two parties
    - Voting on a change in Dota2
        - Round-based procedure
        - Each round, each senator can exercise one of the two rights
            - Ban one senator's right: A senator can make another senator lose all his rights in this and all following rounds
            - Announce the victory: If this senator found the senators who still have rights to vote are all from the same party
                - He can announce the victory and decide on the change in the game 

    - Round-based procedure starts from the first senator to the last in the given order
    - All senators who have lost their rights will be skipped during the procedure

Given:
    - A string senate
        - Representing each senator's party belonging
        - 'R' for Radiant, 'D' for the Dire
    - If there are n senators, the size of the given string will be n

Return:
    - Assuming each senator will play the best strategy for his own party
    - Predict which party will finally announce victory
        - Return "Radiant" for the Radiant party or "Dire" for the Dire party

Approach:
    - Queue??
    - Greedy approach
        - Every senator has one choice between either Ban or Announce Victory
        - Announcing Victory prior to knowing that all other members are of their own party is a wasted action
        - A Ban will always yield a positive action unless all other members are of their own party
            - But maybe not? You do ban the other senator for all other rounds though???
            

'''

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = deque()
        dire_q = deque()

        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant_q.append(i)
            else:
                dire_q.append(i)

        while radiant_q and dire_q:

            # Get the two earliest indices from both queues
            radiant_i = radiant_q.popleft()
            dire_i = dire_q.popleft()

            # Add back the smaller of the two indices (as that one will have the opportunity to ban the larger)
            # This will make this index take place after all other senators in a given turn have taken their turn
            # i.e. n + i
            if radiant_i > dire_i:
                dire_q.append(dire_i + n)
            else:
                radiant_q.append(radiant_i + n)


        return "Radiant" if radiant_q else "Dire"

# Tests
sol = Solution()
sol.predictPartyVictory("RD")