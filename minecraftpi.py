#pi minecraft
from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block
import random

mc = Minecraft.create()
#STONE = 1
#blockNumber = 1

sleep(2)
#mc.postToChat('Hello Minecraft World')

#x,y,z = mc.player.getPos()
#mc.player.setPos(x,y+random.randint(5,25),z)

'''
for i in range(0,100):
    blockNumber = random.randint(1,25)
    mc.postToChat('BlockNumber' + str(blockNumber))
    mc.setBlock(x+5,y+i,z,blockNumber)
    sleep(0.2)
   ''' 


'''
mc.setBlocks(20,20,20,30,30,30,block.GLASS.id)
mc.setBlocks(21,21,21,29,29,29,block.AIR.id)
mc.setBlocks(23,23,23,27,27,27,block.TNT.id)
mc.player.setPos(22,22,22)
'''

air = 0
gold = 41


mc.player.setPos(100,0,100)
x,y,z = mc.player.getPos()
block_below = mc.getBlock(x,y-1,z)
while True:
    if block_below != air:
        mc.setBlock(x,y-1,z,gold)

    x,y,z = mc.player.getPos()
    block_below = mc.getBlock(x,y-1,z)

    sleep(0.1)

        
