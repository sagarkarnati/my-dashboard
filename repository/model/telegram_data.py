class TelegramData:

    def __init__(self, id, entity_id, channel_name, message_id, message, message_time, created_ts):
        self.id = id
        self.entity_id = entity_id
        self.channel_name = channel_name
        self.message_id = message_id
        self.message = message
        self.message_time = message_time
        self.created_ts = created_ts
