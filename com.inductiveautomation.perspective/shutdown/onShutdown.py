def onShutdown(session):
	myDescription = "Perspective Session Logout"
	myActor = soe.getUser(session)
	soe.log(description=myDescription, actor=myActor, category="info")