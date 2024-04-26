meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "ROFL": "bir şakaya karşılık cevap"
            }
            
word = input("Anlamadığınız bir kelime yazın")
            
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime bende yok")
