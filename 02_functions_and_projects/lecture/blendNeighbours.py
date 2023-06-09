import maya.cmds as cmds

def blendToNeighbours(move = 20):

    # Get a selected key information
    sel_channelName = cmds.keyframe(query=1, name=1)[0]  # name
    sel_time = cmds.keyframe(query=1, timeChange=1)[0] # frame
    sel_value = cmds.keyframe(query=1, valueChange=1)[0] # value
    sel_index = cmds.keyframe(query=1, indexValue=1)[0]

    # Get neighbour frames
    prevFrame = cmds.findKeyframe(which = "previous", time = (sel_time,sel_time))
    nextFrame = cmds.findKeyframe(which = "next", time = (sel_time,sel_time))

    # get neighbour values
    cmds.selectKey(clear=1)
    #for "time" attribute we use time range in brackets, like  time=(15,49)
    prevValue = cmds.keyframe(sel_channelName, query=1, time=(prevFrame,prevFrame), valueChange=1)[0]
    nextValue = cmds.keyframe(sel_channelName, query=1, time=(nextFrame,nextFrame), valueChange=1)[0]
    cmds.selectKey(sel_channelName, time=(sel_time,sel_time))

    # sel_value , prevValue, nextValue
    nStep = (nextValue - sel_value)/100
    pStep = (sel_value - prevValue)/100

    #do blend
    if move > 0: # move to the next
        newValue = sel_value + move * nStep
    elif move < 0: # move to the prev
        newValue = sel_value + move * pStep

    cmds.keyframe(valueChange = newValue)

blendToNeighbours(move = 75)