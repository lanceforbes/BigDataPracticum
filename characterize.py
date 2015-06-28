import json
import operator

# load training data
print 'start loading file'
f = open('./train.json','r')
reviews = json.load(f)
print '    done loading file'

# count ratings
rating_counts = {}
for review in reviews:
    if review['rating'] in rating_counts:
        rating_counts[review['rating']] += 1
    else:
        rating_counts[review['rating']] = 1

print 'rating counts'
for key in rating_counts:
    print key, rating_counts[key]

# count categories 
category_counts = {}
for review in reviews:
    if review['category'] in category_counts:
        category_counts[review['category']] += 1
    else:
        category_counts[review['category']] = 1

print 'category counts:'
for key in category_counts:
    print key, category_counts[key]

print 'sort category counts by count'
s_category_counts = sorted(category_counts.items(), key=operator.itemgetter(1), reverse=True) 
for s_category_count in s_category_counts:
    print s_category_count 
