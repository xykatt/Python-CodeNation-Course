def qa( question, true_options, false_options) :
    answer = "  "

    while answer not in true_options.upper() and answer not in false_options.upper() :
        answer = input( question )
        answer = answer.upper()
    
    if answer in true_options.upper() :
        return True

    if answer in false_options.upper() :
        return False

def qa_until( question, valid_answers) :
    max_answers = len( valid_answers)
    answer_prompt = ""
    result = -1

    #build visual list of valid answers to display
    for ans in valid_answers :
        answer_prompt += (ans + " ")
    
    #loop until answer is valid
    while result < 0 :
        #get the user input after displaying the question, a newline and the valid answers
        ans = input( f"{question} \n ( {answer_prompt}) ?")

        #search valid answers for uppercase match to ans from input above and update result
        for x in range( 0, max_answers):
            if ans.upper() == valid_answers[x].upper() :
                result = x

    #return result from search(which may have remained -1 meaning no match found)
    return result

def type_print( message, speed=0.1, pause=0.5):
    from sys import stdout
    from time import sleep

    #loop display each character in the message string pausing for 100millsec each time
    for char in message:
        stdout.write(char)
        stdout.flush()
        sleep(speed)

    #after typing the message, pause before proceeding
    sleep(pause)
    stdout.write('\n')
    stdout.flush()
