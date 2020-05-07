from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from users.models import Profile
# Create your models here.

class Post(models.Model):
   
    JOB_CATEGORY =(
    (".NET Development", ".NET Development"),
    ("3D Printing", "3D Printing"),
    ("Accounts", "Accounts"),
    ("Acting", "Acting"),
    ("Agriculture & Food Engineering", "Agriculture & Food Engineering"),
    ("Analytics", "Analytics"),
    ("Android App Development", "Android App Development"),
    ("Angular.js Development", "Angular.js Development"),
    ("Animation", "Animation"),
    ("Architecture", "Architecture"),
    ("Artificial Intelligence (AI)", "Artificial Intelligence (AI)"),
    ("ASP.NET Development", "ASP.NET Development"),
    ("Automobile Engineering", "Automobile Engineering"),
    ("Backend Development", "Backend Development"),
    ("Big Data", "Big Data"),
    ("Bioinformatics", "Bioinformatics"),
    ("Biology", "Biology"),
    ("Biotechnology Engineering", "Biotechnology Engineering"),
    ("Blogging", "Blogging"),
    ("Brand Management", "Brand Management"),
    ("CAD Design", "CAD Design"),
    ("Campus Ambassador", "Campus Ambassador"),
    ("Chartered Accountancy (CA)", "Chartered Accountancy (CA)"),
    ("Chemical Engineering", "Chemical Engineering"),
    ("Chemistry", "Chemistry"),
    ("Cinematography", "Cinematography"),
    ("Civil Engineering", "Civil Engineering"),
    ("Client Servicing", "Client Servicing"),
    ("Cloud Computing", "Cloud Computing"),
    ("Commerce", "Commerce"),
    ("Company Secretary (CS)", "Company Secretary (CS)"),
    ("Computer Science", "Computer Science"),
    ("Computer Vision", "Computer Vision"),
    ("Content Writing", "Content Writing"),
    ("Copywriting", "Copywriting"),
    ("Creative Writing", "Creative Writing"),
    ("Customer Service", "Customer Service"),
    ("Cyber Security", "Cyber Security"),
    ("Data Entry", "Data Entry"),
    ("Data Science", "Data Science"),
    ("Database Building", "Database Building"),
    ("Design", "Design"),
    ("Digital Marketing", "Digital Marketing"),
    ("Editorial", "Editorial"),
    ("Electrical Engineering", "Electrical Engineering"),
    ("Electronics Engineering", "Electronics Engineering"),
    ("Embedded Systems", "Embedded Systems"),
   ("Energy Science & Engineering", "Energy Science & Engineering"),
   ("Engineering", "Engineering"),
   ("Engineering Design", "Engineering Design"),
   ("Environmental Sciences", "Environmental Sciences"),
   ("Event Management", "Event Management"),
   ("Facebook Marketing", "Facebook Marketing"),
   ("Fashion Design", "Fashion Design"),
   ("Film Making", "Film Making"),
   ("Finance", "Finance"),
   ("Front End Development", "Front End Development"),
   ("Full Stack Development", "Full Stack Development"),
   ("Fundraising", "Fundraising"),
   ("Game Development", "Game Development"),
   ("General Management", "General Management"),
   ("Government", "Government"),
   ("Graphic Design", "Graphic Design"),
   ("Hospitality", "Hospitality"),
   ("Hotel Management", "Hotel Management"),
   ("Human Resources (HR)", "Human Resources (HR)"),
   ("Humanities", "Humanities"),
   ("Image Processing", "Image Processing"),
   ("Industrial & Production Engineering", "Industrial & Production Engineering"),
   ("Industrial Design", "Industrial Design"),
   ("Information Technology", "Information Technology"),
   ("Instrumentation & Control Engineering", "Instrumentation & Control Engineering"),
   ("Interior Design", "Interior Design"),
   ("Internet of Things (IoT)", "Internet of Things (IoT)"),
   ("iOS App Development", "iOS App Development"),
   ("Java Development", "Java Development"),
   ("Javascript Development", "Javascript Development"),
   ("Journalism", "Journalism"),
   ("Law", "Law"),
   ("Legal Research", "Legal Research"),
   ("Machine Learning", "Machine Learning"),
   ("Magento Development", "Magento Development"),
   ("Manufacturing Engineering", "Manufacturing Engineering"),
   ("Market/Business Research", "Market/Business Research"),
   ("Marketing", "Marketing"),
   ("Mathematics", "Mathematics"),
   ("Mathematics & Computing", "Mathematics & Computing"),
   ("MBA", "MBA"),
   ("Mechanical Engineering", "Mechanical Engineering"),
   ("Mechatronics", "Mechatronics"),
   ("Media", "Media"),
   ("Medicine", "Medicine"),
   ("Merchandise Design", "Merchandise Design"),
   ("Metallurgical Engineering", "Metallurgical Engineering"),
   ("Mobile App Development", "Mobile App Development"),
   ("Motion Graphics", "Motion Graphics"),
   ("Naval Architecture and Ocean Engineeering", "Naval Architecture and Ocean Engineeering"),
   ("Network Engineering", "Network Engineering"),
   ("NGO", "NGO"),
   ("Node.js Development", "Node.js Development"),
   ("Operations", "Operations"),
   ("Pharmaceutical", "Pharmaceutical"),
   ("Photography", "Photography"),
   ("PHP Development", "PHP Development"),
   ("Physics", "Physics"),
   ("Political/Economics/Policy Research", "Political/Economics/Policy Research"),
   ("Public Relations (PR)", "Public Relations (PR)"),
   ("Product Management", "Product Management"),
   ("Programming", "Programming"),
   ("Psychology", "Psychology"),
   ("Python/Django Development", "Python/Django Development"),
   ("Recruitment", "Recruitment"),
   ("Ruby on Rails", "Ruby on Rails"),
   ("Sales", "Sales"),
   ("Science", "Science"),
   ("Search Engine Optimization (SEO)", "Search Engine Optimization (SEO)"),
   ("Social Media Marketing", "Social Media Marketing"),
   ("Social Work", "Social Work"),
   ("Software Development", "Software Development"),
   ("Software Testing", "Software Testing"),
   ("Statistics", "Statistics"),
   ("Strategy", "Strategy"),
   ("Supply Chain Management (SCM)", "Supply Chain Management (SCM)"),
   ("Teaching", "Teaching"),
   ("Telecalling", "Telecalling"),
   ("Travel & Tourism", "Travel & Tourism"),
   ("UI/UX Design", "UI/UX Design"),
   ("Video Making/Editing", "Video Making/Editing"),
   ("Videography", "Videography"),
   ("Volunteering", "Volunteering"),
   ("Web Development", "Web Development"),
   ("Wordpress Development", "Wordpress Development"),
    
  )

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
    available = models.CharField(max_length=2,choices= AVAILABLE )
    category= models.CharField(max_length=100, choices= JOB_CATEGORY)
    daerah= models.CharField(max_length=100, choices= DAERAH)
    duration= models.CharField(max_length=100, choices= DURATION)
    contact= models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    


