class Twitter:

    def __init__(self):
        self.followers = defaultdict(list)
        self.tweets = defaultdict(list)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap =[]
        res = []
        for follower in self.followers[userId] + [userId]:
            for tweet in self.tweets[follower]:
                heapq.heappush_max(maxHeap, (tweet))
        for i in range(10):
            if maxHeap:
                res.append(heapq.heappop_max(maxHeap)[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId] :
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
