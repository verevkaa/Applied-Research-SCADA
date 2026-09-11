def onStartup(session):
	myDescription = "Perspective Session Login"
	myActor = _soe.getUser(session)
	_soe.log(description=myDescription, actor=myActor, category="info")