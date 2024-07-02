from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import TodoItem
import json

@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todos = TodoItem.objects.all()
        data = {'todos': list(todos.values())}
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        todo = TodoItem.objects.create(
            title=data['title'],
            body=data['body']
        )
        return JsonResponse({'message': 'Todo created successfully!'})

    return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def todo_detail(request, pk):
    try:
        todo = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return JsonResponse({'error': 'Todo does not exist'}, status=404)

    if request.method == 'GET':
        data = {
            'title': todo.title,
            'body': todo.body
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        todo.title = data.get('title', todo.title)
        todo.body = data.get('body', todo.body)
        todo.save()
        return JsonResponse({'message': 'Todo updated successfully!'})

    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': 'Todo deleted successfully!'})

    return JsonResponse({'error': 'Invalid request method'})
