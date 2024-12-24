import os
import random
import re
import time

from tqdm import tqdm
from unidecode import unidecode

import colors
import crypto
from questions import Question

SALT_VERIFICATION_HASH = "604d4568848db19c20777fb02150482347a1d213ffd76ed6604a5ea78ef65f40"
SALT_VERIFICATION_ENCRYPTED_TEXT = "gAAAAABnaeXslw9MT8bvTcAM2FenajsoWzbmgaUQfJsPGZoLhgJg5rtVU977SuqfYlhuPASnGKpV-E5a2QTUYMF5jRPBJeKGE3T0qQkBfChy1WutkwbKgyNgkcppaMUrLrN5af4BdhiQ1t6msnILa2Jw7-TZ0o1vZ-j5PQvld6y3KWJywiax4-4="


def _clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_greeting():
    _clear_screen()
    print(colors.YELLOW + "+---------------------------------------------+" + colors.RESET)
    print(colors.YELLOW + "|                 Cześć Antek!                |" + colors.RESET)
    print(colors.YELLOW + "|        Witaj w świątecznym quizie...        |" + colors.RESET)
    print(colors.YELLOW + "+---------------------------------------------+" + colors.RESET)
    print("\n")


def _identity_verification(school_name: str, salt: str) -> bool:
    hash_comparison = crypto.generate_hash(school_name, salt) == SALT_VERIFICATION_HASH
    if not hash_comparison:
        print("\n" + colors.RED + "Weryfikacja tożsamości nie powiodła się" + colors.RESET + "\n")
        return False

    decrypted_text = crypto.decrypt_text(
        encrypted_text=SALT_VERIFICATION_ENCRYPTED_TEXT,
        password=school_name.lower(),
        salt=salt
    )
    print("\n" + colors.RESET + "Twoja tożsamość została " + colors.GREEN + "pomyślnie" + colors.RESET + " zweryfikowana!")
    print("Odszyfrowany tekst: " + colors.YELLOW + decrypted_text + colors.RESET + "\n")
    return True


def get_crypto_salt() -> str:
    print("WERYFIKACJA TOŻSAMOŚCI")
    print("----------------------")
    print("Jeśli poprawnie odpowiesz na 2 pytania to odszyfrujesz następujący tekst: " + colors.YELLOW + SALT_VERIFICATION_ENCRYPTED_TEXT + colors.RESET + "\n")
    pattern = r"^\d{2}\.\d{2}\.\d{4}$"
    while True:
        school_name = input("Podaj nazwę szkoły podstawowej, do której chodziłeś (wielkość liter bez znaczenia):  ")
        date = input("Podaj datę swoich urodzin w formacie DD.MM.YYYY:  ")
        if re.match(pattern, date):
            result = _identity_verification(school_name.lower(), date)
            if result:
                input("Wciśnij ENTER aby przejść dalej")
                return date
        else:
            print(colors.RED + "Niepoprawny format. Upewnij się, że wpisujesz datę w formacie DD.MM.YYYY." + colors.RESET + "\n")


def present_rules():
    _clear_screen()
    print("Zasady są bardzo proste:")
    print("1. Jeśli pytanie ma różne odpowiedzi do wyboru - podaj samą cyferkę przypisaną do odpowiedzi.")
    print("2. Jeśli nie ma odpowiedzi do wyboru - wpisz odpowiedź ręcznie.\n")
    print(colors.RED + "UWAGA!" + colors.RESET)
    print("Przy odpowiedziach wpisywanych ręcznie nie używaj polskich znaków. Wielkość liter nie ma znaczenia.\n")
    while True:
        answer = input("Czy możemy zaczynać? Jeśli tak - wpisz '" + colors.GREEN + "start" + colors.RESET + "':   " + colors.GREEN)
        if answer.lower() == "start":
            print(colors.RESET)
            return


def _display_progress(decoded_chars: list[str], total_length: int):
    _clear_screen()
    print(f"Odszyfrowywanie znaku {len(decoded_chars) + 1}/{total_length}")
    padding = '_' * (total_length - len(decoded_chars))
    print("Prezent: " + ''.join(decoded_chars) + padding)
    print("\n")


def _animation():
    stages = [
        ("Preparing", 20, colors.CYAN),
        ("Configuring", 30, colors.YELLOW),
        ("Installing", 40, colors.GREEN),
        ("Finalizing", 10, colors.MAGENTA)
    ]

    for desc, steps, color in stages:
        with tqdm(
            total=steps,
            desc=f"{color}{desc}{colors.RESET}",
            bar_format="{l_bar}{bar}| {percentage:3.0f}%",
            ncols=70
        ) as pbar:
            for _ in range(steps):
                time.sleep(random.uniform(steps * 0.001, steps * 0.01))
                pbar.update(1)


def _display_final_message(decoded_message: str):
    chunks = [decoded_message[i:i+4] for i in range(0, len(decoded_message), 4)]
    chunked_message = ' '.join(chunks)
    print(colors.YELLOW + "+------------------------------------------------+" + colors.RESET)
    print(colors.YELLOW + "|        Wesołych Świąt Bożego Narodzenia!       |" + colors.RESET)
    print(colors.YELLOW + "|                                                |" + colors.RESET)
    print(colors.YELLOW + "|  Prezent świąteczny to:   " + colors.GREEN + chunked_message + colors.YELLOW + "  |" + colors.RESET)
    print(colors.YELLOW + "+------------------------------------------------+" + colors.RESET)
    print("\n\n\n")


def _get_pbar_color(step: int):
    if step <= 4:
        return "red"
    if step <= 11:
        return "yellow"
    return "green"


def run_quiz(questions: list[Question], salt: str):
    _clear_screen()
    decoded_chars = []
    total_length = len(questions)

    with tqdm(
        total=total_length,
        desc="Postęp",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
        ncols=80
    ) as pbar:
        for i, question in enumerate(questions):
            pbar.colour = _get_pbar_color(i + 1)
            _display_progress(decoded_chars, total_length)
            print(colors.YELLOW + "PYTANIE: " + colors.RESET + question.question)
            if question.hints:
                for key, val in question.hints.items():
                    print(f"[{key}] {val}")
            while True:
                answer = input(colors.YELLOW + "\nODPOWIEDŹ:  " + colors.RESET)
                if answer:
                    if question.hints:
                        mini = min(list(question.hints.keys()))
                        maxi = max(list(question.hints.keys()))
                        try:
                            answer = int(answer)
                            answer = question.hints[answer]
                        except Exception:
                            print(colors.RED + f"Wybierz poprawny numer odpowiedzi [{mini} - {maxi}]." + colors.RESET)
                            continue
                    else:
                        answer = unidecode(answer.lower())

                    is_correct = (crypto.generate_hash(answer, salt) == question.hashed_answer)
                    print()
                    if is_correct:
                        print(colors.GREEN + "Dobrze!" + colors.RESET)
                        decoded_char = crypto.decrypt_text(
                            encrypted_text=question.encrypted_text,
                            password=answer,
                            salt=salt
                        )
                        decoded_chars.append(decoded_char)
                        break
                    print(colors.RED + "Źle..." + colors.RESET)

            # Update the progress bar
            pbar.update(1)
            time.sleep(1.25)
            _display_progress(decoded_chars, total_length)

    _clear_screen()
    _animation()
    _clear_screen()
    _display_final_message(decoded_message=''.join(decoded_chars))
