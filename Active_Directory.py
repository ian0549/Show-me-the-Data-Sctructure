"""
Active Directory
In Windows Active Directory, a group can consist of user(s) 
and group(s) themselves. We can construct this hierarchy as such. 
Where User is represented by str representing their ids.

"""



class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group == []:
        return None
    users = group.get_users()

    if user in users:
        return True
    else:
        #use recursion through the groups
        list_groups = group.get_groups()
        for element in list_groups:

            return is_user_in_group(user, element)

    return False







parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


###############  test
print(is_user_in_group(sub_child_user,parent))

group = Group("test_groupp")
user1 = "user1"
user2 = "user2"
user3 = "user3"
user4 = "user4"
group.add_user(user1)
group.add_user(user2)
group.add_user(user3)
print(group.get_name(), "group have user1?", is_user_in_group(user1, group))
print(group.get_name(), "group have user2?", is_user_in_group(user2, group))
print(group.get_name(), "group have user3?", is_user_in_group(user3, group))
print(group.get_name(), "group have user4?", is_user_in_group(user4, group))


# Group with no Users test
# empty group has user? False
group = Group("test_groupp")
user1 = "user1"
user2 = "user2"
user3 = "user3"


print(group.get_name(), "group have user1?", is_user_in_group(user1, group))
print(group.get_name(), "group have user2?", is_user_in_group(user2, group))
print(group.get_name(), "group have user3?", is_user_in_group(user3, group))


# Group test, users with no parent
group = Group("mygroup")
user1 = "user1"
user2 = "user2"
user3 = "user3"

group.add_user(user1)

print(group.get_name(), "group have user1?", is_user_in_group(user1, group))
print(group.get_name(), "group have user2?", is_user_in_group(user2, group))
print(group.get_name(), "group have user3?", is_user_in_group(user3, group))

