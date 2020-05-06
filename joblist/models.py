from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from users.models import Profile
# Create your models here.

class Post(models.Model):
   
    JOB_CATEGORY = (('Android App Development','Android App Development'), ('  Angular.js Development','  Angular.js Development'),('Software Developer','Software Developer'),('Consultant','Consultant'),('Accountant','Accountant'),('Mechanical Engineer','Mechanical Engineer'),('Electrician','Electrician'),('Graphic Designer','Graphic Designer'),('Writer and Editor','Writer and Editor'),('Market Research Analyst','Market Research Analyst'),('Interpreter and Translator','Interpreter and Translator'),('Architect','Architect'),('Chemist','Chemist'),('Database Administrator','Database Administrator'),('Customer Service Representative','Customer Service Representative'),('Fashion Designer','Fashion Designer'))

    DAERAH= (('Works from Home','Works from Home'),('Tawau','Tawau'),('Sandakan','Sandakan'),('Lahad Datu','Lahad Datu'),('Kota Kinabalu','Kota Kinabalu'),('Semporna','Semporna'))
    DURATION =(('1 Months','1 Months'),('2 Months','2 Months'),('3 Months','3 Months'),('4 Months','4 Months'),('5 Months','5 Months'),('6 Months','6 Months'))
    AVAILABLE =(('1','1'),('2','2'),('3','3'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'))

    content = models.TextField("About the work")
    responsibility = models.TextField("Selected intern's day-to-day responsibilities include")
    skills= models.CharField(max_length=100)
    perks = models.CharField(max_length=100)
    who_apply= models.TextField("Who can apply")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete =models.CASCADE)
    available = models.CharField(max_length=2,choices= AVAILABLE)
    category= models.CharField(max_length=100, choices= JOB_CATEGORY)
    daerah= models.CharField(max_length=100, choices= DAERAH)
    duration= models.CharField(max_length=100, choices= DURATION)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    


