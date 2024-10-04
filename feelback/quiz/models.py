from django.db import models
#Créer une class par table à autiliser pour dire à django com#ment est fait notre bdd
#Normalement, utiliser ce modèle de classe pour créer les tables et accéder au colone
#ATTENTION PAS DE makemigration ICI, autrement bddd = cassé, car django aura créer des nouvelles tables

class User(models.Model):  
    id_users = models.AutoField(primary_key=True)  
    email_users = models.EmailField(unique=True)  
    password_users = models.CharField(max_length=255)  
    create_at_users = models.DateTimeField(auto_now_add=True)  
    update_at_users = models.DateTimeField(auto_now=True)  
    delete_at_users = models.DateTimeField(null=True, default=None)  

    class Meta:
        db_table = 'users' 

    def __str__(self):
        return self.email_users


class Form(models.Model):  
    id_forms = models.AutoField(primary_key=True) 
    name_forms = models.CharField(max_length=45)  
    created_at_forms = models.DateTimeField(auto_now_add=True)  
    update_at_forms = models.DateTimeField(auto_now=True)
    delete_at_forms = models.DateTimeField(null=True, default=None)  
    users_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='users_id')  

    class Meta:
        db_table = 'forms'  

    def __str__(self):
        return self.name_forms


class Question(models.Model): 
    id_questions = models.AutoField(primary_key=True)  
    title_questions = models.CharField(max_length=150)  
    created_at_forms = models.DateTimeField(auto_now_add=True)  
    update_at_forms = models.DateTimeField(auto_now=True)  
    delete_at_questions = models.DateTimeField(null=True, default=None)  
    forms_id = models.ForeignKey(Form, on_delete=models.CASCADE, db_column='forms_id')  

    class Meta:
        db_table = 'questions'  

    def __str__(self):
        return self.title_questions


class Answer(models.Model):  
    id_answers = models.AutoField(primary_key=True)  
    value_answers = models.PositiveSmallIntegerField()  
    created_at_answers = models.DateTimeField(auto_now_add=True)  
    update_at_answers = models.DateTimeField(auto_now=True)  
    delete_at_answers = models.DateTimeField(null=True, default=None)  
    questions_id = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='questions_id')  
    users_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='users_id')  

    class Meta:
        db_table = 'answers'  

    def __str__(self):
        return f"Answer {self.id_answers} - Value: {self.value_answers}"
