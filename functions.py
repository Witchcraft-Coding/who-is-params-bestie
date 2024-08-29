def is_params_bestie(name: str, bestie: str, surname: str) -> str:
	name = name.strip()
	if ' ' in name:
		name_parts = name.split(' ')
		if len(name_parts) != 2:
			return "Aww, too bad for you! You aren't Param's bestie."
		else:
			if (
				name_parts[0].lower() == bestie.lower()
				and name_parts[1].lower() == surname.lower()
			):
				return "Yes, you are Param's bestie!"
			else:
				return "Aww, too bad for you! You aren't Param's bestie."
	else:
		if name.lower() == bestie.lower():
			return "Yes, you are Param's bestie!"
		else:
			return "Aww, too bad for you! You aren't Param's bestie."