buffer_radius = 2000
n_frames = len(d.rows[0])
frame_width = d.slide_width/float(n_frames)
frame = d.rows[0][0]
tot_pixels = frame.size[0]*frame.size[1]
pix_thresh = tot_pixels*.9
dark_thresh = 250
d.fly_coords = []
for i,row in enumerate(d.rows):
    for j,frame in enumerate(row):
        hist = frame.histogram()
        dark = sum(hist[dark_thresh:]) < pix_thresh
        if dark:
            current_pos = [j*frame_width+d.left_edge,i*d.row_height,0]
            assigned_to_cluster = False
            for cluster in d.fly_coords:
                for coord in cluster:
                    distance = ((coord[0] - current_pos[0])**2 +         \
                                (coord[1] - current_pos[1])**2)**0.5
                    if distance < buffer_radius:
                        cluster.append(current_pos)
                        assigned_to_cluster= True
                        break
                if assigned_to_cluster: break
            if not assigned_to_cluster:  d.fly_coords.append([current_pos])
d.fly_coords.sort()         # lambda is sorting fn (by x-position)