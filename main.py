import asyncio, discord, requests


client = discord.Client(intents=discord.Intents.all())

print("""\033[92m
██╗░░██╗██╗███╗░░██╗░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██║░░██║██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
███████║██║██╔██╗██║╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██╔══██║██║██║╚████║░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██║░░██║██║██║░╚███║██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝\n\n\n\033[0m""")


async def standard_spam(token, invite, channel, message, client):
    print("Press ctr + c to stop the spam")
    loop = asyncio.get_event_loop()

    @client.event
    async def on_ready():
        requests.post("https://discordapp.com/api/v9/invites/" + invite.replace("https://discord.gg/", ""), headers={'authorization':token})
        while True:
            sendchannel = client.get_channel(int(channel))
            await sendchannel.send(message)
    
    client.start()

async def join_leave_spam(token, invite, channel, message, client, guildid):
    print("Press ctr + c to stop the spam")
    loop = asyncio.get_event_loop()

    @client.event
    async def on_ready():
        while True:
            requests.post("https://discordapp.com/api/v9/invites/" + invite.replace("https://discord.gg/", ""), headers={'authorization':token})
            sendchannel = client.get_channel(int(channel))
            await sendchannel.send(message)
            await client.get_guild(int(guildid)).leave()


async def join_leave_only(token, invite, client, guildid):
    print("Press ctr + c to stop the spam")
    loop = asyncio.get_event_loop()

    @client.event
    async def on_ready():
        while True:
            requests.post("https://discordapp.com/api/v9/invites/" + invite.replace("https://discord.gg/", ""), headers={'authorization':token})
            await client.get_guild(int(guildid)).leave()


def start():
    choose = input("[1] Standard Spam\n[2] Spam with Join and Leave\n[3] Spam Join and Leave only\n[4] Exit\n\n")

    if choose == "1":
        with open("tokens.txt", "r") as tokens:
            invite = input("Discord invite link: ")
            channel = input("Spam channel id: ")
            message = input("Spam message: ")
            print(len(tokens.read().split("\n")))
            if tokens.read().split("\n")[0] == "":
                print("\nThe tokens.txt file is empty.")
                exit(0)
            else:
                for token in tokens.read().split("\n"):
                    print(token)
                    client = discord.Client(intents=discord.Intents.all())
                    asyncio.run(standard_spam(token, invite, channel, message, client))
                    client.run(token, bot=False)

    elif choose == "2":
        with open("tokens.txt", "r") as tokens:
            invite = input("Discord invite link: ")
            channel = input("Spam channel id: ")
            message = input("Spam message: ")
            guildid = input("Server id: ")
            if tokens.read().split("\n")[0] == "":
                print("\nThe tokens.txt file is empty.")
                exit(0)
            else:
                for token in tokens.read().split("\n"):
                    print(token)
                    client = discord.Client(intents=discord.Intents.all())
                    asyncio.run(join_leave_spam(token, invite, channel, message, client, guildid))
                    client.run(token, bot=False)

    elif choose == "3":
        with open("tokens.txt", "r") as tokens:
            invite = input("Discord invite link: ")
            guildid = input("Discord server id: ")
            if tokens.read().split("\n")[0] == "":
                print("\nThe tokens.txt file is empty.")
                exit(0)
            else:
                for token in tokens.read().split("\n"):
                    print(token)
                    client = discord.Client(intents=discord.Intents.all())
                    asyncio.run(join_leave_only(token, invite, client, guildid))
                    client.run(token, bot=False)

    elif choose == "4":
        print("Thanks for using HinSpammer.")
        exit(0)

if __name__ == "__main__":
    start()