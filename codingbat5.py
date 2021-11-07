def parrot_trouble(talking, hour):
   if(talking and (hour<=6 or hour>=21)):
     return True
   if(talking or (hour<=6 or hour>=21)):
     return False
   else:
      return False
