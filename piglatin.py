def piglatin(string):
  digraphs = ['bl','br','ch','cl','cr','dr','fl','fr','gl','gr','pl','pr','sc',
'sh','sk','sl','sm','sn','sp','st','sw','th','tr','tw','wh','qu','wr']
  trigraphs = ['sch', 'scr', 'str', 'sph', 'spl', 'squ', 'thr']
  vowels = ['a','e','i','o','u']
  s = []
  punctuation = ['?','!','.',',']
  punc = [len(word)-1:] #as punctuation is at the end of words, this notes the punctuation
  split_string  = string.split()
  for word in split_string:
    if word[0] in vowels: 
     new = word + 'yay'
    elif word[:2] in digraphs or word[:3] in trigraphs:   
       new = word[2:] + word[:2] + 'ay'
       new = word[3:] + word[:3] + 'ay'
    elif punc in punctuation:
       new = word.strip(punc) + word[1:] + word[:1] + punc
    else:
       new = word[1:] + word[:1] + 'ay'
    s.append(new)
  s = ' '.join(s)
  return s
