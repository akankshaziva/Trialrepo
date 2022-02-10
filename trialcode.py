def getBuildUser() :
    return currentBuild.rawBuild.getCause(Cause.UserIdCause).getUserId()
    

getBuildUser()
