meme_dict= {"cringe":"garip ve utanç verici şeyler için kullanılır","lol":"komik şeyler için kullanılır",
"rofl":"şakaya şakayla karşılık vermek","creepy":"korkunç,ürkütücü anlamına gelir","creepypasta":"korkutucu şehir efsaneleri",
"sheesh":"onaylamamak","aggro":"sinirlenmek"}
word = input('bir kelime giriniz:')
if word in meme_dict.keys():
    print(meme_dict[word])
    
else:
    print("kelime bulunamadı")
