import random

import tink_spb_out_float
import tink_spb_out_integer
import tink_spb_out_integer_with_comment
import tink_spb_out_float_with_cooment
import spb_tink_in_integer
import spb_tink_in_float
import tink_tink_in_flout
import tink_tink_in_integer
import tink_tink_out_float
import tink_tink_out_integer


class Main:
    path_tink_spb_out_integer_with_comment = "ReceiptFont/tink-sbp-out/IntegerWithComment.pdf"
    path_tink_spb_out_integer_without_comment = "ReceiptFont/tink-sbp-out/Integer.pdf"
    path_tink_spb_out_float_with_comment = "ReceiptFont/tink-sbp-out/FloatWithComment.pdf"
    # добавить тиньк спб аут флоут без комента
    path_tink_spb_out_float_without_comment = "ReceiptFont/tink-sbp-out/FloatWithComment.pdf"
    path_spb_tink_in_integer = "ReceiptFont/sbp-tink-in/Integer.pdf"
    path_spb_tink_in_float = "ReceiptFont/sbp-tink-in/Float.pdf"
    path_tink_tink_in_integer = "ReceiptFont/tink-tink-in/Integer.pdf"
    path_tink_tink_in_float = "ReceiptFont/tink-tink-in/Float.pdf"
    path_tink_tink_out_integer = "ReceiptFont/tink-tink-out/Integer.pdf"
    path_tink_tink_out_float = "ReceiptFont/tink-tink-out/Float.pdf"

    original_string = "1-14-304-448-003"
    new_color = (0.2, 0.2, 0.2)
    text = "400"
    output_path = "check/modified_document.pdf"
    output_path_2 = "check/modified_document_2.pdf"
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
        if ',' not in amount:
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
                tink_spb_out_integer_with_comment.replace_text_custom(self.path_tink_spb_out_integer_with_comment, self.output_path, [replacements[0]], self.font_path, self.new_size, self.new_color,
                                      self.output_path_2, self.output_path_3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_3, self.output_path, [replacements[1]], "d/fonts/dsHeading/400.ttf", 8,
                                      (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2,
                                      self.output_path_4, 2.5)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 9,
                                      self.new_color,
                                      self.output_path_2, self.output_path_5, 2.5)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 9,
                                      self.new_color,
                                      self.output_path_2, self.output_path_6, 3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9,
                                      self.new_color,
                                      self.output_path_2, self.output_path_7, 3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9,
                                      self.new_color,
                                      self.output_path_2, self.output_path_8, 2.5)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_8, self.output_path, [replacements[6]], "d/fonts/dsHeading/400.ttf", 9,
                                      self.new_color,
                                      self.output_path_2, self.output_path_9, 3)
                tink_spb_out_integer_with_comment.replace_text_custom_2(self.output_path_9, self.output_path, [replacements[7]], "d/fonts/dsHeading/400.ttf", 9,
                                      self.new_color,
                                      self.output_path_2, path, 3)
            else:
                generated_string = Main.generate_random_string(self.original_string)
                replacements = [
                    ("500", amount, 1),
                    ("25.02.2024  19:29:24", dateTime, 1),
                    ("500", amount, 1),
                    ("Владислав Скрябин", sender, 1),
                    ("+7 (911) 199-10-58", phone, 1),
                    ("Милана Б.", receiver, 1),
                    ("Сбербанк", bank, 1),
                    (self.original_string, generated_string, 1)
                ]
                tink_spb_out_integer.replace_text_custom(self.path_tink_spb_out_integer_without_comment, self.output_path, [replacements[0]], self.font_path, self.new_size, self.new_color, self.output_path_2, self.output_path_3)
                tink_spb_out_integer.replace_text_custom_2(self.output_path_3, self.output_path, [replacements[1]], "d/fonts/dsHeading/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_4, 2.5)
                tink_spb_out_integer.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_5, 2.5)
                tink_spb_out_integer.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_6, 3)
                tink_spb_out_integer.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_7, 3)
                tink_spb_out_integer.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_8, 2.5)
                tink_spb_out_integer.replace_text_custom_2(self.output_path_8, self.output_path, [replacements[6]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, path, 3)

        else:
            if comment != None:
                generated_string = Main.generate_random_string(self.original_string)
                replacements = [
                    ("12", amount[0: amount.find(',')], 1),
                    (",30", amount[amount.find(','):], 1),
                    ("04.04.2024  11:46:03", dateTime, 1),
                    ("12,30", amount, 1),
                    ("Владислав Скрябин", sender, 1),
                    ("+7 (981) 121-88-27", phone, 1),
                    ("Станислав К.", receiver, 1),
                    ("Сбербанк", bank, 1),
                    ('привет', comment, 1),
                    (self.original_string, generated_string, 1)
                ]
                tink_spb_out_float_with_cooment.replace_text_custom(self.path_tink_spb_out_float_with_comment, self.output_path, [replacements[0]], self.font_path, self.new_size, self.new_color, self.output_path_2,
                    self.output_path_3)
                tink_spb_out_float_with_cooment.replace_text_custom(self.output_path_3, self.output_path, [replacements[1]], self.font_path, 16,
                    (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_4)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 8,
                      (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_5, 2.5)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_2, self.output_path_6, 2.5)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_2, self.output_path_7, 3)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_2, self.output_path_8, 3)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_8, self.output_path, [replacements[6]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_2, self.output_path_9, 2.5)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_9, self.output_path, [replacements[7]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_2, self.output_path_10, 3)
                tink_spb_out_float_with_cooment.replace_text_custom_2(self.output_path_10, self.output_path, [replacements[8]], "d/fonts/dsHeading/400.ttf", 9, self.new_color,
                      self.output_path_2, path, 2.5)
            else:
                generated_string = Main.generate_random_string(self.original_string)
                replacements = [
                    ("12", amount[0: amount.find(',')], 1),
                    (",30", amount[amount.find(','):], 1),
                    ("04.04.2024  11:46:03", dateTime, 1),
                    ("12,30", amount, 1),
                    ("Владислав Скрябин", sender, 1),
                    ("+7 (981) 121-88-27", phone, 1),
                    ("Станислав К.", receiver, 1),
                    ("Сбербанк", bank, 1),
                    (self.original_string, generated_string, 1)
                ]
                tink_spb_out_float.replace_text_custom(self.path_tink_spb_out_float_without_comment, self.output_path, [replacements[0]], self.font_path, self.new_size, self.new_color, self.output_path_2, self.output_path_3)
                tink_spb_out_float.replace_text_custom(self.output_path_3, self.output_path, [replacements[1]],self.font_path , 16,(0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_4)
                tink_spb_out_float.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_5, 2.5)
                tink_spb_out_float.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_6, 2.5)
                tink_spb_out_float.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_7, 3)
                tink_spb_out_float.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_8, 3)
                tink_spb_out_float.replace_text_custom_2(self.output_path_8, self.output_path, [replacements[6]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_9, 2.5)
                tink_spb_out_float.replace_text_custom_2(self.output_path_9, self.output_path, [replacements[7]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_10, 3)
                tink_spb_out_float.replace_text_custom_2(self.output_path_10, self.output_path, [replacements[8]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, path, 2.5)

    def generate_spb_tink_in(self, dateTime, amount, phone, rnn, path):
        if '.' not in amount:
            generated_string = Main.generate_random_string(self.original_string)
            replacements = [
                ("1 000", amount, 1),
                ("25.02.2024  19:22:33", dateTime, 1),
                ("+7 (981) 032-89-83", phone, 1),
                ('011993662247', rnn, 1),
                (self.original_string, generated_string, 1)
            ]
            spb_tink_in_integer.replace_text_custom(self.path_spb_tink_in_integer, self.output_path, [replacements[0]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, self.new_color, self.output_path_2, self.output_path_3)
            spb_tink_in_integer.replace_text_custom_2(self.output_path_3, self.output_path, [replacements[1]], "d/fonts/dsText/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_4, 2.75)
            spb_tink_in_integer.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsText/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_5, 2.75)
            spb_tink_in_integer.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsText/400.ttf", 9,self. new_color, self.output_path_2, path, 2.75)
        else:
            generated_string = Main.generate_random_string(self.original_string)
            replacements = [
                ("1.23", amount, 1),
                (amount[0: amount.find('.')], amount[0: amount.find('.')], 1),
                (amount[amount.find('.'):], amount[amount.find('.'):], 1),
                ("04.04.2024  11:49:13", dateTime, 1),
                ("+7 (995) 596-64-99", phone, 1),
                ('012558387964', rnn, 1),
                (self.original_string, generated_string, 1)
            ]
            spb_tink_in_float.replace_text_custom(self.path_spb_tink_in_float, self.output_path, [replacements[0]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, self.new_color, self.output_path_2, self.output_path_3)
            spb_tink_in_float.replace_text_custom(self.output_path_3, self.output_path, [replacements[1]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, self.new_color, self.output_path_2, self.output_path_4)
            spb_tink_in_float.replace_text_custom(self.output_path_4, self.output_path, [replacements[2]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size , (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_5)
            spb_tink_in_float.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsText/400.ttf", 8,(0.5647058823529412, 0.5647058823529412, 0.5647058823529412) , self.output_path_2, self.output_path_6, 2.75)
            spb_tink_in_float.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsText/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_7, 2.75)
            spb_tink_in_float.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsText/400.ttf", 9 , self.new_color, self.output_path_2, path, 2.75)


    def generate_tink_tink_in(self, dateTime, amount, document, rnn, path):
        if '.' not in amount:
            generated_string = Main.generate_random_string(self.original_string)
            replacements = [
                ("300", amount, 1),
                ("01.03.2024  14:45:18", dateTime, 1),
                ("5404050596", document, 1),
                ('012064577913', rnn, 1),
                (self.original_string, generated_string, 1)
            ]
            tink_tink_in_integer.replace_text_custom(self.path_tink_tink_in_integer, self.output_path, [replacements[0]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, self.new_color, self.output_path_2, self.output_path_3)
            tink_tink_in_integer.replace_text_custom_2(self.output_path_3, self.output_path, [replacements[1]], "d/fonts/dsText/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_4, 2.75)
            tink_tink_in_integer.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsText/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_5, 2.75)
            tink_tink_in_integer.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsText/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_6, 2.75)
            tink_tink_in_integer.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsText/400.ttf", 8, self.new_color, self.output_path_2, path, 2.75)
        else:
            generated_string = Main.generate_random_string(self.original_string)
            replacements = [
                ("0.12", amount, 1),
                (amount[0: amount.find('.')], amount[0: amount.find('.')], 1),
                (amount[amount.find('.'):], amount[amount.find('.'):], 1),
                ("04.04.2024  10:51:47", dateTime, 1),
                ("5404050596", document, 1),
                ('012557512032', rnn, 1),
                (self.original_string, generated_string, 1)
            ]
            tink_tink_in_flout.replace_text_custom(self.path_tink_tink_in_float, self.output_path, [replacements[0]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, self.new_color, self.output_path_2, self.output_path_3)
            tink_tink_in_flout.replace_text_custom(self.output_path_3, self.output_path, [replacements[1]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, self.new_color, self.output_path_2, self.output_path_4)
            tink_tink_in_flout.replace_text_custom(self.output_path_4, self.output_path, [replacements[2]], "ТЗ на чеки/ReceiptFont/sbp-tink-in/Heading.ttf", self.new_size, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_5)
            tink_tink_in_flout.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsText/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_6, 2.75)
            tink_tink_in_flout.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsText/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_7, 2.75)
            tink_tink_in_flout.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsText/400.ttf", 9, self.new_color, self.output_path_2, path, 2.75)

    def generate_tink_tink_out(self, dateTime, amount, sender, phone, receiver, path):
        if ',' not in amount:
            generated_string = Main.generate_random_string(self.original_string)
            replacements = [
                ("100", amount, 1),
                ("05.03.2024  17:32:47", dateTime, 1),
                ("100", amount, 1),
                ("Владислав Скрябин", sender, 1),
                ("+7 (911) 088-72-91", phone, 1),
                ("Михаил С.", receiver, 1),
                (self.original_string, generated_string, 1)
            ]
            tink_tink_out_integer.replace_text_custom(self.path_tink_tink_out_integer, self.output_path, [replacements[0]], self.font_path, self.new_size, self.new_color, self.output_path_2, self.output_path_3)
            tink_tink_out_integer.replace_text_custom_2(self.output_path_3, self.output_path, [replacements[1]], "d/fonts/dsHeading/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_4, 2.5)
            tink_tink_out_integer.replace_text_custom_2(self.output_path_4, self.output_path, [replacements[2]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_5, 2.5)
            tink_tink_out_integer.replace_text_custom_2(self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_6, 3)
            tink_tink_out_integer.replace_text_custom_2(self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_7, 3)
            tink_tink_out_integer.replace_text_custom_2(self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, path, 2.5)
        else:
            generated_string = Main.generate_random_string(self.original_string)
            replacements = [
                ("0,12", amount, 1),
                (amount[0: amount.find(',')], amount[0: amount.find(',')], 1),
                (amount[amount.find(','):], amount[amount.find(','):], 1),
                ("02.04.2024 17:22:28", dateTime, 1),
                ("0,12", amount, 1),
                ("Владислав Скрябин", sender, 1),
                ("+7 (981) 121-88-27", phone, 1),
                ("Станислав К.", receiver, 1),
                (self.original_string, generated_string, 1)
            ]
            tink_tink_out_float.replace_text_custom(self.path_tink_tink_out_float, self.output_path, [replacements[0]], self.font_path, self.new_size, self.new_color, self.output_path_2, self.output_path_3)
            tink_tink_out_float.replace_text_custom( self.output_path_3,  self.output_path, [replacements[1]], self.font_path , 16, self.new_color, self.output_path_2, self.output_path_4)
            tink_tink_out_float.replace_text_custom( self.output_path_4,  self.output_path, [replacements[2]], self.font_path, self.new_size, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_5)
            tink_tink_out_float.replace_text_custom_2( self.output_path_5, self.output_path, [replacements[3]], "d/fonts/dsHeading/400.ttf", 8, (0.5647058823529412, 0.5647058823529412, 0.5647058823529412), self.output_path_2, self.output_path_6, 2.5)
            tink_tink_out_float.replace_text_custom_2( self.output_path_6, self.output_path, [replacements[4]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_7, 2.5)
            tink_tink_out_float.replace_text_custom_2( self.output_path_7, self.output_path, [replacements[5]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_8, 3)
            tink_tink_out_float.replace_text_custom_2( self.output_path_8, self.output_path, [replacements[6]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_9, 3)
            tink_tink_out_float.replace_text_custom_2( self.output_path_9, self.output_path, [replacements[7]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, self.output_path_10, 2.5)
            tink_tink_out_float.replace_text_custom_2( self.output_path_10, self.output_path, [replacements[8]], "d/fonts/dsHeading/400.ttf", 9, self.new_color, self.output_path_2, path, 3)

# tink-spb-out int comment ТУТ ДРОБЬ ЧЕРЕЗ ЗАПЯТУЮ
#Main().generate_tink_spb_out("99.04.2024  21:22:23", "3323", "фывлфвы", "+7 123123", 'Asdasda', "Tinkoff", "тут комент", "final.pdf")
# tink-spb-out int no comment
#Main().generate_tink_spb_out("99.04.2024  21:22:23", "3323,43", "фывлфвы", "+7 123123", 'Asdasda', "Tinkoff", None, "final.pdf")
# tink-spb-out float comment
# Main().generate_tink_spb_out("99.04.2024  21:22:23", "3323,33", "фывлфвы", "+7 123123", 'Asdasda', "Tinkoff", "тут комент", "final.pdf")
# tink-spb-out float no comment не проверял ибо нет шаблона
#Main().generate_tink_spb_out("99.04.2024  21:22:23", "3323,34", "фывлфвы", "+7 123123", 'Asdasda', "Tinkoff", None, "final.pdf")


#spb-tink-in integer
#Main().generate_spb_tink_in("99.04.2024 21:22:33", "999", "+7 123123", "245565", "final.pdf")
#spb-tink-in float (ТУТ ДРОБЬ ЧЕРЕЗ ТОЧКУ)
# Main().generate_spb_tink_in("99.04.2024 21:22:33", "999.23", "+7 123123", "245565", "final.pdf")

# tink-tink-in integer
# Main().generate_tink_tink_in("92.04.2024 21:22:33", "993", "+7 124123", "245565", "final.pdf")
# tink-tink-in float ЧЕРЕЗ ТОЧКУ
# Main().generate_tink_tink_in("92.04.2024 21:22:33", "993.7", "+7 124123", "245565", "final.pdf")

# tink-tink-out integer
# Main().generate_tink_tink_out("92.04.2024 21:22:33", "993", "+7 124123", "245565", "final.pdf", "final.pdf")
# tink-tink-out float ЧЕРЕЗ ТОЧКУ
Main().generate_tink_tink_out("92.04.2024 21:22:33", "993,32", "+7 124123", "245565", "final.pdf", "final.pdf")




