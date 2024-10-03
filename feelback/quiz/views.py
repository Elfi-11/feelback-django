from django.shortcuts import render, redirect
from django.db.models import Avg
from .models import Answer, Question, User  # Assurez-vous d'importer votre modèle personnalisé

def index(request):
    return render(request, 'quiz/index.html')

def feedbackForm(request):
    return render(request, "quiz/feedback-form.html")

def dashboard(request):
    # Compte des réponses uniques
    total_unique_responses = Answer.objects.values('id_answers').distinct().count()
    
    # Ajout des statistiques spécifiques
    avg_delivery_time = Answer.objects.filter(questions_id__title_questions='Évaluer de 1 à 5 le respect du délai de livraison').aggregate(Avg('value_answers'))['value_answers__avg']
    avg_package_condition = Answer.objects.filter(questions_id__title_questions='Évaluer de 1 à 5 l\'état de votre colis à sa réception').aggregate(Avg('value_answers'))['value_answers__avg']
    avg_courier_behavior = Answer.objects.filter(questions_id__title_questions='Évaluer de 1 à 5 le comportement du livreur').aggregate(Avg('value_answers'))['value_answers__avg']

    # Crée le contexte
    context = {
        'total_responses': total_unique_responses,
        'avg_delivery_time': avg_delivery_time,  # Ajout de la moyenne des délais de livraison
        'avg_package_condition': avg_package_condition,
        'avg_courier_behavior': avg_courier_behavior,
    }
    
    return render(request, 'quiz/dashboard.html', context)


def submit_feedback(request):
    if request.method == 'POST':
        # Récupérez les réponses du formulaire
        delivery_time = request.POST.get('delivery_time')
        package_condition = request.POST.get('package_condition')
        courier_behavior = request.POST.get('courier_behavior')

        print("Delivery Time from POST:", delivery_time)
        print("Package Condition from POST:", package_condition)
        print("Courier Behavior from POST:", courier_behavior)

        
        try:
            user = User.objects.get(id_users=1)  # Récupérez l'utilisateur avec id_users = 1
        except User.DoesNotExist:
            print("User with id_users=1 does not exist.")
            return render(request, 'quiz/feedback-form.html')  

        # Obtenez les questions correspondantes
        delivery_time_question = Question.objects.get(title_questions='Évaluer de 1 à 5 le respect du délai de livraison')
        package_condition_question = Question.objects.get(title_questions='Évaluer de 1 à 5 l\'état de votre colis à sa réception')
        courier_behavior_question = Question.objects.get(title_questions='Évaluer de 1 à 5 le comportement du livreur')

        # Enregistrez les réponses dans la base de données
        Answer.objects.create(value_answers=delivery_time, questions_id=delivery_time_question, users_id=user)
        Answer.objects.create(value_answers=package_condition, questions_id=package_condition_question, users_id=user)
        Answer.objects.create(value_answers=courier_behavior, questions_id=courier_behavior_question, users_id=user)

        # Redirigez vers une page de succès
        return redirect('success') 

    return render(request, 'quiz/feedback-form.html')

def success_view(request):
    return render(request, 'quiz/success.html')  


