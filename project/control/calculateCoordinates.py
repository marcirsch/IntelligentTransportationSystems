DISTANCE_BEETWEEN_WINDOWS = 6

def calculateWindowCoordinates(target, recognisedWindowId):
    # TODO 
    val = target - int(recognisedWindowId)
    verticalDistance = int(val / 10) * DISTANCE_BEETWEEN_WINDOWS # we know if it is a negative or positive number so we can decide the moving direction 
    numOfWindowsToMoveHorizontal = val % 10            
    horizontalDistance = DISTANCE_BEETWEEN_WINDOWS * numOfWindowsToMoveHorizontal
    return horizontalDistance, verticalDistance