import sys
import argparse

import cv2
import numpy as np

def add_image_padding(width, height, src, dst):
    # read image
    img = cv2.imread(src)
    old_image_height, old_image_width, channels = img.shape

    # create new image of desired size and color (blue) for padding
    new_image_width = max(width, old_image_width)
    new_image_height = max(height, old_image_height)
    color = (255,255,255)
    result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)


    print(f'resize {src} from {old_image_height}x{old_image_width} to {new_image_height}x{new_image_width}')

    # compute center offset
    x_center = (new_image_width - old_image_width) // 2
    y_center = (new_image_height - old_image_height) // 2

    # copy img image into center of result image
    result[y_center:y_center+old_image_height, 
           x_center:x_center+old_image_width] = img

    # save result
    print(f'save to {dst}')
    cv2.imwrite(dst, result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='the variable `line` is exposed to the cmd exec',
        )
    parser.add_argument('--width', type=int, help='min width')
    parser.add_argument('--height', type=int, help='min height')
    parser.add_argument('images', nargs='+')

    args = parser.parse_args()

    for src in args.images:
        add_image_padding(args.width, args.height, src, src)
