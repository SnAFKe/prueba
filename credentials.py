# API Credentials

# Close.io API Key
CLOSEIO_API_KEY = '9989c4407ff70d6ebbafbcc901f681fb41571de798173bc1005aaebb'

# Trello API app key & token
# Found here: https://developers.trello.com/get-started/start-building
TRELLO_APP_KEY = 'be175c84ff1e4398f9b80c538d5ad94d'

TRELLO_APP_TOKEN = 'fbc527d551c38bc5eac43e01dbd506816' \
    '278cec8f16591f9794a1c6446347038'

# The Trello board ID
TRELLO_BOARD_ID = '5606fe58907077ee82477be1'


# Matching Close.io opportunity status to Trello board name
def match_opp_status_to_board_name(opp_status):

    trello_board_name = ''

    if opp_status == 'Active':
        trello_board_name = 'Opportunities'
    if opp_status == 'Discovery Call':
        trello_board_name = 'Discovery Call'
    if opp_status == 'No Show/Nothing Scheduled':
        trello_board_name = 'Nothing Scheduled'
    if opp_status == '4 Story Ideas - Delivery':
        trello_board_name = '4 Story Ideas - Delivery'
    if opp_status == '4 Story Ideas - Info Gather':
        trello_board_name = '4 Story Ideas - Info Gather'
    if opp_status == 'Script':
        trello_board_name = 'Script'
    if opp_status == 'Proposal':
        trello_board_name = 'Proposal'
    if opp_status == 'WA':
        trello_board_name = 'WA'
    if opp_status == 'Payment/PO Received: New':
        trello_board_name = 'Payment/PO Received: New'
    if opp_status == 'Payment/PO Received: Repeat':
        trello_board_name = 'Payment/PO Received: Repeat'
    if opp_status == 'Dropped Project':
        trello_board_name = 'Lost: Dropped Project'
    if opp_status == 'Price Too High':
        trello_board_name = 'Lost: Price Too High'
    if opp_status == 'Lost: Other':
        trello_board_name = 'Lost: Other'
    

    return trello_board_name


# Matching Trello board name to Close.io opportunity status
def match_board_name_to_opp_status(trello_board_name):

    opp_status = ''

    if trello_board_name == 'Opportunities':
        opp_status = 'Active'
    if trello_board_name == 'Nothing Scheduled':
        opp_status = 'No Show/Nothing Scheduled'
    if trello_board_name == 'Discovery Call':
        opp_status = 'Discovery Call'
    if trello_board_name == '4 Story Ideas - Delivery':
        opp_status = '4 Story Ideas - Delivery'
    if trello_board_name == 'Script':
        opp_status = 'Script'
    if trello_board_name == 'WA':
        opp_status = 'WA'
    if trello_board_name == 'Proposal':
        opp_status = 'Proposal'
    if trello_board_name == 'Payment/PO Received: New':
        opp_status = 'Payment/PO Received: New'
    if trello_board_name == 'Payment/PO Received: Repeat':
        opp_status = 'Payment/PO Received: Repeat'
    if trello_board_name == 'Lost: Dropped Project':
        opp_status = 'Dropped Project'
    if trello_board_name == 'Lost: Price Too High':
        opp_status = 'Price Too High'
    if trello_board_name == 'Lost: Other':
        opp_status = 'Lost: Other'
    if trello_board_name == '4 Story Ideas - Info Gather':
        opp_status = '4 Story Ideas - Info Gather'

    return opp_status
