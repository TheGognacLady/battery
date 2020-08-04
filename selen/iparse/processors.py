

class DefaultProcessor:

    def process(self, data):
        posts_count = len(data['mediacodes'])
        likers = set(dict(data['active_likes']).keys())
        commentators = set(dict(data['active']).keys())
        followers = set(dict(data['followers']).keys())
        l_intersection = followers & likers
        c_intersection = followers & commentators
        obj =  {1: len(c_intersection), 2: len(commentators), 3: len(l_intersection), 4: len(likers)}
        obj['lf'] = obj[4] / obj[3] if obj[3] != 0 else obj[4]
        obj['cf'] = obj[2] / obj[1] if obj[1] != 0 else obj[2]
        obj['comments_per_post'] = len(commentators) / posts_count
        obj['comments_suspicious'] = (obj[2] - obj[1]) / posts_count
        obj['likes_per_post'] = len(likers) / posts_count
        obj['likes_suspicious'] = (obj[4] - obj[3]) / posts_count
        return obj
