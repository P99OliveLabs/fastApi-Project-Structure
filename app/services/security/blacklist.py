# Function to check if a user is blacklisted (hardcoded for now)
async def is_user_blacklisted(user_id: int) -> bool:
    # Hardcoding the blacklist check: user with id=3 is blacklisted
    if user_id == 3:
        return True
    return False