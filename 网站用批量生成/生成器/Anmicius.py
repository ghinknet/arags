import tensorflow as tf
import numpy as np
import random
import pickle
from PIL import Image
from qrcode import make as makeqr
from dnnlib import tflib
import time, os, hashlib


def main():
        # Define global variables.
        seed = random.randint(0,10000000)
        available_charaters = {'Anmicius', 'Camil', 'Grey', 'King', 'Ray'}


        # Select charater and input seed.
        selected_character = 'Anmicius'
        while selected_character not in available_charaters:
            selected_character = input('Type in the character you want to draw, e.g. \"Anmicius\" and \"Ray\" (no quotes).\n')
            if selected_character not in available_charaters:
                print('You typed in a character that is not available or you made a misspell, try agian.')
    
        seed_str = ''
        if seed_str != '':
            if seed_str.isdigit():
                seed = int(seed_str.encode('utf-8'))
            else:
                seed = int(hashlib.sha256(seed_str.encode('utf-8')).hexdigest(), 16) % 10**8
    
        print('INFO: Setting up variables...')
        tflib.init_tf()
        rnd = np.random.RandomState(seed)
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)

        print('INFO: Loading pretrained model...')
        Gs = pickle.load(open('models/network-%s-gs.pkl' % selected_character, 'rb'))
        latents = rnd.randn(1, Gs.input_shape[1])
    
        print('INFO: Generating...')
        images = Gs.run(latents, None, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)
    
        im = Image.fromarray(images[0], 'RGB')
        qr = makeqr('This is an image automatically generated by Aotu Draw Bot by Rand0mZ.LiCloud provides computing resources. Seed: %d' % seed)
        w, h = im.size
        qw, qh = qr.size
        if qw > w:
            qr = qr.resize((w, w))
        elif qh > h:
            qr = qr.resize((h, h))
        qw, qh = qr.size

        imd = im.load()
        for i in range(w):
            for j in range(h):
                d = imd[i, j]
                imd[i, j] = d[:-1] +((d[-1] | 1) if qr.getpixel((i%qw, j%qh)) else (d[-1] & ~1),)

        print('Done!')

        save_name = '%s_%d.png' % (selected_character, seed)
        print('INFO: Saving %s' % save_name)
        output_dir = os.path.join(os.path.dirname(os.getcwd()) , 'ARAGS/安迷修')
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
        im.save(os.path.join(output_dir, save_name))
        print('INFO: Image %s is saved in directory.' % save_name)
        print('INFO: All processes has done!')
        print('Thank you for using this software and obeying the terms of use above.')
        time.sleep(3)
        

def generate_image(model, save_path, selected_character, seed, amount):
    tflib.init_tf()

    print('INFO: Loading pretrained model...')
    Gs = pickle.load(open(model, 'rb'))

    if not os.path.isdir(save_path):
        os.mkdir(save_path)

    for i in range(1, amount + 1):
        print('INFO: Generating image %d' %i)
        rnd = np.random.RandomState(seed)
        fmt = dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True)
        latents = rnd.randn(1, Gs.input_shape[1])
        images = Gs.run(latents, None, truncation_psi=0.7, randomize_noise=True, output_transform=fmt)

        im = Image.fromarray(images[0], 'RGB')
        qr = makeqr('This is an image automatically generated by Aotu Draw Bot CLI by Rand0mZ hence this image is not for commercial propose. Seed: %d' % seed)
        w, h = im.size
        qw, qh = qr.size
        if qw > w:
            qr = qr.resize((w, w))
        elif qh > h:
            qr = qr.resize((h, h))
        qw, qh = qr.size

        imd = im.load()
        for i in range(w):
            for j in range(h):
                d = imd[i, j]
                imd[i, j] = d[:-1] +((d[-1] | 1) if qr.getpixel((i%qw, j%qh)) else (d[-1] & ~1),)

        print('Done!')

        save_name = '%s_%d.png' % (selected_character, seed)
        print('INFO: Saving %s' % save_name)
        im.save(os.path.join(save_path, save_name))
        print('INFO: Image %s is saved to %s.\n' % (save_name, save_path))
        seed += i - 1

if __name__ == "__main__":
    main()
