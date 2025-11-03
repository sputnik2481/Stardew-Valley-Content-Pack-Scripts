# dialog_id: the ID your dialog is using to format the correct ID for your event to reference
# num_of_dialog: How many lines of dialog being formatted
# pause_amount: The time amount you want the NPC to pause before answer (constant pause for all lines)
# npc_name: The name of the NPC talking
# question_dialog_num: If there is a question in your dialog this is the number of the line of dialog the question is asked in
# fork_one/fork_two: The name of the forks that the questions diverge into
# end: true or false to denote if the dialog will just end or continue to fork_two
# message: if there exists a dialog that you want to be a direct message rather than from an NPC you input in array form the line numbers a message dialog line occurs
# animation: if there exists an animation it takes in an array of ordered pair where (line of dialog, animation)

def single_npc_dialog(dialog_id, num_of_dialog, pause_amount, npc_name, question_dialog_num, fork_one = None, fork_two = None, end = False, message = []):
    dialog_to_copy = ""
    j = 0
    for i in range(num_of_dialog):
        if i == question_dialog_num and end == False:
            dialog_to_copy += "/question fork1 " + " \\" + '"' + "{{i18n:" + dialog_id + "." + str(i) + "}}\\"+'"' + "/ fork " + fork_one
        elif i == message[j]:
            dialog_to_copy +=  "/message " + " \\"+ '"' +"{{i18n:"+ dialog_id + "." + str(i) +"}}\\"+ '"'+ " /pause " + str(pause_amount) + " "
            j += 1
        else:
            dialog_to_copy += "/speak " + npc_name + " \\"+ '"' +"{{i18n:"+ dialog_id + "." + str(i) +"}}\\"+ '"'+ " /pause " + str(pause_amount) + " "

    if not end:
        dialog_to_copy += "/switchEvent " + fork_two
    else:
        dialog_to_copy += " /end"

    print(dialog_to_copy)

# this is for alternating npc dialog strictly this is how it is encoded
def two_npc_dialog(dialog_id, num_of_dialog, pause_amount, first_npc_name, second_npc_name,switch_event = "",end = False):
    dialog_to_copy = ""
    for i in range(num_of_dialog):
        dialog_to_copy += "/speak " + first_npc_name + " \\" + '"' + "{{i18n:" + dialog_id + "." + str(i) + "}}\\" + '"' + " /pause " + str(pause_amount) + " " + "/speak " + second_npc_name + " \\" + '"' + "{{i18n:" + dialog_id + "." + str(i) + "}}\\" + '"' + " /pause " + str(pause_amount) + " "
    if not end:
        if switch_event != "":
            dialog_to_copy += "/switchEvent " + switch_event
        else:
            return print(dialog_to_copy)
    else:
        dialog_to_copy += " /end"
        return print(dialog_to_copy)

# This is for formatting dialog easier eg naming and numbering
# dialog should be an array of all written out dialog separated by a comma
def npc_dialog_formatter(dialog, dialog_id):
    for i in range(len(dialog)):
        if i != len(dialog):
            print('"' + str(dialog_id) + "." + str(i) + ": " + '"' + dialog[i] + '"'+",")
        else:
            print('"'+str(dialog_id)+"."+str(i)+": "+'"'+dialog[i]+'"')






