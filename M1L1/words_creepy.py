meme_dict = {'cringe': 'pena ajena',
'GG':'Good game',
'npc':'no playable character',
'BRB':'Be right back',
'IDK':'I don´t know',
'ZZZ':'Dormido',
'FPS':'Fotogramaa por segundo o First person shooter',
'XP':'Experience points',
'NOOB':'Novato',
'Hitbox':'Caja de daño'}

print (meme_dict.keys())
while True:
  palabra = input ('que palabra quieres saber')
  if palabra in meme_dict.keys():
    print(meme_dict[palabra])
  else:
    print('Esa palabra no la tenemos')