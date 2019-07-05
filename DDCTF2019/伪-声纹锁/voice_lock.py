# -*- encoding: utf-8 -*-
# written in python 3.6
__author__ = 'garzon'

import cmath
import librosa # v0.6.2, maybe ffmpeg is needed as backend
import numpy as np # v1.15.4
import sys
from PIL import Image # Pillow v5.4.1

if sys.version[0] == '3':
    xrange = range
    def _range_wrapper(*args):
        return list(xrange(*args))
    range = _range_wrapper

window_size = 2048
step_size = 100
max_lim = 0.15
f_ubound = 2000
f_bins = 150
sr = 15000

def transform_x(x, f_ubound=f_ubound, f_bins=f_bins):
    freqs = np.logspace(np.log10(20), np.log10(f_ubound), f_bins)
    seqs = []
    for f in freqs:
        seq = []
        d = cmath.exp(-2j * cmath.pi * f / sr)
        coeff = 1
        for t in xrange(len(x)):
            seq.append(x[t] * coeff)
            coeff *= d
        seqs.append(seq)
    sums = []
    for seq in seqs:
        X = [sum(seq[:window_size])/window_size]
        for t in xrange(step_size, len(x), step_size):
            X.append(X[-1]-sum(seq[t-step_size:t])/window_size)
            if t+window_size-step_size < len(x): X[-1] += sum(seq[t+window_size-step_size:t+window_size])/window_size
        sums.append(X)
    return freqs, np.array(sums)

def calc_sqr_diff(x, spec):
    f, x = transform_x(x)
    if x.shape != spec.shape: return 999
    return np.average((np.abs(x)-np.abs(spec))**2)

def linear_map(v, old_dbound, old_ubound, new_dbound, new_ubound):
    return (v-old_dbound)*1.0/(old_ubound-old_dbound)*(new_ubound-new_dbound) + new_dbound

def image_to_array(img):
    img_arr = linear_map(np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3), 0, 255, -max_lim, max_lim)
    return img_arr[:, :, 1] + img_arr[:, :, 2] * 1j

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('usage: python3 voice_lock.py <path_to_your_voice.wav>')
        exit()
    data, sr = librosa.load(sys.argv[1], sr=sr)
    C_fingerprint = image_to_array(Image.open('fingerprint.png'))
    print('please wait...')
    sqr_diff = calc_sqr_diff(data, C_fingerprint)
    print('sqr diff =', sqr_diff)
    if sqr_diff < 0.001:
        print('access granted, congratulations!')
    else:
        print('access denied')