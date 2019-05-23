from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def result(request):
    text = request.GET['fulltext']
    textcount = len(text)
    words = text.split()
    words_set = set(words)
    total_word_count = len(words_set)
    word_count_dic = dict()

    for word in words_set:
        word_count_dic[word] = words.count(word)

    return render(request, 'result.html', {
        'total_text_count' : textcount,
        'total_word_count': total_word_count,
        'text': text,
        'word_count_dic': word_count_dic,
    })
