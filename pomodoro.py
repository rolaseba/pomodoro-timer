"""
This is a Pomodoro timer application that helps manage work and break intervals 
based on the Pomodoro Technique. The application reads configuration settings 
from a JSON file, displays ASCII art, and plays audio notifications for work 
and break periods.

Features:
- Configurable work and break durations.
- Audio notifications (optional) for different phases.
- Visual display of the number of Pomodoros completed and progress bar.
"""

import time
import os
import json
from tqdm import tqdm
from art import *
import pygame

pomodoro_art = '''
   ,--./,-.
 / #      \\ 
|          |  
 \\        /   
  `._,._,'
'''


def load_config(config_file):
    """
    Load configuration from a JSON file.

    Parameters:
    config_file (str): Path to the configuration JSON file.

    Returns:
    dict: Configuration settings.
    """
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config


def run_timer(minutes, message):
    """
    Run a timer for a specified number of minutes with a progress bar.

    Parameters:
    minutes (int): Duration of the timer in minutes.
    message (str): Message to display during the timer.
    """
    print(f"For {minutes} minutes.")
    total_seconds = minutes * 60
    for second in tqdm(range(total_seconds), desc=f"{message}", unit='sec'):
        time.sleep(1)  # Sleep for 1 second

def clean_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')  
    
         
def print_pomodoro_info(pomodoros, pomodoro_basket, pomodoros_before_long_break, pomodoro_art):
    """
    Print Pomodoro information with ASCII art.

    Parameters:
    pomodoros (int): Number of completed Pomodoros in the current cycle.
    pomodoro_basket (int): Number of Pomodoro baskets (completed cycles of Pomodoros).
    pomodoros_before_long_break (int): Number of Pomodoros before a long break.
    pomodoro_art (str): ASCII art representing a Pomodoro.
    """
    clean_screen()
    num_art = text2art(f"{pomodoros}   /   {pomodoros_before_long_break}        -        {pomodoro_basket}   Baskets")
    print(pomodoro_art, num_art) 

def play_audio_notification(audio_file):
    """
    Play an audio notification.

    Parameters:
    audio_file (str): Path to the audio file to play.
    """
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    
def main():
    """
    Main function to run the Pomodoro timer application.
    """
    config = load_config('config.json')
    
    work_duration = config['work_duration']
    short_break_duration = config['short_break_duration']
    long_break_duration = config['long_break_duration']
    pomodoros_before_long_break = config['pomodoros_before_long_break']
    text_for_long_break = config["text_for_long_break"]
    audio_notification = config['audio_notification']
    audio_file_start_work = config['audio_file_work']
    audio_file_start_break = config['audio_file_break']
    audio_file_start_long_break = config['audio_file_long_break']
    
    pygame.mixer.init()
    
    pomodoros = 0
    pomodoro_basket = 0

    while True:
        pomodoros += 1
        print_pomodoro_info(pomodoros, pomodoro_basket, pomodoros_before_long_break, pomodoro_art)
        
        if audio_notification:
            play_audio_notification(audio_file_start_work)
            
        run_timer(work_duration, "Working")
        
        if pomodoros % pomodoros_before_long_break == 0:
            if audio_notification:
                play_audio_notification(audio_file_start_long_break)
            clean_screen()
            print(text2art(text_for_long_break,font="colossal")) # fonts on https://www.ascii-art.site/FontList.html
            run_timer(long_break_duration, "Long break")
            
            pomodoro_basket += 1
            pomodoros = 0  # Reset pomodoros count after a long break
        else:
            print("\n")
            if audio_notification:
                play_audio_notification(audio_file_start_break)
            run_timer(short_break_duration, "Short break")
            

if __name__ == "__main__":
    main()
