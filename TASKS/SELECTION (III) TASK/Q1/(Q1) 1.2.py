#DECLARE day: STRING
#DECLARE Socks: STRING
#DECLARE Sandals: STRING

#CASE OF DAY
    #"Monday" : OUTPUT "Red Socks"
    #"Tuesday" : OUTPUT "Blue Socks"
    #"Wednesday" : OUTPUT "Yellow Socks"
#OTHERWISE
    #OUTPUT "Sandals"
#ENDCASE