def piglatin(string):
  digraphs = ['bl','br','ch','cl','cr','dr','fl','fr','gl','gr','pl','pr','sc',
'sh','sk','sl','sm','sn','sp','st','sw','th','tr','tw','wh','qu','wr']
  trigraphs = ['sch', 'scr', 'str', 'sph', 'spl', 'squ', 'thr']
  vowels = ['a','e','i','o','u']
  s = []:
  split_string  = string.split()
  for word in split_string:
    if word[0] in vowels: 
     new = word + 'yay'
    elif word[:2] in digraphs:   
       new = word[2:] + word[:2] + 'ay'
    elif word[3:] in trigraphs:
       new = word[3:] + word[:3] + 'ay'
    else:
       new = word[1:] + word[:1] + 'ay'
    s.append(new)
  s = ' '.join(s)
  return s
