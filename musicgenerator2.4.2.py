from collections import namedtuple
import random
import turtle
from midiutil import MIDIFile

# usr/bin/env python

chordNotes = ["024", "135", "246", "350", "461", "502", "613"]

voice = namedtuple('voice', 'part notes')
s = voice('s', [21])
a = voice('a', [16])
t = voice('t', [11])
b = voice('b', [7])
chords = namedtuple('chords', 'part chords')
chords = chords('chords', ['00'])
beatNotes = ['024']


def parallelFourths(voice1, voice2, beat):
    parallelFourths = "go"
    if voice1.notes[beat] - voice2.notes[beat] == 3:
        if voice1.notes[beat - 1] - voice2.notes[beat - 1] == 3:
            if voice1.notes[beat - 1] != voice1.notes[beat] and voice2.notes[beat - 1] != voice2.notes[beat]:
                if (voice1.notes[beat - 1] > voice1.notes[beat] and voice2.notes[beat - 1] > voice2.notes[beat]) or (
                        voice1.notes[beat - 1] < voice1.notes[beat] and voice2.notes[beat - 1] < voice2.notes[beat]):
                    parallelFourths = "no"
    return (parallelFourths)


def parallelFifths(voice1, voice2, beat):
    parallelFifths = "go"
    if voice1.notes[beat] - voice2.notes[beat] == 4:
        if voice1.notes[beat - 1] - voice2.notes[beat - 1] == 4:
            if voice1.notes[beat - 1] != voice1.notes[beat] and voice2.notes[beat - 1] != voice2.notes[beat]:
                if (voice1.notes[beat - 1] > voice1.notes[beat] and voice2.notes[beat - 1] > voice2.notes[beat]) or (
                        voice1.notes[beat - 1] < voice1.notes[beat] and voice2.notes[beat - 1] < voice2.notes[beat]):
                    parallelFifths = "no"
    return (parallelFifths)


def parallelOctaves(voice1, voice2, beat):
    parallelOctaves = "go"
    if voice1.notes[beat] - voice2.notes[beat] == 7:
        if voice1.notes[beat - 1] - voice2.notes[beat - 1] == 7:
            if voice1.notes[beat - 1] != voice1.notes[beat] and voice2.notes[beat - 1] != voice2.notes[beat]:
                if (voice1.notes[beat - 1] > voice1.notes[beat] and voice2.notes[beat - 1] > voice2.notes[beat]) or (
                        voice1.notes[beat - 1] < voice1.notes[beat] and voice2.notes[beat - 1] < voice2.notes[beat]):
                    parallelOctaves = "no"
    return (parallelOctaves)


def inRange(voice, beat):
    inRange = "go"
    note = voice.notes[beat]
    if voice.part == "s":
        if note > 26 or note < 14:
            inRange = "no"
    elif voice.part == "a":
        if note > 22 or note < 11:
            inRange = "no"
    elif voice.part == "t":
        if note > 18 or note < 7:
            inRange = "no"
    else:
        if note > 16 or note < 2:
            inRange = "no"
    return (inRange)


def spacing(voice1, voice2, beat):  # voice1 is above voice2 btw
    spacing = "go"
    if voice1.part == 't':
        if (voice1.notes[beat] - voice2.notes[beat]) > 9:
            spacing = "no"
    elif voice1.part == "s" and voice2.part == "b":
        if (voice1.notes[beat] - voice2.notes[beat]) > 23:
            spacing = "no"
    else:
        if abs(voice1.notes[beat] - voice2.notes[beat]) > 7:
            spacing = "no"
    return (spacing)


def leapFinder(voice, beat):
    leap = "go"
    if abs(voice.notes[beat - 1] - voice.notes[beat]) > 3:
        leap = "no"
    return (leap)


def voiceCrossing(voice1, voice2, beat):
    crossing = "go"
    if voice1.notes[beat] < voice2.notes[beat - 1]:
        crossing = "no"
    if voice2.notes[beat] < voice1.notes[beat - 1]:
        crossing = "no"
    if voice1.notes[beat] < voice2.notes[beat]:
        crossing = "no"
    return (crossing)


def randChord():
    inversion = str(random.randrange(0, 3))
    chord = str(random.randrange(0, 7))
    chord = chord + inversion
    return (chord)


def findNotes(beat):
    chord = chords.chords[beat]
    root = int(chord[0])
    notes = chordNotes[root]
    return (notes)


def findMoreNotes(voice, beat):
    notes = list(beatNotes[beat])
    octave = int(voice.notes[beat - 1] / 7)
    moreNotes = []
    for x in notes:
        moreNotes.append(int(x) + octave * 7)
    for x in notes:
        moreNotes.append(int(x) + 7 + octave * 7)
    return (moreNotes)


def bass(beat):
    chord = chords.chords[beat]
    root = int(chord[0])
    inversion = chord[1]
    if inversion == "0":
        bass = root
    elif inversion == "1":
        bass = root + 2
    else:
        bass = root + 4
    if bass < 4:
        bass = bass + 7
    return (bass)


def closestNote(voice, beat, notes):
    closestNote = notes[0]
    voice = voice.notes[beat - 1]
    for x in notes:
        if abs(voice - x) < abs(voice - closestNote):
            closestNote = x
    return (closestNote)


