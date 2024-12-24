import cli
from questions import questions


def run():
    cli.display_greeting()
    salt = cli.get_crypto_salt()
    cli.present_rules()
    cli.run_quiz(questions, salt=salt)


if __name__ == "__main__":
    run()
