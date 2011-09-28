from random import randint

from django.shortcuts import render, get_object_or_404
from django.db import models
from models import Comic

def index(request):
	#latest comic 
	max_pk = Comic.objects.aggregate(max_pk=models.Max('pk'))['max_pk']
	curr_pk = max_pk
	next_pk = Comic.objects.filter(pk__gt=curr_pk).aggregate(next_pk=models.Min('pk'))['next_pk']
	pre_pk = Comic.objects.filter(pk__lt=curr_pk).aggregate(pre_pk=models.Max('pk'))['pre_pk']
	random_comic =  Comic.objects.order_by('?')[0]
	rand_pk = random_comic.pk
	comic = Comic.objects.get(pk=max_pk)

	if next_pk is None:
		#this handles the case where the user is at the last comic
		next_pk = curr_pk

	if pre_pk is None:
		#this handles the case where the user at the first comic
		pre_pk = 1

	return render(request, 'index.html', {'comic': comic, 'next_pk': next_pk, 'pre_pk': pre_pk, 'rand_pk': rand_pk})

def comic(request, id):
	comic = get_object_or_404(Comic, pk=id)
	curr_pk = id
	next_pk = Comic.objects.filter(pk__gt=curr_pk).aggregate(next_pk=models.Min('pk'))['next_pk']
	pre_pk = Comic.objects.filter(pk__lt=curr_pk).aggregate(pre_pk=models.Max('pk'))['pre_pk']
	max_pk = Comic.objects.aggregate(max_pk=models.Max('pk'))['max_pk']
	random_comic =  Comic.objects.order_by('?')[0]
	rand_pk = random_comic.pk

	if next_pk is None:
		#this handles the case where the user is at the last comic
		next_pk = curr_pk

	if pre_pk is None:
		#this handles the case where the user at the first comic
		pre_pk = 1
		
	# print 'next_pk value: ' , next_pk
	# print 'pre_pk value: ' ,  pre_pk
	# print 'rand_pk value: ' , rand_pk

	return render(request, 'comic.html', {'comic': comic, 'next_pk': next_pk, 'pre_pk': pre_pk, 'rand_pk': rand_pk})
