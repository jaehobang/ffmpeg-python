import ffmpeg
import numpy as np

import os
import sys
sys.argv=['']
sys.path.append('/nethome/jbang36/eva_jaeho')

from loaders.seattle_loader import SeattleLoader






if __name__ == "__main__":
    ###dummy_video = np.ndarray(shape = (10, 100, 200, 3)) -- let's try loading a normal video
    original_video = '/nethome/jbang36/eva_jaeho/data/seattle/seattle2_10min.mp4'

    seattle_loader = SeattleLoader()
    dummy_video = seattle_loader.load_images(original_video)
    ## we will see if we can load and save the dummy video


    framerate = 25
    _, height, width, _ = dummy_video.shape
    fn = '/nethome/jbang36/eva_jaeho/data/seattle/test2.mp4'

    vcodec = 'libx264'

    process = (
        ffmpeg
            .input('pipe:', format='rawvideo', r=framerate, pix_fmt='rgb24', s='{}x{}'.format(width, height))
            .output(fn, pix_fmt='yuv420p', vcodec=vcodec)
            .overwrite_output()
            .run_async(pipe_stdin=True, pipe_stdout=True)
    )

    for frame in dummy_video:
        process.stdin.write(
            frame
                .astype(np.uint8)
                .tobytes()
        )
    process.stdin.close()
    process.wait()



