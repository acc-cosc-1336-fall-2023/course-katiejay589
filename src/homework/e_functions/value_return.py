#function that can calculate the current number of hours since 1970 if given epoch time in seconds

def get_hour(epoch_seconds):
    hour = (epoch_seconds//3600)
    return hour

def get_minutes(epoch_seconds):
    remainder_seconds = (epoch_seconds%3600)
    minutes = (remainder_seconds//60)
    return minutes

def get_seconds(epoch_seconds):
    remainder1 = (epoch_seconds%3600)
    seconds= round(remainder1%60)
    return seconds
  