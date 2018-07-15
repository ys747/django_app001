from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import TemplateView
from django.shortcuts import redirect
#from .forms import HelloForm
from .forms import FriendForm
from .models import Friend
from .forms import FindForm
from django.db.models import Q

def index(request):
    data = Friend.objects.all()
    params = {
            'title': 'Hello',
            'data': data,
        }
    """
    if (request.method == 'POST'):
        num=request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    """
    return render(request, 'hello/index.html', params)

def create(request):
    if(request.method == 'POST'):
        obj = Friend()
        friend = Friend(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html' , params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)

def find(request):
    if(request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        #val = str.split()
        list = str.split()
        data = Friend.objects.filter(name__in=list)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request, 'hello/find.html', params)

"""
class HelloView(TemplateView):

    def __init__ (self):
       self.params = {
                'title': 'Hello',
                'form': HelloForm(),
                'result':None
            }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        ch = request.POST.getlist('choice')
        result = '<ol><b>selected:<b>'
        for item in ch:
            result += '<li>' + item + '</li>'
        result += '<ol>'
        self.params['result'] = result
        self.params['form'] = HelloForm(request.POST)

        msg = 'あなたは，<b>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
            ')</b>さんです。<br>メールアドレスは<b>' +request.POST['mail'] + \
            '</b>ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)

        return render(request, 'hello/index.html', self.params)


def form (request):
    msg = request.POST['msg']
    params = {
            'title':'Hello/Form',
            'msg':'こんにちは、' + msg + 'さん！',
        }
    return render(request, 'hello/index.html', params)

"""
