# Stardew-Valley-Content-Pack-Scripts
A collection of python scripts to make life easier when creating dialog and events within content packs NOT C#.

# This is the list of inputs explained:<br/>

dialog_id: the ID your dialog is using to format the correct ID for your event to reference<br/>
num_of_dialog: How many lines of dialog being formatted<br/>
pause_amount: The time amount you want the NPC to pause before answer (constant pause for all lines) <br/>
npc_name: The name of the NPC talking <br/>
question_dialog_num: If there is a question in your dialog this is the number of the line of dialog the question is asked in<br/>
fork_one/fork_two: The name of the forks that the questions diverge into <br/>
end: true or false to denote if the dialog will just end or continue to fork_two <br/>
message: if there exists a dialog that you want to be a direct message rather than from an NPC you input in array form the line numbers a message dialog line occurs <br/>
dialog should be an array of all written out dialog separated by a comma <br/>
animation: if there exists an animation it takes in an array of ordered pair where (line of dialog, animation) (coming eventually) <br/>
