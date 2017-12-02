#IN PSEUDOCODE

#DECLARE Day: STRING
#DECLARE Socks: STRING
#DECLARE Sandals: STRING

#Input Day
#IF Day <- "Monday"
    #THEN
        #OUTPUT "Red Socks"
    #ELSE
        #IF Day <- "Tuesday"
            #THEN
                #OUTPUT "Blue Socks"
    #ELSE
        #IF Day <- "Wednesday"
            #THEN
                #OUTPUT "Yellow Socks"
    #ELSE
        #IF Day <> <- "Monday", "Tuesday", "Wednesday"
            #OUTPUT "Sandals"
#END IF