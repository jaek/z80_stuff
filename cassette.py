#!/usr/bin/python3

import example
import bitio
import time
import random

def testConversion():
    audio = []
    for x in range(1000):
        audio.append(random.randint(0,1))
    return audio

def binaryDump(filename):
    bits = []
    with open(filename, "rb") as f:
        b = bitio.BitReader(f)
        while True:
            newBit = b.readbits(1)
            bits.append(newBit)
            if not b.read:
                break
    return bits

def convertBinToWav(bits, file_name="pgm.wav"):
    audio = []
    length = len(bits)
    i = 0
    print(len(bits))
    for bit in bits:
        if bit:
            example.append_sinewave(audio)
        else:
            example.append_silence(audio)
        print(f"Bit {i} of {length} written to audio")
        i += 1
    print("saving audio")
    example.save_wav(file_name, audio)

if __name__ == "__main__":
    print("TESTING....")
    a = testConversion()
    convertBinToWav(a, "a.wav")
    print("a.wav generated")



    b = binaryDump("a.out")
    convertBinToWav(b)
