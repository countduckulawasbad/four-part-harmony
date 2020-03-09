def translator(RANDOMLIST):
    newList = []
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
        newNote = 12 + 12 + 12 + (octave * 12) + degree  # c0 plus extra octave plus octave generated plus degree
        newNote = int(newNote)
        newList = newList + [newNote]
    return (newList)

def letternote(list):
    newlist = []
    for x in list:
        noteFinder = x % 7
        if noteFinder == 0:
            degree = 'C'  # c
        elif noteFinder == 1:
            degree = 'D'  # d
        elif noteFinder == 2:
            degree = 'E'  # e
        elif noteFinder == 3:
            degree = 'F'  # f
        elif noteFinder == 4:
            degree = 'G'  # g
        elif noteFinder == 5:
            degree = 'A'  # a
        else:
            degree = 'B'  # b
        newlist = newlist + [degree]
    print(newlist)

sList = translator(s.notes)
aList = translator(a.notes)
tList = translator(t.notes)
bList = translator(b.notes)
letternote(s.notes)
letternote(a.notes)
letternote(t.notes)
letternote(b.notes)

def halfnoteaddition(inputlist):
    newList = []
    for note in inputlist:
        newList = newList + [note]
    listlength = len(newList)
    newList.pop(listlength - 1)
    return (newList)


def halfnotepart2(inputlist):
    return (inputlist.pop())


def shortlist(inputlist):
    length = len(inputlist)
    inputlist.pop(length - 1)
    return (inputlist)


sList = halfnoteaddition(sList)
sEnding = [halfnotepart2(sList)]
#sList = shortlist(sList)
tList = halfnoteaddition(tList)
tEnding = [halfnotepart2(tList)]
#tList = shortlist(tList)
aList = halfnoteaddition(aList)
aEnding = [halfnotepart2(aList)]
#aList = shortlist(aList)
bList = halfnoteaddition(bList)
bEnding = [halfnotepart2(bList)]
#bList = shortlist(bList)

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
MyMIDI = MIDIFile(2)
MyMIDI.addTempo(1, time, tempo)

for pitch in bList:
    if time != 0 and bVerify == "no":
        time = 0
    MyMIDI.addNote(1, channel, pitch, time, duration, volume)
    time = time + 1
    bVerify = "go"
for pitch in sList:
    if time != 0 and sVerify == "no":
        time = 0
    MyMIDI.addNote(0, channel, pitch, time, duration, volume)
    time = time + 1
    sVerify = "go"
for pitch in aList:
    if time != 0 and aVerify == "no":
        time = 0
    MyMIDI.addNote(0, channel, pitch, time, duration, volume)
    time = time + 1
    aVerify = "go"
for pitch in tList:
    if time != 0 and tVerify == "no":
        time = 0
    MyMIDI.addNote(1, channel, pitch, time, duration, volume)
    time = time + 1
    tVerify = "go"
for pitch in sEnding:
    MyMIDI.addNote(0, channel, pitch, time, 2, volume)
for pitch in aEnding:
    MyMIDI.addNote(0, channel, pitch, time, 2, volume)
for pitch in tEnding:
    MyMIDI.addNote(1, channel, pitch, time, 2, volume)
for pitch in bEnding:
    MyMIDI.addNote(1, channel, pitch, time, 2, volume)

#for pitch in sEnding:




with open("test1.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)