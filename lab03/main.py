
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я','А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def gamma(start, key):
  key*=len(start)

  end_text=""
  for i, j in enumerate(start):
    position = alphabet.index(j)
    
    position_key=alphabet.index(key[i])+1
    new_position =(position+position_key)%33
    end_text+=alphabet[new_position]
    print(new_position,end=" ")
  print(f"\n Our Result: {end_text}")

gamma("ПРИКАЗ".upper(),"ГАММА")

#П 17   Г 4  21
#Р 18   А 1  19 
#И 10   М 14  24
#К 12   М 14  26
#А 1    А  1 2 
#З 9    Г 4 13

  