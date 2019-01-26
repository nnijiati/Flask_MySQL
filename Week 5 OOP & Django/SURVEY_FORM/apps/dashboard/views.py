from django.shortcuts import render, redirect

# Create your views here.


def index(req):
    context = {
        'title': 'Home'
    }
    return render(req, 'dashboard/index.html', context)

def success(req):
    context = {
        'title': 'Success'
    }
    return render(req, "dashboard/success.html", context)

def user_ids(req, u_id):
    context = {
        'title': 'Colors', 
        'header': u_id
    }
    return render(req, "dashboard/colors.html", context)

def process(req):
    if req.method != "POST":
        return redirect('/')

    req.session['name'] = req.POST['name']
    req.session['location'] = req.POST['location']
    req.session['favorite_language'] = req.POST['favorite_language']
    return redirect('/success')