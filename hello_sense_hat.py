from sense_hat import SenseHat


r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

sense = SenseHat()

rmon4 = [k, d, d, k, d, d, k, k,
         d, d, d, k, d, d, k, k,
         d, d, r, n, n, n, n, k,
         d, r, r, n, n, n, n, k,
         k, k, n, k, n, k, n, k,
         k, k, n, n, n, n, n, k,
         k, k, n, c, c, c, n, k,
         k, k, n, n, n, n, n, k
]
		
		
	

sense.set_pixels(rmon4)