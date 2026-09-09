def onStartup(session):
	myDescription = "Perspective Session Login"
	myActor = soe.getUser(session)
	soe.log(description=myDescription, actor=myActor, category="info")