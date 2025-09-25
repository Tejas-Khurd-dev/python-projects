logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def get_emoji(account):
    """Return an emoji based on account type/description."""
    description = account['description'].lower()
    if "actor" in description or "actress" in description:
        return "🎬"
    elif "musician" in description or "singer" in description:
        return "🎵"
    elif "tv" in description or "television" in description:
        return "📺"
    elif "football" in description or "soccer" in description or "athlete" in description:
        return "⚽"
    elif "basketball" in description:
        return "🏀"
    else:
        return "🌟"
