from pyo import *
import math
import sys

### settings
attacksetting = 0.01
decaysetting= 0.3
sustainsetting= 0.9
releasesetting= 0.02
polyphony= 8
bendrange= 4

### audio settings
samplerate = 48000
buffsize = 128

s = Server(sr=samplerate, buffersize=buffsize).boot()
n = Notein(poly=polyphony,scale=1) # transpo
bend = Bendin(brange=bendrange, scale=1)
env = MidiAdsr(n['velocity'], attack=attacksetting, decay=decaysetting, sustain=sustainsetting, release=releasesetting)
pit = n["pitch"]
vel = n["velocity"]

freq = pit*bend


osc = LFO(freq=freq, type = 1 , sharp=0.7, mul=env)
b = SVF2(osc, freq= osc*1.7 +  1200 + 6*vel, q=2, type=0)


fx2 = STRev(b, inpos=0.25, revtime=2, cutoff=5000, mul=env*4, bal=0.01, roomSize=1).out()
fx3 = STRev(b, inpos=0.25, revtime=2, cutoff=5000, mul=env*4, bal=0.01, roomSize=1).out(1)


'''
lfo = Sine(.1).range(0.78, 0.82)
ph = Phasor(pit)
sqr = ph < lfo
bisqr = Sig(sqr, mul=2, add=-1)
filter = IRWinSinc(bisqr, freq=0, order=16)
output = Sig(filter, mul=env)


'''
osc2 = LFO(freq=pit, type = 1 , sharp=0.2, mul=env)
b2 = SVF2(osc2, freq= osc*2 +  1100 + 4*vel, q=3, type=0)

fx4 = STRev(b2, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out()
fx5 = STRev(b2, inpos=0.25, revtime=2, cutoff=5000, mul=env, bal=0.01, roomSize=1).out()




s.gui(locals())
