from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class About(models.Model):
    # Basic Info
    name = models.CharField(max_length=100, default="Ali Hassan")
    role = models.CharField(max_length=100, default="Python Developer")
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True, null=True)
    
    # Images & Files
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    about_image = models.ImageField(upload_to="about/", blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    
    # Stats & Experience
    projects_completed = models.CharField(max_length=20, default="50+", blank=True, null=True)
    experience_title = models.CharField(max_length=100, default="Python Developer", blank=True, null=True)
    experience_years = models.CharField(max_length=50, default="1+ Years", blank=True, null=True)
    experience_description = models.TextField(blank=True, null=True)
    
    # Education
    education_degree = models.CharField(max_length=100, default="B.Sc. Computer Science", blank=True, null=True)
    education_university = models.CharField(max_length=100, default="Tech University", blank=True, null=True)
    education_year = models.CharField(max_length=50, default="2020-2024", blank=True, null=True)

    # Contact & Socials
    email = models.EmailField(default="your-email@example.com")
    phone = models.CharField(max_length=20, default="+1234567890")
    location = models.CharField(max_length=200, default="City, Country")
    linkedin_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me Settings"

    def save(self, *args, **kwargs):
        # This forces the singleton behavior correctly
        if not self.pk and About.objects.exists():
            return None 
        return super(About, self).save(*args, **kwargs)

    def __str__(self):
        # THIS FIXES YOUR ADMIN ISSUE: It will now say "Portfolio Settings"
        return "Portfolio Settings (Click to Edit)"



class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FRONTEND', 'Frontend Development'),
        ('BACKEND', 'Backend & Tools'),
    ]
    name = models.CharField(max_length=100)
    level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Enter a value between 1 and 100"
    )
    # Changed default to FRONTEND to match home.html expectations
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='FRONTEND')

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    date = models.DateField(blank=True, null=True) # Added for the year display
    tech_stack = models.CharField(max_length=255, help_text="Enter skills separated by commas (e.g. Django, React, TailWind)", blank=True)
    link_live = models.URLField(blank=True, null=True, help_text="Live project URL")
    link_github = models.URLField(blank=True, null=True, help_text="GitHub repository URL")
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    @property
    def tech_stack_list(self):
        """Splits the tech_stack string into a list for the template loop"""
        if self.tech_stack:
            return [tech.strip() for tech in self.tech_stack.split(',')]
        return []

    def __str__(self):
        return self.title
