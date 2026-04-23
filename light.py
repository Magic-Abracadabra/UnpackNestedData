def light(key, d):
	if key in d:
		return True, [d]
	else:
		l = False
		values = []
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
