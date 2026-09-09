def log(description, pointName=None, pointValue=None, actor=None, category=None):
	system.db.runPrepUpdate(
						"INSERT INTO soe_AR (event_category, point_name, point_value, description, actor) VALUES (?, ?, ?, ?, ?)",
						[category, pointName, pointValue, description, actor]
					)
					
def alarmClass(alarmName):
	"""
	Maps an alarm name to the SOE description prefix.
	Returns None for alarms that should not be logged.
	"""
	if alarmName in ("Alarm High", "Alarm Low"):
		return "Threshold"
	elif alarmName == "Alarm":
		return "BadQuality"
	else:
		return

def qualityText(qualifiedValue):
	"""
	Human-readable quality description for a QualifiedValue.
	Falls back to the quality code name when no diagnostic message exists.
	"""
	q = qualifiedValue.quality
	msg = None
	try:
		msg = q.getDiagnosticMessage()
	except:
		pass

	if msg is not None and not isinstance(msg, basestring):
		try:
			msg = msg.orElse(None)
		except:
			msg = None
	if msg is None or not str(msg).strip():
		msg = str(q)
	return str(msg)
	
def getUser(session):
	user = session.props.auth.user.userName
	return user