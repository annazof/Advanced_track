class SMS_store:
    """
    Create a store of SMS messages
    """
    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """Makes new SMS tuple, inserts it after other messages
        in the store. When creating this message, its
        has_been_viewed status is set False."""
        has_been_viewed = "False"
        new_message = (from_number, time_arrived, text_of_SMS, has_been_viewed)
        self.messages.append(new_message)

    def message_count(self): # Returns the number of sms messages in my_inbox
        return len(self.messages)


    def get_unread_indexes(self): # Returns list of indexes of all not-yet-viewed SMS messages
        for (index, new_message) in enumerate(self.messages):
            if "False" in new_message:
                print(index)


    def get_message(self, i):
        if i < len(self.messages):
            new_message = self.messages[i]
            print(new_message[0:3])
            self.messages[i] = new_message[:3], "True"
        else:
            return None
    # Return (from_number, time_arrived, text_of_sms) for message[i]
    # Also change its state to "has been viewed".
    # If there is no message at position i, return None


    def delete(self, i):# Delete the message at index i
        if i < len(self.messages):
            del self.messages[i]
        else:
            return None

    def clear(self):# Delete all messages from inbox
        self.messages.clear()

inbox = SMS_store()
inbox.add_new_arrival("+49660", "12:53", "food")
print(inbox.message_count())
print(inbox.get_unread_indexes())
print(inbox.get_message(0))
print(inbox.get_unread_indexes())
inbox.delete(0)
print(inbox.message_count())
inbox.add_new_arrival("+49660", "12:53", "food")
print(inbox.message_count())
inbox.add_new_arrival("+3165", "14:43", "drink")
inbox.add_new_arrival("+5165", "15:43", "sfsdf")
print(inbox.get_message(1))
print(inbox.get_message(0))
print(inbox.get_message(2))
print(inbox.get_unread_indexes())
print(inbox.message_count())
inbox.clear()
print(inbox.message_count())