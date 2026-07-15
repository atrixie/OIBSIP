import json


def create_message(message_type, username, content):

    return json.dumps(
        {
            "type": message_type,
            "username": username,
            "content": content
        }
    ).encode()


def read_message(data):

    return json.loads(data.decode())