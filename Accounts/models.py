from django.db import models

class Student(models.Model):
    first_name = models.CharField(db_column='First_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    registration_number = models.IntegerField(db_column='Registration_number', primary_key=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=20, blank=True, null=True)  # Field name made lowercase.
    semester_number = models.IntegerField(db_column='Semester_Number', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contact_number = models.IntegerField(db_column='Contact_Number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'
        app_label='Accounts'
