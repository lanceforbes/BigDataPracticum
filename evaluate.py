import json

# load the actual ratings 
actuals_fn = '../../answer_key/test_with_rating.json'
print 'Load actual ratings from file "%s"...' % (actuals_fn)
actuals_f = open(actuals_fn,'r')
actuals = json.load(actuals_f)
actuals_f.close()
answers = {}
for actual in actuals:
    answers[actual['review_id']] = actual['rating'] 
   
# open the predictions file
predict_fn = './predict_random.txt' # totaly random predictions
predict_fn = './predict_5.txt'      # always guess 5
predict_f = open(predict_fn,'r')

# compare actual to predicted
print 'Compare actual to predicted...'
correct_count = 0
wrong_count = 0
confusion_matrix = {1:{1:0,2:0,3:0,4:0,5:0},  # this matrix will hold the detailed evaluation results
                    2:{1:0,2:0,3:0,4:0,5:0},
                    3:{1:0,2:0,3:0,4:0,5:0},
                    4:{1:0,2:0,3:0,4:0,5:0},
                    5:{1:0,2:0,3:0,4:0,5:0}}

# read the input file and run the evaluation
print 'Loading predictions from file "%s"...' % (predict_fn)
for line in predict_f.readlines():
    id, predicted_rating = line.split()
    predicted_rating = int(predicted_rating)
    actual_rating = int(answers[float(id)])
    confusion_matrix[actual_rating][predicted_rating] += 1
    if predicted_rating == actual_rating:
        correct_count += 1
    else:
        wrong_count += 1

# print the results of the evaluation
percent_correct = 100. * float(correct_count) / float(correct_count + wrong_count)
print '%i correct, %i wrong (%5.2f%%)' % (correct_count, wrong_count, percent_correct)
for a in confusion_matrix:
    for p in confusion_matrix:
        print '%7i (%i,%i)' % (confusion_matrix[a][p], a, p),
    print

