from djongo import models

class Person(models.Model):
    _id = models.ObjectIdField()  # Explicitly use ObjectId
    name = models.CharField(max_length=100)
    email = models.EmailField()
    aadhar_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    qualifications = models.CharField(max_length=100)
    job_details = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'persons'
