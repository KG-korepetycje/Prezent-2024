from dataclasses import dataclass


@dataclass
class Question:
    question: str
    hashed_answer: str
    encrypted_text: str
    hints: dict[int, str] | None


# ! ORDER OF THE QUESTIONS MATTERS
questions = [
    Question(
        question="Jak się nazywał rejon we Włoszech, gdzie byliśmy na wakacjach w 2023 roku?",
        hashed_answer="d291249966a55bd3a7fce69d616037e3f2d729efc4fbcaf9280344f812fddd31",
        encrypted_text="gAAAAABnafWM1sGb5XMWENEh80LEBZBKETX7m0nnLyZhHDl-XNmdIx6KojDy7H2iJOWjcYWhr1WTVyccpTBGTWsfqaPaYM_jIQ==",
        hints = None
    ),
    Question(
        question="Gdzie urodziła się Ola (miasto)?",
        hashed_answer="6b1524556caf337d5f1a6e3efabdf8b29fda4f9b19d5bf2c689081eb14054606",
        encrypted_text="gAAAAABnafW3ZxAbqLqC-H1gK0ijrzZON_lqJ9aTk5nE7h2Z4YQeDtQ4WuEbtUy0yf5IjbytZKqDpmAyEh_W2bBdXfxECOfkSA==",
        hints = None
    ),
    Question(
        question="W jakim języku mówi się w Brazylii?",
        hashed_answer="30289dc240cebf6fb34a26f2f3c5f5229e9407c647337061065adc5a91d1b668",
        encrypted_text="gAAAAABnafXYVJI5BY788anO0Muv6gRsrIGu7B5KdkcMjZvbCCgJVbxRRxuwA5ZpW2WXolqNUQKRQPB_Him94JtigLHxaoiOGg==",
        hints = {
            1: "włoskim",
            2: "brazylijskim",
            3: "portugalskim",
            4: "hiszpańskim",
        }
    ),
    Question(
        question="Jak na drugie imię ma Twój tata?",
        hashed_answer="42239a2cfc695fc3de49030c7b0c90d6622ac8315e0e00257da478a1916981b6",
        encrypted_text="gAAAAABnafX64Kxfd4PjhpINFA-zTLwmV3Fj9ZdUUifC9A9m-tQlGhhS2siX7Ti1RnNCXgsiUUvyy9ETHt9ffcvcwSnmr9vCEQ==",
        hints = None
    ),
    Question(
        question="Hokkaido to jedna z popularnych odmian...",
        hashed_answer="ff4f10cb53ee5393abadcd665460aefc5492b122644fa8647d8949fafef7f93b",
        encrypted_text="gAAAAABnafYy-yZFy4GQqkkp0NfWpkgsm87fwumtB417sdqA5gGaao2U7FGWht4lnO9QlJwPfp8M2ckXz_vwmcCJvRbBPBRrMw==",
        hints = {
            1: "dyni",
            2: "jabłek",
            3: "papryki",
            4: "arbuza",
        }
    ),
    Question(
        question="Który kraj/kraje Europy pije/piją najwięcej kawy?",
        hashed_answer="e0ad2c839a0214492d1d517378c607086681987c8b7a50a4da39f86b51852c52",
        encrypted_text="gAAAAABnafZWWE9eSmJuhETN1PJC-Re3_Fd1qO5DAkc0f0T6qrgy6xZkwYLxczyWJz-p0H2oEPMHI3qlqGvkjY-xwu87hRlAJA==",
        hints = {
            1: "Hiszpania",
            2: "Włochy i Francja",
            3: "Niemcy",
            4: "Kraje skandynawskie (Finlandia, Norwegia, Islandia, Dania)",
        }
    ),
    Question(
        question="Jaką informatykę studiuje Krzysiek?",
        hashed_answer="8fe361c067d8add9ed838cdb61f6a3e276459adb6dd5289fa783251752bf2e8f",
        encrypted_text="gAAAAABnafZ8uDW-HBhPkYGu2KvIEH-5o7H74XfgPHc2CNFBVNVEnw0dXtYNkvg8WjV8LDUsck2TUMj331xY-mPH8jKSjdO_xw==",
        hints = {
            1: "techniczną",
            2: "stosowaną",
            3: "algorytmiczną",
            4: "teoretyczną",
        }
    ),
    Question(
        question="W jakim mieście Ola robi praktyki w ramach Erasmusa?",
        hashed_answer="e4101fc739f86e33b087440e9ad1b62d18e0c9fd0bf9f058b9bb1527ec9841ce",
        encrypted_text="gAAAAABnafaaWfmcwVdruKWn0zvQy4ysv6Sbb9j76sBZLt31-xspdc61SukBuNR49Cr3oCOg1QEzggYxWdsGdKJsTiGW7D7kmw==",
        hints = None
    ),
    Question(
        question="Co jest stolicą Austrii?",
        hashed_answer="e519dad25ca6d5bdce74efe3fd316fc73cb3d67b928c0ace51e700c76b123482",
        encrypted_text="gAAAAABnafa6JbIQlx54pCm3fGBsZHR9Ote3TJYNr9ZKElOQqn1Dkd5s65WOYbIlceQV8kavfEk9h5kXu0mlIIy29j3dsSrsRQ==",
        hints = None
    ),
    Question(
        question="Gdzie Krzysiek mieszkał przed przeprowadzką na Iwiny (osiedle we Wrocławiu)?",
        hashed_answer="4c572b36fd720c7efba5591f02a9047ee07aad4e41bf0bac7bfe6bb72478374d",
        encrypted_text="gAAAAABnafbPXZKw8wuo0escPEhtAUhnO4Nx854q-xLd7O7uiv54L7slJ0bLSPSMG0Ll8h_-R3g-cjK-KKwFBqjoEC8iKnWZcQ==",
        hints = {
            1: "Klecina",
            2: "Biskupin",
            3: "Brochów",
            4: "Gaj",
            5: "Huby"
        }
    ),
    Question(
        question="Ilu było członków One Direction (podaj dokładną liczbę, np. 2)?",
        hashed_answer="7455265ac4aa040a86c6a32a84339ff25f96a3b4165451b2fc2f2f173c0b67f8",
        encrypted_text="gAAAAABnafb2dLHxaOdZ-prmJnTnhGLOzN1dJy932q69j4x5-_WFeje6VD7r5wXhaIMANv2lXRYBJIzprFad1Ww4GuVDZ-bSJA==",
        hints = None
    ),
    Question(
        question="Czego patronem jest św. Antoni?",
        hashed_answer="1d9b6c5b3ed245fcd36fe021cc39a018d52d8307ed922d2481670fb913e30a7a",
        encrypted_text="gAAAAABnafcSvxBjecMWAUDCFBbY00CkpCHPxQ7RhCHEuzsHGSoSvRXzUshvXk09kG2eYuNKLTD1V5I-7b_9Cae2DXAKnz5RRA==",
        hints = {
            1: "zwierząt domowych",
            2: "rzeczy zaginionych",
            3: "bydła hodowlanego",
            4: "zdrowia dziecka",
        }
    ),
    Question(
        question="Jak na nazwisko ma przyjaciółka Oli - Basia?",
        hashed_answer="163c4077fbe01cb954fede2c95bee0c28f20bfcf60537734d75e34d556a7f3b3",
        encrypted_text="gAAAAABnafc_cIbUNYTGZI7iPy8LbMEIANi8XmmdS5X5Nh8_QUYXWnGmHBXDLc6BO2zPAeVEMZE2wAtWZvtLrcAt0vuCjL5Nig==",
        hints = {
            1: "Frankowska",
            2: "Blok",
            3: "Skałecka",
            4: "Galant",
        }
    ),
    Question(
        question="Jak nazywa się miejscowość, w której mieszka dziadek Andrzej?",
        hashed_answer="bfc7e33d4374e879a2de883fe6cfd817f8d590527a142b58351f1dfa7d954afd",
        encrypted_text="gAAAAABnafdY7Ag56MKUCu0k6UOO6UGY_0PvhVibF1Ec09yi6mXTGoVLjs-V-kl4kcOeU_T49XMJM8HW5eor4ZhCeIzjaEk1yA==",
        hints = None
    ),
    Question(
        question="Jak się nazywa szkoła, w której pracuje Twoja mama?",
        hashed_answer="23c15667c5192da996f60dd24a703aec507280dff897ce133fc86a9f1d72e0a5",
        encrypted_text="gAAAAABnafdteSgBn5QFQRxiz-0cs5gWd8uBpsZIaLwKu5xH7NS3JQSZaHeFGQQ5luP_fJhvQGJolki2_xSOsMOrW014IHQZdw==",
        hints = None
    ),
    Question(
        question="Jak się nazywał kanarek Oli?",
        hashed_answer="f945ea8c6f94c8b98510009c8400127081f7d3f530c1374f3ec2c39a24b239df",
        encrypted_text="gAAAAABnafeAFkFK1JrnsBB6ii4jRnfRUtkLR4p-_-1n8x_-KOeWEV_KtfOLCNY5ulnp9QtHf2nmTQaLWCPaT4FzyBlEuzXw6w==",
        hints = None
    ),
]
