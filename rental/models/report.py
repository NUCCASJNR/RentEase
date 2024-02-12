#!/usr/bin/env python3

"""Contains the report model for the rental app"""

from rental.models.agent import Agent, BaseModel, models
from rental.models.apartment import Apartment


class VisitReport(BaseModel):
    """
    The visit report model
    """
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='visit_reports')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='visit_reports')
    report = models.TextField(null=False, blank=False)
    visit_date = models.DateTimeField(null=False, blank=False)
    recommendation = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'visit_reports'
