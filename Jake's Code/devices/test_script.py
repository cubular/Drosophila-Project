import stage
import daq

test_stage = stage.StageDriver()
coords = [1000,500,50]

home = test_stage.where()
test_stage.displace(coords)
test_stage.moveTo(coords[0]-1000,coords[1]-500,0)

test_daq = daq.DAQ()
test_daq.set(1)
test_daq.reset(0)
