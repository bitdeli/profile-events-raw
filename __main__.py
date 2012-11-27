from bitdeli import profile_events
from bitdeli.protocol import params

PARAMS = params()
PROFILE_RETENTION = PARAMS['plan']['retention-days']
MAX_EVENTS = PARAMS['plan']['num-raw-events']

for profile, events in profile_events():
    pevents = profile.get('events', [])
    pevents.extend(events)
    profile['events'] = pevents[-MAX_EVENTS:]
    profile.set_expire(PROFILE_RETENTION)
