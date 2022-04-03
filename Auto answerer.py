#encoding=UTF-8
from telethon import TelegramClient, sync
# Вставляем api_id и api_hash
api_id = 12868426
api_hash = '1170968e7e29e12da9194556ef47d087'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
# print(client.get_me().stringify())

# client.send_message('+79037454379', 'Привет!')
# message = client.send_message(
#         'me',
#         'This message has **bold**, `code`, __italics__ and '
#         'a [nice website](https://example.com)!',
#         link_preview=False
#     )
#
#  # Sending a message returns the sent message object, which you can use
# print(message.raw_text)
#
# for message in client.iter_messages(-462718788):
#         print(message.id, message.text)

client.send_message(-462718788, 'Hi!')
