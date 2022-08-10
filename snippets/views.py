from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from snippets.forms import SnippetForm
from snippets.models import Snippet


def top(request):
    snippets = Snippet.objects.all()
    context = {'snippets': snippets}
    return render(request, 'snippets/top.html', context)


# def snippet_new(request):
#     return HttpResponse('スニペットの登録')
@login_required
def snippet_new(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.create_by = request.user
            snippet.save()
            return redirect(snippet_detail, snippet_id=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippets/snippet_new.html', {'form': form})


# def snippet_edit(request):
#     return HttpResponse('スニペットの編集')

@login_required
def snippet_edit(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.create_by_id != request.user.id:
        return HttpResponseForbidden('このスニッペトの編集は許可されていません。')

    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.valid():
            form.save()
            return redirect('snippet_detail', snippet_id=snippet_id)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/snippet_edit.html', {'form': form})


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})
