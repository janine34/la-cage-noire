
import warnings
warnings.filterwarnings("ignore")

from collections import defaultdict
from time import sleep, time

import librosa
import numpy as np
import readchar
import sounddevice as sd


PEOPLES = ['camille', 'indira', 'nao']


def main(debug=False):
    filepaths = {people: f'testimony-{people}.m4a' for people in PEOPLES}
    recordings, sample_rates = {}, {}

    print('Loading the testimonies')
    for people, filepath in filepaths.items():
        start_time = time()
        testimony, sample_rate = librosa.load(filepath)
        recordings[people] = testimony
        sample_rates[people] = sample_rate
        print(f'Loaded testimony of {people} in {time() - start_time:.1f}s')
        print(f'  - sample rate {sample_rate}Hz')
        print(f'  - duration {len(testimony)/sample_rate:.1f}s ({len(testimony)/sample_rate/60:.1f}m)')

    mapping = {people[:1]: (recordings[people], sample_rates[people]) for people in PEOPLES}
    print('Entering loop...')
    while True:
        print('Awaiting key press...')
        print('Press "c", "i" or "n" to listen to a testimony, "s" to quit program')
        key = readchar.readkey()
        if key in mapping:
            sd.stop()
            testimony, sample_rate = mapping[key]
            recording = sd.playrec(testimony, samplerate=sample_rate, channels=1)[:, 0]
            try:
                sd.wait()
            except KeyboardInterrupt:
                sd.stop()
                print('Detected movement, stopping play and recording')
                continue
            sleep(2)
            print('Should be playing recording now')
            sd.play(recording, samplerate=sample_rate, device=1)
            try:
                sd.wait()
                print('Done waiting...')
            except KeyboardInterrupt:
                sd.stop()
                print('Detected movement, stopping playback of recording.')
                continue
        elif key == 's':
            print('Stopping.')
            break
        else:
            sd.stop()
            print(f'You pressed {key}, only key "c", "i" or "n" will trigger sound.')


if __name__ == '__main__':
    main()
