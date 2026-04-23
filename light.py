def light(key, d) -> (bool, list):
	'''Returning (l, values). If the *key* is in the nested data d, then l=True. The list *values* will be composed of all iterable objects containing the key in d.'''
	l = False
	values = []
	if key in d:
		l = True
		values.append(d)
	try:
		iter(d)
		if type(d) == dict:
			d = d.items()
		for x in d:
			if key in x:
				l = True
				values.append(x)
			else:
				l_, value = light(key, x)
				l = any([l, l_])
				if l_:
					values += value
		return l, values
	except:
		return l, values
