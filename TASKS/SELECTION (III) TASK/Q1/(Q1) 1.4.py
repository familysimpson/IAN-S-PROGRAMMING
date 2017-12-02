#DECLARE Temperature: INTEGER

#IF Temperature > 25
    #THEN
        #OUTPUT "Hot"
#END IF
#IF Temperature >= 20 and = 25
    #THEN
        #OUTPUT "Just Right"
    #ELSE
        #OUTPUT "Cold"