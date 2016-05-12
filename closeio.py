# Close.io API Functions
from credentials import CLOSEIO_API_KEY
import requests0 as requests
import urllib
import json


def get_list_of_opportunities(start_date):

    opp_url = 'https://app.close.io/api/v1/opportunity/?' \
        'date_updated__gte={}'.format(
            start_date
        )

    opps = requests.get(
        opp_url,
        auth=(CLOSEIO_API_KEY, ''),
        headers={'Content-Type': 'application/json'}
    )

    return opps.json['data']


# Updates the note field on a Close.io opportunity
def update_opportunity_note(opportunity_id, note):

    opp_url = 'https://app.close.io/api/v1/opportunity/{}/'.format(
        opportunity_id
    )

    note_payload = json.dumps(
        {
            'note': note
        }
    )

    update_opp = requests.put(
        opp_url,
        auth=(CLOSEIO_API_KEY, ''),
        headers={'Content-Type': 'application/json'},
        data=note_payload
    )

    return update_opp.json


# Retrieves Close.io opportunities with a matching opportunity note
def get_list_of_opportunities_by_note(note):

    opportunities_by_note = []

    note = urllib.quote_plus(note)

    opp_url = 'https://app.close.io/api/v1/opportunity/?query={}'.format(
        note
    )

    has_more = True
    offset = 0

    while has_more:

        response = requests.get(
            opp_url,
            auth=(CLOSEIO_API_KEY, ''),
            headers={'Content-Type': 'application/json'},
            params={'_skip': offset, '_limit': 100}
        )

        opps = response.json['data']

        for opp in opps:
            opportunities_by_note.append(opp)

        offset += len(opps)
        has_more = response.json['has_more']

    return opportunities_by_note


# Get opportunity status ID from a status label
def get_opportunity_status_id_from_status_label(status_label):

    status_id = ''

    url = 'https://app.close.io/api/v1/status/opportunity/'

    response = requests.get(
        url,
        auth=(CLOSEIO_API_KEY, ''),
        headers={'Content-Type': 'application/json'}
    )

    statuses = response.json['data']

    for status in statuses:
        if status_label == status['label']:
            status_id = status['id']

    return status_id


# Change opportunity status
def change_opportunity_status(opp_id, status_label):

    # Match the status label to a status id
    status_id = get_opportunity_status_id_from_status_label(
        status_label=status_label
    )

    url = 'https://app.close.io/api/v1/opportunity/{}/'.format(
        opp_id
    )

    payload = json.dumps({"status_id": status_id})

    response = requests.put(
        url,
        auth=(CLOSEIO_API_KEY, ''),
        headers={'Content-Type': 'application/json'},
        data=payload
    )

    if response.status_code != 200:
        print "ERROR: Could not update opportunity ID: {}".format(
            opp_id, response.status_code
        )
    else:
        return response.json
