
from django.shortcuts import render
from django.http import HttpResponse
import re

word_counts = {}

def load_file_view(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        content = file.read().decode('utf-8')
        words = re.findall(r'\b[а-яА-ЯёЁ]+\b', content)
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return HttpResponse("Файл успешно загружен.")
    return render(request, 'index.html')

def word_count_view(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        if word in word_counts:
            count = word_counts[word]
            return HttpResponse(f"Слово '{word}' встретилось {count} раз(а).")
        else:
            return HttpResponse(f"Слово '{word}' не найдено.")
    return render(request, 'index.html')

def clear_memory_view(request):
    if request.method == 'POST':
        word_counts.clear()
        return HttpResponse("Память успешно очищена.")
    return render(request, 'index.html')
