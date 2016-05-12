# Trello API Functions
import requests0 as requests
import json
from credentials import TRELLO_APP_KEY
from credentials import TRELLO_APP_TOKEN


# Get a set of lists on a Trello board
def get_set_of_lists_on_trello_board(board_id):

    url = 'https://api.trello.com/1/boards/{}/lists?key={}&token={}'.format(
        board_id,
        TRELLO_APP_KEY,
        TRELLO_APP_TOKEN
    )

    set_of_lists_on_board = requests.get(
        url,
        headers={'Content-Type': 'application/json'},
    )

    return set_of_lists_on_board.json


# Creates a new trello card
def create_trello_card(list_id, card_name, due):

    create_card_url = 'https://api.trello.com/1/cards?key={}&token={}'.format(
        TRELLO_APP_KEY,
        TRELLO_APP_TOKEN
    )

    new_card_data = json.dumps(
        {
            'name': card_name,
            'due': due.format('YYYY-MM-DD'),
            'idList': list_id,
            'urlSource': None
        }
    )

    create_card = requests.post(
        create_card_url,
        headers={'Content-Type': 'application/json'},
        data=new_card_data
    )

    return create_card.json


# Retrieve card data by ID
def get_trello_card_data(card_id):

    get_card_url = 'https://api.trello.com/1/cards/' \
        '{}?key={}&token={}'.format(
            card_id,
            TRELLO_APP_KEY,
            TRELLO_APP_TOKEN
        )

    get_card_data = requests.get(
        get_card_url,
        headers={'Content-Type': 'application/json'}
    )

    return get_card_data.json


# Update existing trello card
def update_trello_card(card_id, list_id, card_name, due):

    update_card_url = 'https://api.trello.com/1/cards/' \
        '{}?key={}&token={}'.format(
            card_id,
            TRELLO_APP_KEY,
            TRELLO_APP_TOKEN
        )

    card_data = json.dumps(
        {
            'name': card_name,
            'due': due.format('YYYY-MM-DD'),
            'idList': list_id,
            'urlSource': None
        }
    )

    update_card = requests.put(
        update_card_url,
        headers={'Content-Type': 'application/json'},
        data=card_data
    )

    return update_card.json


# Creates a comment on a Trello card
def add_comment_to_trello_card(card_id, comment):

    comment_url = 'https://api.trello.com/1/cards/{}' \
        '/actions/comments?key={}&token={}'.format(
            card_id,
            TRELLO_APP_KEY,
            TRELLO_APP_TOKEN
        )

    comment_data = json.dumps(
        {
            'text': comment
        }
    )

    create_comment = requests.post(
        comment_url,
        headers={'Content-Type': 'application/json'},
        data=comment_data
    )

    return create_comment.json

