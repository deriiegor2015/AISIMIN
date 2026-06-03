import random

class AIOperator100G:
    def __init__(self, operator_id):
        self.operator_id = operator_id
        self.active_numbers = []
        self.data_streams = {}

    def create_number(self):
        new_number = f"{random.randint(100,999)}-100G-{self.operator_id}"
        self.active_numbers.append(new_number)
        self.data_streams[new_number] = []
        print(f"🚀 Оператор {self.operator_id} створив номер: {new_number}")
        return new_number

    def call(self, from_number, to_number):
        if to_number in self.active_numbers:
            print(f"📞 Дзвінок у 100G: {from_number} ➡️ {to_number}")
        else:
            print(f"❌ Номер {to_number} поза мережею")

    def send_sms(self, from_number, to_number, message):
        if to_number in self.active_numbers:
            print(f"✉️ SMS у 100G від {from_number} до {to_number}: {message}")
        else:
            print(f"❌ SMS не доставлено: {to_number} не існує")

    def start_data_stream(self, number, content="VR‑світ"):
        if number in self.data_streams:
            stream_id = f"100G-{random.randint(1000,9999)}"
            self.data_streams[number].append(stream_id)
            print(f"⚡ 100G‑потік {stream_id} активовано для {number} ({content})")
        else:
            print(f"❌ Номер {number} не підтримує 100G")

# Симуляція
operator = AIOperator100G(2030)
num1 = operator.create_number()
num2 = operator.create_number()

operator.call(num1, num2)
operator.send_sms(num1, num2, "Привіт із 100G 🌐")
operator.start_data_stream(num2, content="Стрім VR‑гри")
