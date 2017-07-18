#pi minecraft
#usage python flatmap.py [blockid]
import sys
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
mc.setBlocks(-128,0,-128,128,64,128,0)
#bid = block.SANDSTONE.id
#bid = block.SNOW_BLOCK.id
bid = block.GRASS.id
mc.setBlocks(-128,0,-128,128,-64,128,bid)
mc.postToChat('world flattened')
print('world flattened')
#if len(sys.argv) > 1):
#    bid = int(sys.argv[1])
#else:
#    bid = block.SANDSTONE.id
#
#if bid < 0 or bid > 108:
#    bid = block.SANDSTONE.id
#
#mc.setBlocks(-128,0,-128,128,-64,128,bid)

x,y,z = mc.player.getPos()
mc.player.setPos(0,0,0)
mc.postToChat('player moved')


#x,y,z = mc.player.getPos()

        
