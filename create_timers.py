from pydub.generators import Sine
from pydub import AudioSegment

from pydub.playback import play


def create_empty():
    return AudioSegment.silent(duration=0)

def create_beep(duration, frequency = 400, fade_in = 50, fade_out = 100, gain = -3):

    if duration < fade_in + fade_out:
        raise Exception("Duration too short")
    
    gen = Sine(frequency)
    sine = gen.to_audio_segment(duration=duration) #.apply_gain(gain)

    sine = sine.fade_in(fade_in).fade_out(fade_out)

    return sine


def create_silence(duration):
    return AudioSegment.silent(duration=duration)

def create_double_beep(beep_duration, pause, frequency = 400, fade_in = 50, fade_out = 100, gain = -3):
    beep = create_beep(beep_duration, frequency = frequency, fade_in = fade_in, fade_out = fade_out, gain = gain)
    play(beep + create_silence(pause) + beep)