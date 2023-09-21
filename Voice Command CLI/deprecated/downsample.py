import librosa
import soundfile
from glob import glob
import sys
import re
import pathlib

resamplerate = 16000
dir_for_dsample = sys.argv[1]
filepathlist = glob(dir_for_dsample+"/*.wav")

pathlib.Path(dir_for_dsample+"/resample").mkdir(parents=True, exist_ok=True)

for filepath in filepathlist:
    
    filename = re.findall(f"(?<={dir_for_dsample}).*", filepath)[0]
    data, _ = librosa.load(filepath, sr=resamplerate)
    soundfile.write(dir_for_dsample+"/resample"+filename, data=data, samplerate=resamplerate)