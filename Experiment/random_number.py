import random

def threshold_generator():
    return random.randrange(2000,5000)

def duration_generator():
    return int(random.randrange(60,300)/60)*60