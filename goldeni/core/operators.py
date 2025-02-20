import Image, time

# Convolve the kernels with the image to approximate the gradient
def convolve(pixels, width, height, k):

	# Initialize the various kernels
	dim = 2
	if k == 'scharr':
		xmask, ymask = get_scharr_masks()
	if k == 'prewitt':
		xmask, ymask = get_prewitt_masks()
	if k == 'sobel':
		xmask, ymask = get_sobel_masks()
	if k == 'roberts':
		xmask, ymask = get_roberts_masks()
		dim = 1

	outimg = Image.new('L', (width, height))
	outpixels = list(outimg.getdata())

	iend = width
	jend = height
	mend = dim+1
	nend = dim+1

	# Main loop
	# Runs through image and calculates an approximation of the magnitude of the gradient at all points.
	for i in xrange(0, iend):
		for j in xrange(0, jend):
			sumX,sumY = 0,0
			mag = 0
			if j == 0 or j == height-1: mag = 0
			elif i == 0 or i == width-1: mag = 0
			else:
				for m in xrange(mend):
					for n in xrange(nend):
						# Sum x and y gradient-approximations
						pix = pixels[(i-m+(j-n)*width)]
						sumX += xmask[m,n] * pix
						sumY += ymask[m,n] * pix

			# Approximate the magnitude of the gradient
			mag = (abs(sumX)+abs(sumY))/(mend*nend)

			# Normalize bad results
			if mag > 255: mag = 255
			if mag < 0: mag = 0

			# Output gradient approximation to an image array
			outpixels[i+j*width] = 255 - mag
	outimg.putdata(outpixels)
	return outimg

# Define edge-detection operators
def get_scharr_masks():
	xmask = {}
	ymask = {}

	xmask[(0,0)] = -3
	xmask[(0,1)] = 0
	xmask[(0,2)] = 3
	xmask[(1,0)] = -10
	xmask[(1,1)] = 0
	xmask[(1,2)] = 10
	xmask[(2,0)] = -3
	xmask[(2,1)] = 0
	xmask[(2,2)] = 3

	
	ymask[(0,0)] = 3
	ymask[(0,1)] = 10
	ymask[(0,2)] = 3
	ymask[(1,0)] = 0
	ymask[(1,1)] = 0
	ymask[(1,2)] = 0
	ymask[(2,0)] = -3
	ymask[(2,1)] = -10
	ymask[(2,2)] = -3

	return (xmask, ymask)

def get_roberts_masks():
	xmask = {}
	ymask = {}

	xmask[(0,0)] = 1
	xmask[(0,1)] = 0
	xmask[(1,0)] = 0
	xmask[(1,1)] = -1
	
	ymask[(0,0)] = 0
	ymask[(0,1)] = 1
	ymask[(1,0)] = -1
	ymask[(1,1)] = 0

	return (xmask, ymask)

def get_sobel_masks():
	xmask = {}
	ymask = {}

	xmask[(0,0)] = -1
	xmask[(0,1)] = 0
	xmask[(0,2)] = 1
	xmask[(1,0)] = -2
	xmask[(1,1)] = 0
	xmask[(1,2)] = 2
	xmask[(2,0)] = -1
	xmask[(2,1)] = 0
	xmask[(2,2)] = 1

	
	ymask[(0,0)] = 1
	ymask[(0,1)] = 2
	ymask[(0,2)] = 1
	ymask[(1,0)] = 0
	ymask[(1,1)] = 0
	ymask[(1,2)] = 0
	ymask[(2,0)] = -1
	ymask[(2,1)] = -2
	ymask[(2,2)] = -1

	return (xmask, ymask)

def get_prewitt_masks():
	xmask = {}
	ymask = {}

	xmask[(0,0)] = -1
	xmask[(0,1)] = 0
	xmask[(0,2)] = 1
	xmask[(1,0)] = -1
	xmask[(1,1)] = 0
	xmask[(1,2)] = 1
	xmask[(2,0)] = -1
	xmask[(2,1)] = 0
	xmask[(2,2)] = 1

	
	ymask[(0,0)] = 1
	ymask[(0,1)] = 1
	ymask[(0,2)] = 1
	ymask[(1,0)] = 0
	ymask[(1,1)] = 0
	ymask[(1,2)] = 0
	ymask[(2,0)] = -1
	ymask[(2,1)] = -1
	ymask[(2,2)] = -1

	return (xmask, ymask)

# Old convolve functction
#def convolve(pixels, width, height, k):
#	dim = 2
#	if k == 'scharr':
#		xmask, ymask = get_scharr_masks()
#	if k == 'prewitt':
#		xmask, ymask = get_prewitt_masks()
#	if k == 'sobel':
#		xmask, ymask = get_sobel_masks()
#	if k == 'roberts':
#		xmask, ymask = get_roberts_masks()
#		dim = 1
#
#	outimg = Image.new('L', (width, height))
#	outpixels = list(outimg.getdata())
#
#	for y in xrange(height):
#		for x in xrange(width):
#			sumX, sumY, magnitude = 0,0,0
#
#			if y == 0 or y == height-1: magnitude = 0
#			elif x == 0 or x == width-1: magnitude = 0
#			else:
#				for i in xrange(-1,dim):
#					for j in xrange(-1,dim):
#						sumX += (pixels[x+i+(y+j)*width]) * xmask[i+1, j+1]
#						sumY += (pixels[x+i+(y+j)*width]) * ymask[i+1, j+1]
#
#			magnitude = abs(sumX) + abs(sumY)
#
#			if magnitude > 255: magnitude = 255
#			if magnitude < 0: magnitude = 0
#
#			outpixels[x+y*width] = 255 - magnitude
#	outimg.putdata(outpixels)
#	return outimg

def main(img, kern):
	pixels = list(img.getdata())
	w, h = img.size
	print "Convolution Started"
	start = time.time()
	outimg = convolve(pixels, w, h, kern)
	print "Convolution Complete: Time = ", (time.time()-start)*1000, "ms"
	return outimg
