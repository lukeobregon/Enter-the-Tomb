import tcod as libtcod
import textwrap

class Message: #stores the messgae text and draws a white color to it
    def __init__(self, text, color=libtcod.white):
        self.text = text
        self.color = color

class MessageLog: #holds a list of messages, keeping their x coordinate, width and height. the width and height let add_message delete old messages
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height
    
    def add_message(self, message):
        #splitting message across multiple lines
        new_msg_lines = textwrap.wrap(message.text, self.width)

        for line in new_msg_lines:
            #if buffer is full, remove first line to make room
            if len(self.messages) == self.height:
                del self.messages[0]

            #add the new line as a Message object, with text and color
            self.messages.append(Message(line, message.color))