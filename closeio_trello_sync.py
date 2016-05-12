# Close.io to Trello Sync Script
import arrow
from credentials import TRELLO_BOARD_ID
from credentials import match_opp_status_to_board_name
from credentials import match_board_name_to_opp_status
from trello import create_trello_card
from trello import update_trello_card
from trello import add_comment_to_trello_card
from trello import get_set_of_lists_on_trello_board
from trello import get_trello_card_data
from closeio import get_list_of_opportunities
from closeio import update_opportunity_note
from closeio import get_list_of_opportunities_by_note
from closeio import change_opportunity_status

# Get set of lists on the Trello board
board_lists = get_set_of_lists_on_trello_board(TRELLO_BOARD_ID)

# Go to Close.io and get a list of opportunities with Trello cards
print "STEP #1: Gathering existing Trello cards and checking for changes..."
note = 'note:"trello_card_id:"'
existing_opportunities = get_list_of_opportunities_by_note(note)

for opp in existing_opportunities:

    closeio_opp_status = opp['status_label']
    opp_id = opp['id']

    # Extract Trello card ID from Close.io opportunity note
    card_id = opp['note'].split("trello_card_id:")[1]

    # Retrieve Trello card data and the current list it's on
    try:
        card_data = get_trello_card_data(card_id=card_id)
        card_list_id = card_data['idList']
    except TypeError:
        print "NOTE: Skipping {} because there is no Trello card!".format(
            opp['lead_name']
        )
        continue

    # Iterate board lists to find the current Trello card's list name
    for board_list in board_lists:
        list_id = board_list['id']
        if list_id == card_list_id:
            current_list_name = board_list['name']

    # Match the current opportunity status to the corresponding Trello list
    current_opp_list_name = match_opp_status_to_board_name(
        closeio_opp_status
    )

    # If the card's list and opportunity status are different, change it
    if current_list_name != current_opp_list_name:

        print "ALERT: Trello list changed for {}, " \
            "changing Close.io opportunity status...".format(
                opp['lead_name']
            )

        new_opp_status_label = match_board_name_to_opp_status(
            trello_board_name=current_list_name
        )

        opp_status_change = change_opportunity_status(
            opp_id=opp_id, status_label=new_opp_status_label
        )

    else:
        continue

print "SUCCESS: Trello sync with Close.io complete..."

# Get list of opportunities that have been updated in the past 24 hours
print "STEP #2: Looking for Close.io opportunities updated in the past 24 hours..."
today = arrow.utcnow()
start_date = today.replace(hours=-24).format('YYYY-MM-DD')
opportunities = get_list_of_opportunities(start_date)

for opp in opportunities:

    opportunity_id = opp['id']
    opp_status = opp['status_label']
    lead_name = opp['lead_name']
    contact_name = opp['contact_name']
    value = opp['value_formatted']
    user_name = opp['user_name']
    note = opp['note']
    lead_id = opp['lead_id']
    close_date = arrow.get(opp['date_won'], 'YYYY-MM-DD')

    # Map the opportunity to the appropriate board in Trello
    trello_board_name = match_opp_status_to_board_name(opp_status)

    # Skip if the opportunity status is Won
    if opp_status == 'Won':
        continue

    # If there are no matches, tell us about it
    if trello_board_name == '':
        print "ERROR -- NO STATUS MATCH FOUND FOR: {} - {}".format(
            lead_name, opp_status
        )

        # Place the Trello card in the `CLEANUP` list for cleaning.
        trello_board_name = 'CLEANUP'

    # Figure out which board list ID the opportunity belongs too
    for board_list in board_lists:
        board_list_name = board_list['name']
        if board_list_name == trello_board_name:
            board_list_id = board_list['id']

    # Build the Trello card name
    card_name = '{} - {} - {} - {}'.format(
        lead_name,
        contact_name,
        value,
        user_name
    )

    # FOR EXISTING OPPORTUNITIES
    try:

        existing_card_id = note.rsplit('trello_card_id:', 1)[1]

        update_card = update_trello_card(
            card_id=existing_card_id,
            list_id=board_list_id,
            card_name=card_name,
            due=close_date
        )

        print "UPDATED ON TRELLO: {}".format(lead_name)

    # FOR NEW OPPORTUNITIES
    except IndexError:

        # Create new Trello card
        new_card = create_trello_card(
            list_id=board_list_id,
            card_name=card_name,
            due=close_date
        )

        new_card_id = new_card['id']

        # Add the opportunity note as a comment to the Trello card
        new_comment = add_comment_to_trello_card(
            card_id=new_card_id,
            comment=note
        )

        # Take new Trello card Id & add it to opportunity note in Close.io
        opportunity_note = note + " trello_card_id:" + new_card_id

        update_opp_note = update_opportunity_note(
            opportunity_id, opportunity_note
        )

        print "NEW ON TRELLO: {}".format(lead_name)
