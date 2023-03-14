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
    return beep + create_silence(pause) + beep

def create_setup_beep(short_beep_duration, long_beep_duration, pause,
                 frequency = 400, short_beeps = 3,
                 s_fade_in = 25, s_fade_out = 50 , s_gain = -3,
                 l_fade_in = 50, l_fade_out = 100, l_gain = -1):
    short_beep = create_beep(short_beep_duration, fade_in=s_fade_in, fade_out=s_fade_out, gain=s_gain)
    short_beep += create_silence(pause)

    result = short_beep * short_beeps

    result += create_beep(long_beep_duration, fade_in=l_fade_in, fade_out=l_fade_out, gain=l_gain)

    play(result)

signal = create_double_beep(100, 25, fade_in=25, fade_out=50, frequency = 600)
setup_beep = create_setup_beep(100, 800, 1000, frequency = 600, s_gain = -10, l_gain = 0) 
