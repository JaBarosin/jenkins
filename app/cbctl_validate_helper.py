# Takes in the outfile from cbctl validate and writes a brief outfile summary of 
#  CBC Policy: <what cbctl policy was applied that triggered the violations>
#  Rules Violated: <what CBC-cbctl policy rule was violated
#
# If no violations, writes confiromation message to same file.
# 
# jbarosin - 5/27/2021

import json
import sys

with open(sys.argv[1]) as f:
    try:
        data = json.load(f)
    except Exception as e:
        print("No violations reported!")
        exit()

    if len(data['policy_violations']) > 0:
        print("*Cbctl validate results*\n")

        for rule in range(len(data['policy_violations'])):
            for policy in range(len(data['policy_violations'])):
                print("CBC Policy: " + str(data['policy_violations'][rule]['policy']) +
                      "\nRules violated: " + str(data['policy_violations'][rule]['rule']))


    else:
        print("Review ${env.BUILD_JOB} for full details on cbctl results")
