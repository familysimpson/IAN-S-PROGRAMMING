#DECLARE Temperature: INTEGER

#IF Temperature > 25
    #THEN
        #OUTPUT "Hot"
#ELSE IF Temperature >= 20 AND Temperature <= 25
    #THEN
        #OUTPUT "Just Right"
#ELSE
    #OUTPUT "Cold"