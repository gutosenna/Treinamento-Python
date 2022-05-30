# FORMA 1
a = dict(marca='Fiat', modelo='Marea', ano=1999)
print(a)

# FORMA 2
b = {'marca': 'Fiat', 'modelo': 'Marea', 'ano': 1999}
print(b)

# FORMA 3
c = dict(zip(['marca', 'modelo', 'ano'], ['Fiat', 'Marea', 1999]))
print(c)

# FORMA 4
d = dict([('marca', 'Fiat'), ('modelo', 'Marea'), ('ano', 1999)])
print(d)

# FORMA 5
e = dict({'marca': 'Fiat', 'modelo': 'Marea', 'ano': 1999})
print(e)
