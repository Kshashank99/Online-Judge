from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class User(models.Model):
# 	user_name = models.CharField(max_length=100)
# 	# user_rating = models.IntegerField(default=0)
# 	def __str__(self):
# 		return self.user_name

class Question(models.Model):
	question_name = models.CharField(max_length=100)
	question_description = models.CharField(max_length=10000)
	difficulty=models.CharField(max_length=100,null=True, blank=True)
	# question_input_file = models.CharField(max_length=200)
	# question_output_file = models.CharField(max_length=200)
	def __str__(self):
		return self.question_name

class solution(models.Model):
    curr_problem=models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    verdict=models.TextField(default='WA')
    time_of_submit = models.DateTimeField(auto_now=True)
    code=models.TextField(null=True, blank=True)		

class testcase(models.Model):
    curr_problem=models.ForeignKey(Question, on_delete=models.CASCADE)
    input=models.TextField(null=True, blank=True)
    output=models.TextField(null=True, blank=True)
# class Submission(models.Model):
# 	user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)
# 	submission_file = models.FileField(upload_to='documents/', default='background.gif')
# 	submission_status = models.CharField(max_length=50)
# 	submission_language = models.CharField(max_length=50)
# 	submission_time = models.FloatField(default=100.00)

# from django.db import models

# # Create your models here.
# class Users(models.Model):
#     user_name = models.CharField(max_length=200)
#     # pub_date = models.DateTimeField('date published')
#     def __str__(self):
#     		return self.user_name

# class Question(models.Model):
#     question_name = models.CharField(max_length=100)
# 	# description = models.CharField(max_length=1000)
# 	def __str__(self):
# 		return self.question_name

# class TestCases(models.Model):
#     input = models.CharField(max_length=200)
# 	output= models.CharField(max_length=200)

# class Submission(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)
# 	submission_file = models.FileField(upload_to='documents/', default='background.gif')
# 	submission_status = models.CharField(max_length=50)
# 	submission_language = models.CharField(max_length=50)
# 	submission_time = models.FloatField(default=100.00)