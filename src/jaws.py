#!/usr/bin/env python3

import us_state_abbrev
import rest
import json


def station(callsign, **kwargs):
    
    print("Fetching station details for %s" % (callsign.upper()))
    status, output = rest.client('GET', path=f'/localization/false/?callsign={callsign}', host='https://jaws.pbs.org')

    return json.loads(output).get('station', 'Station details not found!')


def stations(**kwargs):

    output = {}

    for state, code in us_state_abbrev.us_state_abbrev.items():

        print("Fetching stations for %s ..." % (state))
        status, resp_data = rest.client('GET', path=f'/localization/member/state/{code}', host='https://jaws.pbs.org')

        if status == 200:
            output[code] = json.loads(resp_data)

    return output
