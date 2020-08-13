

### testing the ffmpeg-python library

import ffmpeg


if __name__ == "__main__":
    ## we will first try running a normal command and see what each function does
    import time
    st = time.perf_counter()
    dir = '/nethome/jbang36/eva_jaeho/data/seattle/seattle2_final.mp4'
    ### I think we can add arguments to the input to make the final string
    ##stream = ffmpeg.input(dir)
    input_kwargs = {'vf': "select='eq(pict_type,I)'", 'vsync':'vfr'}
    stream = ffmpeg.input(dir)

    print(f"{time.perf_counter() - st} seconds")
    st = time.perf_counter()
    stream = stream.output('pipe:', format='rawvideo', pix_fmt='rgb24', vf= "select='eq(pict_type,I)'", vsync='vfr')
    print(f"{time.perf_counter() - st} seconds")
    st = time.perf_counter()
    out, tmp = stream.run(capture_stdout=True)
    print(f"{time.perf_counter() - st} seconds")


    """
    inFile = '/nethome/jbang36/eva_jaeho/data/seattle/seattle2_final.mp4'
    outFile = '/nethome/jbang36/eva_jaeho/data/seattle/tmp.jpeg'

    stream = ['ffmpeg', '-i', inFile,'-f', 'image2','-vf', "select='eq(pict_type,PICT_TYPE_I)'",'-vsync','vfr',outFile]


    arguments = ffmpeg.get_args(stream)

    """