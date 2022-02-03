import re
import datetime

def user_data_control(data: dict):
   try:
      for i in data.keys():
         data[i] = str(data[i]).strip()
   except Exception as e:
      return str(e), False
   if len(data['user_name']) < 5 or len(data['user_name']) > 80:
         return "The username complies with the rules. Please use a minimum of 5 and a maximum of 79 simvols.", False
   if len(data['user_email']) < 5 or len(data['user_email']) > 120 or not is_email(data['user_email']):
      return "It looks like your email address is wrong. Please use a real email address.", False
   if len(data['user_password']) < 10 or len(data['user_password']) > 256 :
      return "Use at least 10 and at most 255 simvols in your password.", False
   return data, True

def event_data_control(data: dict, id_ccontrol=False):
   try:
      for i in data.keys():
         data[i] = str(data[i]).strip()
   except Exception as e:
      return str(e), False
   if len(data['e_text']) < 5 or len(data['e_text']) > 2047:
         return "The event text complies with the rules. Please use a minimum of 5 and a maximum of 2047 simvols.", False
   if id_ccontrol:
      try:
         data['e_id'] = int(data.get('e_id'))
      except Exception as e:
         return str(e), False
   try:
      data['e_date'] = datetime.datetime.strptime(data['e_date'], "%Y %m %d")
   except ValueError:
      return "Use only '%Y %m %d' format for e_date", False
   except Exception as e:
      return str(e), False
   return data, True

def is_email(email):
   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   if re.fullmatch(regex, email):
      return True
   return False