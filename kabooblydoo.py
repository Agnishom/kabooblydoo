import random

def kabooblydoo(s,n=2):
	chain = {}

	data = s.split('\n')
	data = ' '.join(data)
	words = data.split(' ')

	prefix = " "

	for i in xrange(len(words)):
		prefix = prefix.split(' ')
		prefix.append(words[i])
		while len(prefix) > n:
			prefix.pop(0)
		prefix = ' '.join(prefix)
		try:
			suffix = words[i+1]
		except:
			suffix = ""
		if prefix in chain:
			chain[prefix].append(suffix)
		else:
			chain[prefix] = [suffix]

	text = ""

	state = random.choice(chain.keys())
	for i in xrange(1000):
		text += " " + state.split(' ')[0]
		if state not in chain:
			break
		new = random.choice(chain[state])
		state = state.split(' ')
		state.append(new)
		while len(state) > n:
			state.pop(0)
		state = " ".join(state)

	return text