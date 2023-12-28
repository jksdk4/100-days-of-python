class User:
    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.followers_list = []
        self.following_list = []
        self.blocked_by = []
        self.blocked_users = []

    def is_blocked(self, blocker):
        return blocker.username in self.blocked_by

    def block(self, blocked):
        if blocked.username in self.following_list:
            self.unfollow(blocked)

        self.blocked_users.append(blocked.username)
        self.remove_follower(blocked)
        blocked.blocked_by.append(self.username)
        blocked.following = len(blocked.following_list)

    def unblock(self, blocked):
        self.blocked_users.remove(blocked.username)
        blocked.blocked_by.remove(self.username)

    def follow(self, followed_user) -> None:
        print(f"{self.username} is adding {followed_user.username}...")
        if self.is_blocked(followed_user):
            print("User not available to follow.\n")
            return

        self.following_list.append(followed_user.username)
        self.following = len(self.following_list)
        followed_user.followers_list.append(self.username)
        followed_user.followers = len(followed_user.followers_list)

    def unfollow(self, unfollowed_user) -> None:
        self.following_list.remove(unfollowed_user.username)
        self.following = len(self.following_list)
        unfollowed_user.followers_list.remove(self.username)
        unfollowed_user.followers = len(unfollowed_user.followers_list)

    def remove_follower(self, removed_follower):
        self.followers_list.remove(removed_follower.username)
        self.followers = len(self.followers_list)
        removed_follower.following_list.remove(self.username)
        removed_follower.following = len(removed_follower.followers_list)


def show() -> None:
    for user in users_list:
        print("Username: ", user.username)
        print("Following: ", user.following_list)
        print("Followed by: ", user.followers_list)
        print("Amount of Followers: ", user.followers)
        print("Amount Following: ", user.following)
        print("Blocking: ", user.blocked_users)
        print("Blocked by: ", user.blocked_by)
        print()


user_1 = User(1, "Yaya")
user_2 = User(2, "Mimi")
user_3 = User(3, "Shun")

users_list = [user_1, user_2, user_3]

user_1.follow(user_2)
user_3.follow(user_2)
user_2.follow(user_3)
show()

print(f"User 2 {user_2.username} blocked user 3 {user_3.username}\n")
user_2.block(user_3)
user_3.follow(user_2)
show()

print(f"User 2 {user_2.username} unblocked user 3 {user_3.username}\n")
user_2.unblock(user_3)
user_3.follow(user_2)
show()

print(f"user 2 {user_2.username} removed user 3 {user_3.username} as a follower.\n")
user_2.remove_follower(user_3)
show()
