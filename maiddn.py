import random

import tink_spb_out_integer_with_comment


class Main:
    path_tink_spb_out_integer_with_comment = "ReceiptFont/tink-sbp-out/IntegerWithComment.pdf"
    original_string = "1-14-304-448-003"
    new_color = (0.2, 0.2, 0.2)
    text = "400"
    output_path = "modified_document.pdf"
    output_path_2 = "modified_document_2.pdf"
    output_path_3 = "check/result.pdf"
    output_path_4 = "check/result_2.pdf"
    output_path_5 = "check/result_3.pdf"
    output_path_6 = "check/result_4.pdf"
    output_path_7 = "check/result_5.pdf"
    output_path_8 = "check/result_6.pdf"
    output_path_9 = "check/result_7.pdf"
    output_path_10 = "final.pdf"
    font_path = "d/fonts/EEX.ttf"
    new_size = 16

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
                pdf_path = "ReceiptFont/tink-sbp-out/IntegerWithComment.pdf"
                tink_spb_out_integer_with_comment.replace_text_custom(pdf_path, self.output_path, [replacements[0]],
                                                                      self.font_path, self.new_size, self.new_color,
                                                                      self.output_path_2,
                                                                      self.output_path_3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[1]],
                                                                        "d/fonts/dsHeading/400.ttf", 8,
                                                                        (0.5647058823529412, 0.5647058823529412,
                                                                         0.5647058823529412), self.output_path_2,
                                                                        self.output_path_4, 2.5)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[2]],
                                                                        "d/fonts/dsHeading/400.ttf", 9,
                                                                        self.new_color,
                                                                        self.output_path_2, self.output_path_5, 2.5)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[3]],
                                                                        "d/fonts/dsHeading/400.ttf", 9,
                                                                        self.new_color,
                                                                        self.output_path_2, self.output_path_6, 3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[4]],
                                                                        "d/fonts/dsHeading/400.ttf", 9,
                                                                        self.new_color,
                                                                        self.output_path_2, self.output_path_7, 3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[5]],
                                                                        "d/fonts/dsHeading/400.ttf", 9,
                                                                        self.new_color,
                                                                        self.output_path_2, self.output_path_8, 2.5)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[6]],
                                                                        "d/fonts/dsHeading/400.ttf", 9,
                                                                        self.new_color,
                                                                        self.output_path_2, self.output_path_9, 3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(pdf_path, self.output_path, [replacements[7]],
                                                                        "d/fonts/dsHeading/400.ttf", 9,
                                                                        self.new_color,
                                                                        self.output_path_2, path, 3)


Main().generate_tink_spb_out("99.04.2024  21:22:23", 3323, "фывлфвы", "+7 123123", 'Asdasda', "Tinkoff", "ajjbvkkbv",
                             "final.pdf")
