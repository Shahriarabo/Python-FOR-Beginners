import pprint as pp 
text = ' This is the zone is very Beautyful and so Cuteness .'

letter = {}

for i in  text:
    letter.setdefault(i,0)
    letter[i] = letter[i]+1
    
pp.pprint(letter)
    
