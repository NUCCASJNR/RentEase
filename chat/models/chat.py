#!/usr`/bin/env python3

from rental.models.user import BaseModel, MainUser, models


class Message(BaseModel):
    sender = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-created_at"]
    
    def all_messages(self):
        return self.objects.all()
