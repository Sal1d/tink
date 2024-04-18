import random

import tink_spb_out_integer_with_comment

class Main:
    path_tink_spb_out_integer_with_comment = "ReceiptFont/tink-sbp-out/IntegerWithComment.pdf"
    original_string = "1-14-304-448-003"
    new_color = (0.2, 0.2, 0.2)
    output_path_3 = "check/result.pdf"
    output_path_4 = "check/result_2.pdf"

    def generate_random_string(original_string):
        parts = original_string.split('-')

        prefix = original_string[:4]

        random_part = '-'.join([str(random.randint(100, 999)) for _ in range(3)])

        result = prefix + '-' + random_part
        return result

    def generate_tink_spb_out(self, dateTime, amount, sender, phone, receiver, bank, comment, path):
        if isinstance(amount, int):
            if comment != None:
                generated_string = Main.generate_random_string(self.original_string)
                replacements = [
                    ("10", amount, 1),
                    ("16.04.2024  21:22:23", dateTime, 1),
                    ("10", amount, 1),
                    ("Владислав Скрябин", sender, 1),
                    ("+7 (981) 121-88-27", phone, 1),
                    ("Станислав К.", receiver, 1),
                    ("Сбербанк", bank, 1),
                    ('тест', comment, 1),
                    (self.original_string, generated_string, 1)
                ]
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.path_tink_spb_out_integer_with_comment, path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_3, self.output_path_4, 2.5)

Main().generate_tink_spb_out("99.04.2024  21:22:23", 3323, "фывлфвы", "+7 123123", 'Asdasda', "Tinkoff", "ajjbvkkbv", "final.pdf")