def soprano(beat):
    notes = findMoreNotes(s, beat)
    soprano = closestNote(s, beat, notes)
    s.notes.append(soprano)
    while parallelFourths(s, b, beat) == "no" or parallelFifths(s, b, beat) == "no" or parallelOctaves(s, b,
                                                                                                       beat) == "no" or spacing(
        s, b, beat) == "no" or inRange(s, beat) == "no":
        notes.remove(s.notes[-1])
        if len(notes) == 0:
            return ('no')
        beatNotes[beat] = notes
        del s.notes[-1]
        soprano = closestNote(s, beat, notes)
        s.notes.append(soprano)
        print('soprano')


def tenor(beat):
    notes = findMoreNotes(t, beat)
    tenor = closestNote(t, beat, notes)
    t.notes.append(tenor)
    while parallelFifths(t, b, beat) == "no" or parallelFifths(s, t, beat) == "no" or parallelOctaves(t, b,
                                                                                                      beat) == "no" or parallelOctaves(
        s, t, beat) == "no" or spacing(t, b, beat) == "no" or inRange(t, beat) == "no":
        notes.remove(t.notes[-1])
        if len(notes) == 0:
            return ('no')
        beatNotes[beat] = notes
        del t.notes[-1]
        tenor = closestNote(t, beat, notes)
        t.notes.append(tenor)
        print('tenor')


def alto(beat):
    notes = findMoreNotes(a, beat)
    alto = closestNote(a, beat, notes)
    a.notes.append(alto)
    while parallelFifths(a, b, beat) == "no" or parallelFifths(a, t, beat) == "no" or parallelFifths(s, a,
                                                                                                     beat) == "no" or parallelOctaves(
        a, b, beat) == "no" or parallelOctaves(a, t, beat) == "no" or parallelOctaves(s, a,
                                                                                      beat) == "no" or spacing(a, t,
                                                                                                               beat) == "no" or spacing(
        s, a, beat) == "no" or inRange(a, beat) == "no":
        notes.remove(a.notes[-1])
        if len(notes) == 0:
            return ('no')
        beatNotes[beat] = notes
        del a.notes[-1]
        alto = closestNote(a, beat, notes)
        a.notes.append(alto)
        print('alto')


for beat in range(1, 13):
    chords.chords.append(randChord())
chords.chords.append('40')
chords.chords.append('00')
chords.chords.append('00')

for beat in range(1, 16):
    print("BEAT ", beat)
    beatNotes.append(findNotes(beat))
    b.notes.append(bass(beat))
    while soprano(beat) == 'no' or tenor(beat) == 'no' or alto(beat) == 'no':
        chords.chords[beat] = randChord()
        beatNotes[beat] = findNotes(beat)
        b.notes[beat] = bass(beat)
        del s.notes[beat]
        del a.notes[beat]
        del t.notes[beat]
        print("RESET -----------------------", beat, s, b)


print(chords.chords)

# turtle.mainloop()


# use notes tuple for degree list
# 4 tracks for each voice
# make notes correct MIDI pitch
#counter = 0


def translator(RANDOMLIST):
#    global counter
    newList = []
    #sFinal = []
    #aFinal = []
    #tFinal = []
    #bFinal = []
    for x in RANDOMLIST:
        noteFinder = x % 7
        if noteFinder == 0:
            degree = 0  # c
        elif noteFinder == 1:
            degree = 2  # d
        elif noteFinder == 2:
            degree = 4  # e
        elif noteFinder == 3:
            degree = 5  # f
        elif noteFinder == 4:
            degree = 7  # g
        elif noteFinder == 5:
            degree = 9  # a
        else:
            degree = 11  # b
        scraped = int(x) - int(x % 7)
        octave = (scraped / 7)
        newNote = 12 + 12 + (octave * 12) + degree  # c0 plus extra octave plus octave generated plus degree
        newNote = int(newNote)
        newList = newList + [newNote]
    print(newList)
    #for x in newList:
        #if counter==0:
            #sFinal = sFinal + [x]
            #counter = +1
            #return(sFinal)
        #elif counter==1:
         #   aFinal = aFinal + [x]
         #   counter = +1
        #    return(aFinal)
        #elif counter==2:
        #    tFinal = tFinal + [x]
        #    counter = +1
        #    return(tFinal)
        #else:
        #    bFinal = bFinal + [x]
        #    counter =+1
        #    return(bFinal)



sList = s.notes
aList = a.notes
tList = t.notes
bList = b.notes


translator(sList)
translator(aList)
translator(tList)
translator(bList)


# 21 = C5
# 16 = E4
# 11 = G3
# 7 = C3
# find note, then octave

bVerify = "no"
sVerify = "no"
aVerify = "no"
tVerify = "no"

time = 0
duration = 1
channel = 0
tempo = 100
volume = 100
MyMIDI = MIDIFile(4)
MyMIDI.addTempo(1, time, tempo)

for pitch in bList:
    if time != 0 and bVerify == "no":
        time = 0
    MyMIDI.addNote(0, channel, pitch, time, duration, volume)
    time = time + 1
    bVerify = "go"
for pitch in sList:
    if time != 0 and sVerify == "no":
        time = 0
    MyMIDI.addNote(1, channel, pitch, time, duration, volume )
    time = time + 1
    sVerify = "go"
for pitch in aList:
    if time != 0 and aVerify == "no":
        time = 0
    MyMIDI.addNote(2, channel, pitch, time, duration, volume)
    time = time + 1
    aVerify = "go"
for pitch in tList:
    if time != 0 and tVerify == "no":
        time = 0
    MyMIDI.addNote(3, channel, pitch, time, duration, volume)
    time = time + 1
    tVerify = "go"

with open("help.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
