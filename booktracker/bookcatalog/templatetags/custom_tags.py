from django import template
from django.urls import reverse
import datetime 
from functools import reduce 

register = template.Library()

@register.simple_tag 
def calculate_average_rating(book):
  reviews = book.bookreview_set.all()
  all_star = 0
  for review in reviews:
    all_star += review.stars
  #combined_star_rating = reduce(lambda r1,r2: r1.stars+r2.stars,reviews)
  total_ratings = book.bookreview_set.count()
  if total_ratings == 0:
    return "No Ratings"
  else:
    return round(all_star/total_ratings,2)
    