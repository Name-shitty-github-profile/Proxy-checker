import requests, asyncio
f = open("Valid.txt", "a")
i = open("Invalid.txt", "a")
async def check(proxies):
    try:
        proxi = {'http': f'http://{proxy}','https':f'http://{proxy}'}
        r = requests.get("https://discord.gg/catcha", proxies=proxi)
        f.write(proxi)
    except:
        i.write(f"{proxy}")

async def main():
    tasks: list = []
    with open("proxies.txt","r") as f:
        proxies = f.read().split('\n')
    for proxy in proxies:
        print(f"Checking --> {proxy}")
        tasks.append(asyncio.create_task(check(proxy)))
    for i in tasks: await i
