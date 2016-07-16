from django.shortcuts import render
from django.shortcuts import render_to_response
from polls.models import Choice, Poll
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

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
	return render(request, template, context)



def vote(request, poll_id):
    p = get_obj_or_404(Poll, pk=poll_id)
    try:
        chosed_choice = p.choices.get(pk=request.POST['choices'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        chosed_choice.votes += 1
        chosed_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, poll_id, template='results.html'):
	poll = get_obj_or_404(Poll, pk=poll_id)
	context = {
	'poll' : poll
	}
	return render(request, template, context)

#own get_object_or_404 wrapper
def get_obj_or_404(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        raise Http404