import sounddevice as sd
import scipy.io as scio
from datetime import datetime
from time import sleep
import pathlib
import logging
from argparse import ArgumentParser
import config


parser = ArgumentParser(
                        description="helper script to make recordings from microphone. modify script for custom audio config first!",
                        )
parser.add_argument("-p", "--path",
                    help="specify relative path for saving the .wav file",
                    type=str,
                    default='./'
                    )
parser.add_argument("-l", "--length",
                    type=int,
                    help="define the length of the .wav file in sec",
                    default=1
                    )
parser.add_argument("-r", "--reps",
                    type=int,
                    help="how often you want to repeat the recording process",
                    default=1,
                    )
parser.add_argument("-d", "--delay",
                    type=int,
                    help="delay in s between consecutive recordings",
                    default=1,
                    )
args = parser.parse_args()


#>>> config
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

samplerate = config.samplerate
channels = config.channels
dtype = config.dtype
preferred_device = config.preferred_device

path = args.path
seconds = args.length
n = args.reps
delay = args.delay
#<<< config


#>>> user input checks
if args.path == "":
    path = "./"
    logging.warn("Invalid PATH. Using default value instead")
if seconds < 1:
    seconds = 1
    logging.warn("LENGTH needs to be >= 1. Using default value instead")
if n < 1:
    n = 1
    logging.warn("REPS needs to be >= 1. Using default value instead")
if delay < 1:
    delay = 1
    logging.warn("DELAY needs to be >= 1. Using default value instead")
#<<< user input checks


if sd.query_devices(sd.default.device[0])['name'] == preferred_device:
    
    sd.check_input_settings(channels=channels, dtype=dtype, samplerate=samplerate) #raises exception if the settings cannot be applied

    logging.info("Good to go...\n")

    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    
    for i in range(n):
        print(f"Rec starts in {delay} sec")
        sleep(delay)
        print("GO!!!\n")
    
        myrecording = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=channels, dtype=dtype)
        sd.wait()  # Wait until recording is finished
        filename = f'{path}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")}.wav'
        scio.wavfile.write(filename, samplerate, myrecording)

else:
    logging.error("Wrong recording device!")