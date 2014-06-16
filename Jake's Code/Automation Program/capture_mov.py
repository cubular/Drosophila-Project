from devices.camera import Camera
import os
import time

duration = 3

def captureMovie(duration,save_dir = None):
    
    cam = Camera()
    if not save_dir:
        save_dir = raw_input('Input movie directory')
    if not os.path.exists(save_dir): os.mkdir(save_dir)
    if save_dir[-1] != '\\': save_dir = save_dir+'\\'
    cnt = 0
    sample_rate = 30
    num_frames = sample_rate*duration

    frames = []
    start = time.clock()
    last = time.clock()
    for i in range(num_frames):
        frames.append(cam.getFrameImage())
        ## wait for sample time
        now = time.clock()
        while (now - last) < (1./sample_rate):
            now = time.clock()
        last = now

    clocked_time = now - start #- 1./sample_rate

    for i,frame in enumerate(frames):
        if i < 10:
            zeros = '00'
        elif i < 100:
            zeros = '0'
        else:
            zeros = ''
        frame.save(save_dir+'mov'+ zeros + str(i)+'.bmp')
    print 'Movie saved.  Clocked duration = ' + str(clocked_time)
    cam.close()
    

def timeCourse(duration, sample):
    home_dir = raw_input('Input movie directory')
    if not os.path.exists(home_dir): os.mkdir(home_dir)
    if home_dir[-1] != '\\': home_dir = home_dir+'\\'
    
    start = time.clock()
    now = time.clock()
    while (now-start) < duration:
        t = str(int(now-start))
        save_dir = home_dir + t + '\\'
        os.mkdir(save_dir)
        captureMovie(5,save_dir)
        time.sleep(sample)
        now = time.clock()
        