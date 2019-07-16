from textblob import TextBlob
f1='I ate food here before, it was bad.'
f2='I ate food here before, it was awesome.'

b1=TextBlob(f1)
s1=b1.sentiment
print(s1)

#    print(s1)
#        |
#        |
#    ---------
#   /         \
#  /           \
#  Polarity   Subjectivity
