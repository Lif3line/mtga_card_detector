import time

from mtga_get_card_positions import *

t0 = time.time()
mtga_get_card_positions(False)
t1 = time.time()

print(f"Runtime: ~{t1-t0:3f}s")


mtga_get_card_positions(True)  # Show pretty debug images
