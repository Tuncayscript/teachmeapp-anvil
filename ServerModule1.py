import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_contact_info(name, email, topic, question):
  app_tables.contact.add_row(
    name = name,
    email = email,
    topic = topic,
    question = question,
    time = datetime.now()
  )
  anvil.email.send(from_name="Contact Form",
                   subject = "TEACHME Contact",
                   text = f'This email from {name}\nTopic: {topic}\nComment: {question}',
                   
                  )
