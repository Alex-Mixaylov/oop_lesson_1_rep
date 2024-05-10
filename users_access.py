class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__id = user_id # ID пользователя приватный доступ private
        self.__name = name # Имя пользователя приватный доступ private
        self.__access_level = access_level # Уровень доступа пользователя приватный доступ private

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def __str__(self):
        return f"ID: {self.get_id()}, Имя: {self.get_name()}, Уровень доступа: {self.get_access_level()}"

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.users = []

    def add_user(self, user):
        if self.get_access_level() == 'admin':
            self.users.append(user)
            print(f"Пользователь {user.get_name()} добавлен с уровнем доступа {user.get_access_level()}")
        else:
            print("Недостаточно привилегий для добавления пользователя")

    def remove_user(self, user_id):
        if self.get_access_level() == 'admin':
            self.users = [user for user in self.users if user.get_id() != user_id]
            print(f"Пользователь с ID {user_id} был успешно удален")
        else:
            print("Недостаточно привилегий для удаления пользователя")

    def show_users(self):
        print("Список пользователей:")
        for user in self.users:
            print(user)


admin = Admin(1, "Admin")
user1 = User(2, "User1")
user2 = User(3, "User2")
user3 = User(4, "User3")


admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)


admin.show_users()


admin.remove_user(3)
admin.show_users()

#user2.remove_user(1) - это  не будет работать, что как для User не определен метод remove_user

