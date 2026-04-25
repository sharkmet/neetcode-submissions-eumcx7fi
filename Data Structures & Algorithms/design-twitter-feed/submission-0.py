class Twitter:

    def __init__(self):
        self.followMap = {} # store userIds and their unique followeeIds
        self.tweetMap = {} # stores userIds and their tweets as a list of (count, tweetId) pairs.
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        
        # Build the set of users whose tweets we'll include: followees + self
        followees = set()
        if userId in self.followMap:
            followees = set(self.followMap[userId])
            # for f in self.followMap[userId]:
                # followees.add(f)
        followees.add(userId)
        
        # Seed the heap with the most recent tweet from each user
        for followeeId in followees:
            if followeeId in self.tweetMap:
                tweets = self.tweetMap[followeeId]
                idx = len(tweets) - 1
                count, tweetId = tweets[idx]
                heapq.heappush(max_heap, (-count, tweetId, followeeId, idx - 1))
        
        result = []
        while max_heap and len(result) < 10:
            neg_count, tweetId, followeeId, next_idx = heapq.heappop(max_heap)
            result.append(tweetId)
            
            # Push the next older tweet from this user, if any
            if next_idx >= 0:
                count, tId = self.tweetMap[followeeId][next_idx]
                heapq.heappush(max_heap, (-count, tId, followeeId, next_idx - 1))
        
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            self.followMap[followerId].discard(followeeId)
        
