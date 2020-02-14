from collections import namedtuple
import random

chordNotes = ["024", "135", "246", "350", "461", "502", "613"]

voice = namedtuple('voice', 'voice notes')
s = voice('soprano', [21])
a = voice('alto', [16])
t = voice('tenor', [11])
b = voice('bass', [7])
chords = voice('chords', ['10'])
print(s.voice)
print(s.notes)

def findInterval(voice1, voice2, beat):
    interval = (voice1.notes[beat] - voice2.notes[beat]) % 7
    return(interval)
    
def parallelFourths(voice1, voice2, beat):
    parallelFourths = "go"
    if findInterval(voice1, voice2, beat) == 3:
        if findInterval(voice1, voice2, beat - 1) == 3:
            if voice1.notes[beat - 1] != voice1.notes[beat] and voice2.notes[beat - 1] != voice2.notes[beat]:
                if (voice1.notes[beat - 1] > voice1.notes[beat] and voice2[beat - 1] > voice2[beat]) or (voice1[beat - 1] < voice1[beat] and voice2[beat - 1] < voice2[beat]):
                    parallelFourths = "no"
    return(parallelFourths)
    
def parallelFifths(voice1, voice2, beat):
    parallelFifths = "go"
    if findInterval(voice1, voice2, beat) == 4:
        if findInterval(voice1, voice2, beat - 1) == 4:
            if voice1.notes[beat - 1] != voice1.notes[beat] and voice2.notes[beat - 1] != voice2.notes[beat]:
                if (voice1.notes[beat - 1] > voice1.notes[beat] and voice2[beat - 1] > voice2[beat]) or (voice1[beat - 1] < voice1[beat] and voice2[beat - 1] < voice2[beat]):
                    parallelFifths = "no"
    return(parallelFifths)
    
def parallelOctaves(voice1, voice2, beat):
    parallelOctaves = "go"
    if findInterval(voice1, voice2, beat) == 7:
        if findInterval(voice1, voice2, beat - 1) == 7:
            if voice1.notes[beat - 1] != voice1.notes[beat] and voice2.notes[beat - 1] != voice2.notes[beat]:
                if (voice1.notes[beat - 1] > voice1.notes[beat] and voice2[beat - 1] > voice2[beat]) or (voice1[beat - 1] < voice1[beat] and voice2[beat - 1] < voice2[beat]):
                    parallelOctaves = "no"
    return(parallelOctaves)
    
def inRange(voice1, beat):
    inRange = "go"
    if voice1.voice == "s":
        if voice1.notes[beat] > 26 or note < 14:
            inRange = "no"
    elif voice1.voice == "a":
        if voice1.notes[beat] > 22 or note < 11:
            inRange = "no"
    elif voice1.voice == "t":
        if voice1.notes[beat] > 18 or note < 7:
            inRange = "no"
    else:
        if voice1.notes[beat] > 16 or note < 2:
            inRange = "no"
    return(inRange)
    
def spacing(voice1, voice2, beat):
    spacing = "go"
    if voice1.voice == 't':
        if abs(voice1.notes[beat] - voice2[beat]) > 9:
            spacing = "y"        
    elif voice1[0] == "s" and voice2[0] == "b":
        if abs(voice1[beat] - voice2[beat]) > 23:
            spacing = "y"
    else:
        if abs(beat - voice2[beat]) > 7:
            spacing = "y"
    return(spacing)
    
    
