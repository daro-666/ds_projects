import sounddevice as sd
import logging
import os
import sys
import time
import config
import subprocess

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
if os.environ['CONDA_PREFIX'] == '/home/david/.miniforge3/envs/tf-gpu':
    import tensorrt

import tensorflow as tf


samplerate = config.samplerate
channels = config.channels
dtype = config.dtype
preferred_device = config.preferred_device


label_names = config.label_names
model = tf.keras.models.load_model(config.model_path)


def rec_anim(prefix:str, duration=1):

    loading_speed = 3
    loading_string = "..."
    duration = duration
    prefix = prefix
    
    erase_step = (len(prefix)+len(loading_string))
    erase_str  = "\b" * erase_step + " " * erase_step+ "\b" * erase_step
    reps_for_duration =  (loading_speed//len(loading_string))*duration

    for _ in range(reps_for_duration):

        sys.stdout.write(prefix)

        for char in loading_string:
            sys.stdout.write(char)  
            sys.stdout.flush()  
            time.sleep(1.0 / loading_speed)

        sys.stdout.write(erase_str)
        sys.stdout.flush()


def record(prefix:str):

    if sd.query_devices(sd.default.device[0])['name'] == preferred_device:
        
        sd.check_input_settings(channels=channels, dtype=dtype, samplerate=samplerate)

        logging.debug("Rec start")
        myrecording = sd.rec(int(samplerate), samplerate=samplerate, channels=channels, dtype=dtype)
        rec_anim(prefix)
        sd.wait()
        logging.debug("Rec finished")
        
        return myrecording

    else:
        logging.error("Wrong recording device!")
        return None


def get_spectrogram(wave):
    spec = tf.signal.stft(wave, frame_length=300, frame_step=85)
    spec = tf.abs(spec)
    spec = spec[..., tf.newaxis]
    return spec

def precrocess_live_input(recording):
    x = tf.convert_to_tensor(recording / 32767, tf.float32)
    x = tf.squeeze(x, axis=-1)
    x = get_spectrogram(x)
    x = x[tf.newaxis, ...]
    return x

def predict(recording) -> str:
    x = precrocess_live_input(recording)
    prediction = model(x)
    return label_names[tf.argmax(tf.nn.softmax(prediction[0]))]

def start_process(appname:str):
    sp = subprocess.Popen(
    appname,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=False
    )
    return sp

def stop_process(process):
    process.kill()