import os
import time

from tqdm import tqdm

import colors

TOTAL_LENGTH = 16

def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_greeting():
    _clear_screen()
    print(colors.YELLOW + "+---------------------------------------------+" + colors.RESET)
    print(colors.YELLOW + "|                 Cześć Antek!                |" + colors.RESET)
    print(colors.YELLOW + "|        Witaj w świątecznym quizie...        |" + colors.RESET)
    print(colors.YELLOW + "+---------------------------------------------+" + colors.RESET)
    print("\n")


def present_rules():
    print("Zasady są bardzo proste:")
    print("1. Jeśli pytanie ma różne odpowiedzi do wyboru - podaj samą cyferkę przypisaną do odpowiedzi.")
    print("2. Jeśli nie ma odpowiedzi do wyboru - wpisz odpowiedź ręcznie.\n")
    print(colors.RED + "UWAGA!" + colors.RESET)
    print("Przy odpowiedziach wpisywanych ręcznie nie używaj polskich znaków. Wielkość liter nie ma znaczenia.\n")
    answer = ""
    while not answer == "start":
        answer = input("Czy możemy zaczynać? Jeśli tak - wpisz '" + colors.GREEN + "start" + colors.RESET + "':   " + colors.GREEN)
    print(colors.RESET)


def _display_progress(decoded_chars: list[str]):
    _clear_screen()
    padding = '_' * (TOTAL_LENGTH - len(decoded_chars))
    print("Prezent: " + ''.join(decoded_chars) + padding)
    print("\n")


def _display_final_message(decoded_message: str):
    print(colors.YELLOW + "+---------------------------------------------+" + colors.RESET)
    print(colors.YELLOW + "|      Wesołych Świąt Bożego Narodzenia!      |" + colors.RESET)
    print(colors.YELLOW + "|                                             |" + colors.RESET)
    print(colors.YELLOW + f"|  Prezent świąteczny to:   {decoded_message}  |" + colors.RESET)
    print(colors.YELLOW + "+---------------------------------------------+" + colors.RESET)
    print("\n\n\n")


def _get_pbar_color(step: int):
    if step <= 4:
        return "red"
    if step <= 11:
        return "yellow"
    return "green"


def run_quiz():
    decoded_chars = []

    # Główna pętla z progress barem
    with tqdm(
        total=16,
        desc="Decoding progress",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        ncols=80
    ) as pbar:
        for i in range(16):
            pbar.colour = _get_pbar_color(i + 1)

            _display_progress(decoded_chars)

            print(f"Decoding character {i+1}/16")
            # input()
            decoded_chars.append("X")

            # Update the progress bar
            pbar.update(1)
            time.sleep(0.2)

            _display_progress(decoded_chars)

    _clear_screen()
    _display_final_message(decoded_message=''.join(decoded_chars))


if __name__ == "__main__":
    run_quiz()
