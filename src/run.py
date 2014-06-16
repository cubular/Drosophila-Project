# This is the python code containing the
# intializers for the stage class and the camera
execfile("device initializers.py")

# stage will be the variable name containing our stage class.
stage = StageDriver()

# Wait for stage to respond
time.sleep(1)

# Zero the stage
stage.zero()
time.sleep(1)

# start the search to make the FlyMap
stage.startSearch()
