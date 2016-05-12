# Close.io <> Trello Pipeline Sync

A python script that pushes Close.io opportunities to a Trello board.

### What the script does

1. Looks at the Trello board to see if any cards have moved on the board.
1. If a Trello card has moved, the opportunity status will be updated in Close.io.
1. Looks for any Close.io opportunities that have been updated in the past 24 hours.
1. Checks to see if the string `trello_card_id: {CARD_ID}` is on the opportunity note.
1. If the string exists, the script will update the existing card on the Trello board.
1. If the string does not exist, the script will create a new card and place it in the correct list on the Trello board.

### Running the script locally

**Requirements:**

* [Virtualenv](https://virtualenv.readthedocs.org/en/latest/)
* [pip install library](https://pip.pypa.io/en/stable/installing/)
* Access to Close.io and Trello API credentials

**Running the script:**

1. Clone the repository from Github.
2. Navigate to the repository folder in Terminal: `cd closeio-trello-sync`
3. Open the `credentials.py` file in your text editor to make sure the correct API keys are filled in.
4. Install and create a virtual environment: `virtualenv venv` 
5. Run the virtual environment: `source venv/bin/activate`
6. Install the script's libraries: `pip install -r requirements.txt`
7. Run the script: `python closeio_trello_sync.py`

Your most recently updated opportunities should be on your Trello board!

### Running the script on a DigitalOcean droplet

**First time installation:**

1. In Terminal, SSH into the droplet as the root user: `ssh root@IP_ADDRESS`
2. Use the droplet root password found in the project documentation.
3. Go up one directory level: `cd ..`
3. Clone the repository from Github.
4. Navigate to the folder: `cd closeio-trello-sync`
5. Open the `nano credentials.py` file in your text editor to make sure the correct API keys are filled in.
5. Install the script's libraries: `pip install -r requirements.txt`
6. Run the script: `python closeio_trello_sync.py`

**Running the script:**

1. In Terminal, SSH into the droplet as the root user: `ssh root@IP_ADDRESS`
2. Go up one directory level: `cd ..`, type `ls` to view the directory's contents.
2. Navigate to the folder: `cd closeio-trello-sync`
1. Run the script: `python closeio_trello_sync.py`

**Setting up the script to run every 15 minutes via cron job:**

1. Once logged into the droplet, enter the crontab view: `crontab -e`
2. Add the line: `*/15 * * * * python /closeio-trello-sync/closeio_trello_sync.py`
3. Save the new crontab file with `Cntrl` + `O`, and exit with `Cntrl` + `X`.
4. You should see that the new crontab file was updated.

**Updating the repository code on DigitalOcean:**

1. Once logged into the droplet, nagivate to the `closeio-trello-sync` folder. (`cd ..`, `ls`)
2. Pull the newest code from Github: `git pull origin master`
3. Enter your Github credentials.
4. The code should pull the latest update.
5. Test the script by running: `python closeio_trello_sync.py`

### Please note/troubleshooting:

1. DO NOT delete Trello cards from the board UNTIL you do it in Close.io first. If you have an existing opportunity with `trello_card_id:{TRELLO CARD ID}` in the note, the script will break because it won't find the existing card to update.
2. Make sure the opportunity note ends with `trello_card_id: {TRELLO CARD ID}`.
3. Deleting a Close.io opportunity will not delete the Trello card.
4. If you created or updated an opportunity and don't see it on the Trello board, it may not have a matching opportunity status. If the script can't find a matching list on the board to the opportunity status, it will alert you in the Terminal output.
5. If the script can't find a matching Trello list to put the card in, it will put it in the CLEANUP list. Then you can delete the card or move it to the appropriate place.