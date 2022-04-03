#encoding=UTF-8
import random
from telethon import TelegramClient, events
file=open("answer_databse2.txt","r", encoding='utf-8-sig')
H=file.readlines()
file.close()
# for i in range(len(H)):
#     f[i] = f[i].strip()
#print(len(H))
# g = file.readlines()
# g = g.strip()
key = ""
answers={}
i1=0
for line in H:#из файла заполняем справочник впросами и вариантами ответов
    g=line.strip()
    # g = file.readlines(i)
    # g=g.strip()
    if key == g[: g.find("\\")]:
        answers[key].append(g[g.find("\\")+1:g.rfind("\\")-1])
    else:
        key = g[: g.find("\\")]
        answers[key]=[g[g.find("\\") + 1:g.rfind("\\") - 1]]
        i1 += 1
    # key = g[: g.find("\\") - 1]
print(i1)
api_id = 12868426
api_hash = '1170968e7e29e12da9194556ef47d087'
client = TelegramClient('Spider', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    for k in answers:
        if k in event.raw_text:
            await event.reply(answers[k][random.randint(0,len(answers[k])-1)])
client.start()
client.run_until_disconnected()