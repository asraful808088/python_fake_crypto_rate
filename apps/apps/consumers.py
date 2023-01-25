import asyncio
import json
import random

from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer


class GetCryptoCoinRate(AsyncConsumer):
   async  def websocket_connect(self,event):
        await self.send({
            'type':'websocket.accept'
        })

   async  def websocket_disconnect(self,event):
    try:
        if self.cryptoLoop.isRunning:
            self.cryptoLoop.cancel()
    except:
        pass   
    
    raise StopConsumer()



   async def rateLoop(self):
        self.cryptoLoop.isRunning = True
        while True:
            await asyncio.sleep(1)
            cryptoCoin={
            "BTC":random.uniform(20000.5, 40000.5),
            "ETH":random.uniform(1000.5,4000.5),
            "USDT":random.uniform(1.5, 3.5),
            "BNB":random.uniform(30.5, 75.5),
            "USDC":random.uniform(1.5, 5.5),
            "XRP":random.uniform(40.5, 55.5),
            "BUSD":random.uniform(40.5, 55.5),
            "ADA":random.uniform(30.5, 75.5),
            "LTC":random.uniform(50.5, 70.5),
            }
            await self.send({
                'type':'websocket.send',
                'text':json.dumps(cryptoCoin)
            })


            
   async  def websocket_receive(self,event):
        
        self.cryptoLoop = asyncio.create_task(self.rateLoop()) 
        
        

       
        