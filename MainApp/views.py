from django.shortcuts import render, get_object_or_404, reverse, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models


q_id = 0


def index(request) -> HttpResponse:
    x_value = models.XValue.objects.all()[0]
    x_value.x_id = 0
    x_value.x_point = 0
    x_value.save()
    return render(request, 'MainApp/index.html')


def questions(request) -> HttpResponse:
    global q_id

    x_value = models.XValue.objects.all()[0]

    if q_id >= len(models.Questions.objects.all()) and x_value.x_point > 0:
        q_id = 0
        return redirect('/recording')

    if q_id >= len(models.Questions.objects.all()) and x_value.x_point == 0:
        q_id = 0
        x_value.x_id = 0
        x_value.x_point = 0
        x_value.save()
        return redirect('/gameover')

    question = models.Questions.objects.all()[q_id]

    try:
        selected_choices = request.POST['choice']

        if request.method == 'POST':
            if x_value.x_id == 3 and x_value.x_point == 0:
                q_id = 0
                return redirect('/gameover')
            elif x_value.x_id == 3 and x_value.x_point > 0:
                return redirect('/recording')
            else:
                if selected_choices == question.question_answer:
                    x_value.x_point += 10
                    x_value.save()
                else:
                    x_value.x_id += 1
                    x_value.save()
        else:
            if q_id > len(models.Questions.objects.all()):
                q_id = 0
            else:
                q_id += 1
                return render(request, 'MainApp/questions.html', {'x_img': x_value.x_id, 'question': question, 'point': x_value.x_point})
    except KeyError:
        return render(request, 'MainApp/questions.html', {'x_img': x_value.x_id, 'question': question, 'point': x_value.x_point})
    else:
        if q_id > len(models.Questions.objects.all()):
            q_id = 0
        else:
            q_id += 1
            return redirect(f'/questions')


def recording(request) -> HttpResponse:
    champions = models.ScoreBoard.objects.all()
    x_value = models.XValue.objects.all()[0]

    founded = 0

    if request.method == 'POST':
        try:
            champ_name = request.POST['chname']
        except:
            return render(request, 'MainApp/recording.html', {'point': x_value.x_point})
        else:
            for champ in champions:
                if champ_name == champ.name:
                    founded = 1
                    break
                else:
                    founded = 0

            if founded == 1: 
                return render(request, 'MainApp/recording.html', {'point': x_value.x_point, 'error_msg': 'This name exists!'})
            else:
                new_champion = models.ScoreBoard()
                new_champion.name = champ_name
                new_champion.point = x_value.x_point
                new_champion.save()

                x_value.x_id = 0
                x_value.x_point = 0
                x_value.save()
                
                return redirect(f'/leaderboard')
    else:
        return render(request, 'MainApp/recording.html', {'point': x_value.x_point})


def leader_board(request) -> HttpResponse:
    champions = models.ScoreBoard.objects.all()
    sorted_champions = sorted(champions, key=lambda champ: champ.point, reverse=True)
    
    return render(request, 'MainApp/leaderboard.html', {'champions': sorted_champions})


def game_over(request) -> HttpResponse:
    return render(request, 'MainApp/gameover.html')