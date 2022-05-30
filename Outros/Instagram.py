from datetime import datetime
import instaloader

L = instaloader.Instaloader()
L.login('email', 'senha')

followers = instaloader.Profile.from_username(L.context, 'medeirosbarbaras').get_followers()
followees = instaloader.Profile.from_username(L.context, 'medeirosbarbaras').get_followees()

print('\n')
print('Seguidores: ', str(followers._data['count']))
print('Seguindo: ', str(followees._data['count']))
print('\n\n')
print('Lista e informações de seguidores:')
print('\n')
print(followers._data['edges'])
