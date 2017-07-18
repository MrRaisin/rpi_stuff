#pi minecraft
from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block
import random

mc = Minecraft.create()
sleep(2)
mc.postToChat('Hello Minecraft World')

x,y,z = mc.player.getPos()
#mc.player.setPos(x,y+random.randint(5,25),z)
msg = 'Player position x:' + str(x) + 'y:' + str(y) + 'z:'+ str(z)
mc.postToChat(msg)
#mc.player.setPos(100,0,100)
#x,y,z = mc.player.getPos()
 
