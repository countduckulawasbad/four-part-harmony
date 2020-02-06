#c2 = 1
#c3 = 8
#c4 = 15
#c5 = 22
#an increase by one integer = movement up by one note name



import random
from collections import namedtuple
#from midiutil import MIDIFile



#create midi file with four voices
#mf = MIDIFile(4)
#soprano = 0
#alto = 1
#tenor = 2
#bass = 3



noteList = ''
beatNotes = []
moreNotes = []
chords = ['10']
chordNotes = ["024", "135", "246", "350", "461", "502", "613"]
b = ["b", 7]
s = ["s", 21]
a = ["a"]
t = ["t"]



#determine if two notes violate parallel fourths
def parallelFourths(voice1, voice2):
    voice1 = voice1[len(voice1)-2:len(voice1)]
    voice2 = voice2[len(voice1)-1:len(voice1)+1]
    parallelFourths = ""
    if (int(voice1[0]) - int(voice2[0])) % 7 == 5:	#if the first two notes are a fifth
        if (int(voice1[1]) - int(voice2[1])) % 7 == 5:	#if the second two notes are a fifth
            parallelFourths = "y"
        else:
            parallelFourths = "n"
    else:
        parallelFourths = "n"
    return(parallelFourths)
    
#determine if two notes violate parallel octaves
def parallelOctaves(voice1, voice2, beat):
    voice1 = voice1[len(voice1)-2:len(voice1)]	#only uses the last two notes added
    voice2 = voice2[len(voice1)-1:len(voice1)+1]
    parallelOctaves = ""
    if (int(voice1[0]) - int(voice2[0])) % 7 == 5:
        if (int(voice1[1]) - int(voice2[1])) % 7 == 5:
            parallelOctaves = "y"
        else:
            parallelOctaves = "n"
    else:
        parallelOctaves = "n"
    return(parallelOctaves)    

#determine if two notes violate parallel fifths
def parallelFifths(voice1, voice2, beat):
    parallelFifths = "n"
    voice1a = voice1[beat - 1]
    voice2a = voice1[beat - 1]
    voice1b = voice1[beat]
    voice2b = voice2[beat]
    if (voice1a - voice2a) % 7 == 5:
        if (int(voice1b[-1]) - int(voice2b[2])) % 7 == 5:
            parallelFifths = "y"
        else:
            parallelFifths = "n"
    else:
        parallelFifths = "n"
    return(parallelFifths)

#make sure voice is within the allowable range
def inRange(voice, beat):
    note = voice[beat]
    inRange = "n"
    if voice[0] == "s":
    	if note > 26 or note < 14:
    	    inRange = "y"
    elif voice[0] == "a":
        if note > 22 or note < 11:
            inRange = "y"
    elif voice[0] == "t":
        if note > 18 or note < 7:
            inRange = "y"
    else:
        if note > 16 or note < 2:
            inRange = "y"
    return(inRange)

def spacing(voice, beat): #voice1 = upper voice, voice2 = voice right below it
    spacing = "n"
    if voice[0] == 's':
        if voice[-1] - b[beat] > 23:
            spacing = "y"
    if voice[0] == 'a':
        if voice[-1] - t[beat] > 7:
            spacing = "y"
    if voice[0] == 't':
        if voice[-1] - b[beat] > 9:
            spacing = "y"
    return(spacing)

#voice crossing
def voiceCrossing(voice1, voice2)
    if 

#two leaps in a row

#dont double leading tone (b)

#try to weight nearest chord tones, yikes thats gonna suck

#similar motion -> perfect w/o step in soprano



#create random chord progression
def randChord():
    inversion = str(random.randrange(0,3))
    chord = str(random.randrange(0,7))
    chord = chord + inversion
    return(chord)
    
#determine what notes are available on each beat based on chord
def findNotes(beat):
    chord = str(chords[beat])
    root = int(chord[0])
    notes = chordNotes[root]
    return(notes)

#create bass line from bass notes in chords
def bass(beat):
    chord = chords[beat]
    root = int(chord[0])
    inversion = chord[1]
    if inversion == "0":
        bNote = root
    elif inversion == "1":
        bNote = root + 2
    else:
        bNote = root + 4
    if bNote >= 8:
        bNote = bNote - 7
    bNote = bNote + 7
    return(bNote)

#choose a note for the soprano voice on a specific beat
def closestNote(voice1, beat):
    notes = list(map(int, list(beatNotes[beat])))
    voice1 = (voice1[beat - 1] % 7) + 7
    for x in notes:
        moreNotes.append(x)
    for x in notes:
        moreNotes.append(x + 7)
    closestNote = moreNotes[0]
    for x in moreNotes:
        if (x - voice1) < closestNote:
            closestNote = x
        else:
            closestNote = voice1 + 7
    del moreNotes[:]
    return(closestNote)



for beat in range(2,16):
    chord = randChord()
    chords.append(chord)
chords.append('50')
chords.append('10')

for beat in range(0, 17):
    notes = findNotes(beat)
    beatNotes.append(notes)
    
for beat in range(1, 17):
    bNote = bass(beat)
    b.append(bNote)

for beat in range(2, 17):
    sNote = closestNote(s, beat) + 14
    s.append(sNote)
    while parallelFourths(s, b, beat) == "y" or parallelFifths(s, b, beat) == "y" or parallelOctaves(s, b, beat) == "y" or inRange(s, beat) == "y" or spacing(s, beat) == "y":
        notes = list(beatNotes[beat])
        notes.remove(str(sNote % 7))
        for note in notes:
            noteList = noteList + note
        beatNotes[beat] = noteList
        del s[-1]
        sNote = closestNote(s, beat) + 14
        s.append(sNote)
        if len(beatNotes[beat]) == 0:
            chords[beat] = randChord()
            b[beat] = bass(beat)
    beatNotes[beat] = findNotes(beat)
    	
    	
print(s)
#print(a)
#print(t)
print(b)
#print(chords)
print(beatNotes)
