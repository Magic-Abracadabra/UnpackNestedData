def light(key, d) -> (bool, list):
	'''Returning (l, values). If the *key* is in the nested data d, then l=True. The list *values* will be composed of all iterable objects containing the key in d.'''
	l = False
	values = []
	try:
		iter(d)
		if key in d:
			l = True
			values.append(d)
		if type(d) == dict:
			d = d.items()
		for x in d:
			try:
				iter(x)
				if key in x:
					l = True
					values.append(x)
				else:
					l_, value = light(key, x)
					l = any([l, l_])
					if l_:
						values += value
			except:
				pass
		return l, values
	except:
		return l, values
