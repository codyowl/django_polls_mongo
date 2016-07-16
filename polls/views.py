from django.shortcuts import render
from django.shortcuts import render_to_response
from polls.models import Choice, Poll
# from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request, template='index.html'):
	poll = Poll.objects.all()
	context = {
	'poll' : poll
	}
	return render_to_response(template, context)

def detail(request, poll_id, template='detail.html'):
	poll = get_obj_or_404(Poll, pk=poll_id)
	context = {
	'poll' : poll
	}
	return render_to_response(template, context)

def get_obj_or_404(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        raise Http404


