def scores(score):
    if 80 <= score <= 100:
        print("Excellent")

    elif 60 <= score <= 79.9:
        print("Very Good")

    elif 40 <= score <= 59.9:
        print("Good")

    elif 0 <= score <= 39.9:
        print("Fair")

    else:
        print('Invalid Number')