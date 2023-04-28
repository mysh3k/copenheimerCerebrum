import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.shortcuts import render
from .models import *
from .date_calls import *
from django.core import serializers


# Create your views here.
class AssignTask(View):
    def get(self, request, recipient):
        task = Task.objects.filter(finished=False, assign_date__lte=today_delta(48)).count()
        if task > 0:
            response = Task.objects.filter(finished=False, assign_date__lte=today_delta(48)).first()
            response.assign_date = today_date()
            response.recipient = recipient
            response.save()
            serialized_response = serializers.serialize('json', [response])
            return JsonResponse(serialized_response, safe=False)
        else:
            task = Task.objects.last()
            a, b, c = task.sequence1, task.sequence2, task.sequence3

            if c+1 <= 255:
                new_task = Task(sequence1=a, sequence2=b, sequence3=c+1, assign_date=today_date(), recipient=recipient)
                new_task.save()

            elif b+1 <= 255:
                c = 0
                if a == 172 and 16 <= b+1 <= 31:
                    b = 31
                new_task = Task(sequence1=a, sequence2=b+1, sequence3=c, assign_date=today_date(), recipient=recipient)
                new_task.save()

            elif a <= 255:
                c = 0
                b = 0
                if a+1 == 10:
                    a += 1
                new_task = Task(sequence1=a+1, sequence2=b, sequence3=c, assign_date=today_date(), recipient=recipient)
                new_task.save()

            else:
                a, b, c = 1, 0, 0
                new_task = Task(sequence1=a, sequence2=b, sequence3=c, assign_date=today_date(), recipient=recipient)
                new_task.save()
            serialized_response = serializers.serialize('json', [new_task])
            return JsonResponse(serialized_response, safe=False)


class TaskFinish(View):
    def post(self, request):
        data = json.loads(request.body)
        print(data)
        task = Task.objects.get(sequence1=data['fields']['sequence1'], sequence2=data['fields']['sequence2'], sequence3=data['fields']['sequence3'])
        task.finished = True
        task.save()
        return render(request, 'empty.html')


class Feedback(View):
    def post(self, request, ip, recipient):
        data = json.loads(request.body)
        players = []
        for player in data['players']['sample']:
            if len(player['name']) <= 16:
                players.append(player['name'])
            else:
                players = None
                break
        s = Server(ip_address=ip, version_name=data['version']['name'], players_online=data['players']['online'],
                   players_maximum=data['version']['max'], recipient=recipient, players=players, find_date=today_date())
        s.save()
        return render(request, 'empty.html')
