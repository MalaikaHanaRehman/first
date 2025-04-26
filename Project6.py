import time

def countdown_timer(seconds):
    print("Countdown Timer Started!")
    
    while seconds > 0:
        # Display the remaining time
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # Overwrite the previous line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    
    print("Time's up!")

# Get the countdown duration from the user
try:
    duration = int(input("Enter the countdown duration in seconds: "))
    countdown_timer(duration)
except ValueError:
    print("Please enter a valid number of seconds.")