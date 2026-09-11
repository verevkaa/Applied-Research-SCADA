def onShutdown(session):
	myDescription = "Perspective Session Logout"
	myActor = _soe.getUser(session)
	_soe.log(description=myDescription, actor=myActor, category="info")