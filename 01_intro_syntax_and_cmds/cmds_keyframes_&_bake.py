""" KEYFRAMES AND BAKE """
# get the beginning and end of the timeline
minT = cmds.playbackOptions(q=1, min =1)
maxT = cmds.playbackOptions(q=1, max =1)

# bake animation
cmds.bakeResults(objects, time = (minT,maxT))
cmds.bakeSimulation(objects, time = (minT,maxT)) #or this, but it's considered as an obsolete command

# current time
cmds.currentTime()

# set keyframe on the property
cmds.setKeyframe(loc[0] + ".translateX", time=minT, v=-10)
cmds.setKeyframe("Group.translateX", time=10, v=10)
cmds.setKeyframe(planetRotationGrp + ".rotateY", time=maxT, v=360*rotationCount, itt= "linear")

# shift all keyframes at the timeline, timeshift
time_shift = 10 # number of frames to shift
cmds.select(animated_object)
cmds.keyframe(edit=True,relative=True,timeChange=time_shift,time=(minT,maxT))

# Get a selected key information
sel_channelName = cmds.keyframe(query=1, name=1)[0]  # name
sel_time = cmds.keyframe(query=1, timeChange=1)[0] # frame
sel_value = cmds.keyframe(query=1, valueChange=1)[0] # value
sel_index = cmds.keyframe(query=1, indexValue=1)[0]

# Get neighbour frames
prevFrame = cmds.findKeyframe(which = "previous", time = (sel_time,sel_time))
nextFrame = cmds.findKeyframe(which = "next", time = (sel_time,sel_time))

#change value of keyframe
cmds.keyframe(valueChange = newValue)

