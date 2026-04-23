def light(key, d) -> (bool, list):
	'''Returning (l, values). If the *key* is in the nested data d, then l=True. The list *values* will be composed of all iterable objects containing the key in d.'''
	l = False
	values = []
	if hasattr(d, '__iter__') and not isinstance(d, str):
		if key in d:
			l = True
			values.append(d)
		if isinstance(d, dict):
			if key in d.values():
				l = True
				if d[-1] != d:
					values.append(d)
			for x in d.values():
				if hasattr(x, '__iter__') and not isinstance(x, str):
					L, value = light(key, x)
					l = any([l, L])
					values += value
		else:
			for x in d:
				if hasattr(x, '__iter__') and not isinstance(x, str):
					L, value = light(key, x)
					l = any([l, L])
					values += value
	return l, values
