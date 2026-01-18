from datetime import datetime

# Message Class
class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.time = datetime.now().strftime("%H:%M:%S")
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"[{self.time}] ({self.id}) {self.sender.username}: {self.content}"


# User Class

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
            return

        chatroom.add_user(self)
        self.chatroom = chatroom
        print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
            return

        self.chatroom.remove_user(self)
        print(f"{self.username} left {self.chatroom.name}")
        self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
            return

        if not content.strip():
            print("Message cannot be empty.")
            return

        self.chatroom.broadcast(self, content)

# ChatRoom Class

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user in self.users:
            print(f"{user.username} is already in the chatroom.")
            return
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_users(self):
        print(f"\nUsers in {self.name}:")
        if not self.users:
            print("No users online.")
            return
        for user in self.users:
            print("-", user.username)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        if not self.messages:
            print("No messages yet.")
            return
        for msg in self.messages:
            print(msg)

    def clear_chat(self):
        self.messages.clear()
        print("Chat history cleared.")

# Main Execution

if __name__ == "__main__":
    room = ChatRoom("Debug Room")

    Milan = User("Milan")
    Rajdip = User("Rajdip")
    kavy = user("kavy")

    Milan.join_chatroom(room)
    Rajdip.join_chatroom(room)
    kavy.join_chatroom(room)
    

    room.show_users()

    Milan.send_message("Hello everyone!")
    Rajdip.send_message("   ")      # empty message test
    Rajdip.send_message("Hi Milan!")
    kavy.send_message("Hey Rajdip, what's up?")

    room.show_chat_history()

    room.clear_chat()
    room.show_chat_history()

    Milan.leave_chatroom()
    Rajdip.leave_chatroom()
    kavy.leave_chatroom()
