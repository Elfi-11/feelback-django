from django.db import models

class User(models.Model):  # Modèle User pour la table 'users'
    id_users = models.AutoField(primary_key=True)  # Clé primaire
    email_users = models.EmailField(unique=True)  # Un champ email unique pour l'utilisateur
    password_users = models.CharField(max_length=255)  # Champ pour le mot de passe
    create_at_users = models.DateTimeField(auto_now_add=True)  # Date de création
    update_at_users = models.DateTimeField(auto_now=True)  # Date de mise à jour
    delete_at_users = models.DateTimeField(null=True, default=None)  # Date de suppression

    class Meta:
        db_table = 'users'  # Nom de la table existante

    def __str__(self):
        return self.email_users


class Form(models.Model):  # Modèle Form pour la table 'forms'
    id_forms = models.AutoField(primary_key=True)  # Clé primaire
    name_forms = models.CharField(max_length=45)  # Nom du formulaire
    created_at_forms = models.DateTimeField(auto_now_add=True)  # Date de création
    update_at_forms = models.DateTimeField(auto_now=True)  # Date de mise à jour
    delete_at_forms = models.DateTimeField(null=True, default=None)  # Date de suppression
    users_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='users_id')  # Référence à l'utilisateur

    class Meta:
        db_table = 'forms'  # Nom de la table existante

    def __str__(self):
        return self.name_forms


class Question(models.Model):  # Modèle Question pour la table 'questions'
    id_questions = models.AutoField(primary_key=True)  # Clé primaire
    title_questions = models.CharField(max_length=150)  # Titre de la question
    created_at_forms = models.DateTimeField(auto_now_add=True)  # Date de création
    update_at_forms = models.DateTimeField(auto_now=True)  # Date de mise à jour
    delete_at_questions = models.DateTimeField(null=True, default=None)  # Date de suppression
    forms_id = models.ForeignKey(Form, on_delete=models.CASCADE, db_column='forms_id')  # Référence au formulaire

    class Meta:
        db_table = 'questions'  # Nom de la table existante

    def __str__(self):
        return self.title_questions


class Answer(models.Model):  # Modèle Answer pour la table 'answers'
    id_answers = models.AutoField(primary_key=True)  # Clé primaire
    value_answers = models.PositiveSmallIntegerField()  # Valeur de la réponse (1-5)
    created_at_answers = models.DateTimeField(auto_now_add=True)  # Date de création
    update_at_answers = models.DateTimeField(auto_now=True)  # Date de mise à jour
    delete_at_answers = models.DateTimeField(null=True, default=None)  # Date de suppression
    questions_id = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='questions_id')  # Référence à la question
    users_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='users_id')  # Référence à l'utilisateur

    class Meta:
        db_table = 'answers'  # Nom de la table existante

    def __str__(self):
        return f"Answer {self.id_answers} - Value: {self.value_answers}"
